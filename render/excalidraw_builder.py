"""
Sketion Excalidraw Builder Core (Render Layer) 2.8
Generador de escenas .excalidraw con:
- Dimensiones dinámicas de tarjeta (Cero desbordamiento de texto)
- Pastillas protectoras de fondo para etiquetas de flechas (Cero colisiones con líneas)
- Auto-Fit de Frames (Cero espacios blancos muertos)
- Vinculación estricta containerId <-> boundElements
"""

import json
import random
import string
import math
from typing import List, Dict, Any, Optional, Tuple
from layout.routing import compute_orthogonal_arrow

def rid(length: int = 16) -> str:
    """Genera un identificador único aleatorio para Excalidraw."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

# --- CURSOR DE LAYOUT EN FLUJO ---
_CURSOR = {"x": 0, "y": 0, "row_h": 0, "max_row_w": 4700, "gap": 150}

def place_reset(max_row_w: int = 4700, gap: int = 150):
    """Reinicia el cursor de layout."""
    global _CURSOR
    _CURSOR = {"x": 0, "y": 0, "row_h": 0, "max_row_w": max_row_w, "gap": gap}

def place(w: float, h: float) -> Tuple[float, float]:
    """Calcula la posición (x, y) del siguiente bloque en el canvas."""
    global _CURSOR
    if _CURSOR["x"] + w > _CURSOR["max_row_w"] and _CURSOR["x"] > 0:
        _CURSOR["x"] = 0
        _CURSOR["y"] += _CURSOR["row_h"] + _CURSOR["gap"]
        _CURSOR["row_h"] = 0
    x, y = _CURSOR["x"], _CURSOR["y"]
    _CURSOR["x"] += w + _CURSOR["gap"]
    _CURSOR["row_h"] = max(_CURSOR["row_h"], h)
    return x, y


def compute_card_dimensions(title: str, sublabel: Optional[str] = None,
                            metadata: Optional[str] = None,
                            font_size: int = 14, min_w: float = 240.0) -> Tuple[float, float]:
    """
    Calcula matemáticamente el ancho y alto necesarios para albergar el texto
    sin desbordamiento ni cortes de palabras.
    """
    raw_lines = [title]
    if sublabel and metadata:
        raw_lines.append(f"{sublabel} {metadata}")
    elif sublabel:
        raw_lines.append(sublabel)
    elif metadata:
        raw_lines.append(metadata)

    # Considerar saltos de línea explícitos dentro de cada texto
    expanded_lines = []
    for l in raw_lines:
        expanded_lines.extend(str(l).split("\n"))

    max_chars = max((len(l) for l in expanded_lines), default=10)
    
    # 8.8px por caracter para Sans 14px + 45px de padding horizontal
    w = max(min_w, max_chars * 9.0 + 45.0)
    
    # 24px por línea + 40px de padding vertical
    h = max(85.0, 36.0 + len(expanded_lines) * 22.0)
    
    return w, h


class ExcalidrawScene:
    """Constructor de tableros Excalidraw nativos."""

    def __init__(self, roughness: int = 0, bg_color: str = "#ffffff", grid_size: int = 20):
        self.roughness = roughness
        self.bg_color = bg_color
        self.grid_size = grid_size
        self.elements: List[Dict[str, Any]] = []

    def _base_element(self, elem_type: str, x: float, y: float, w: float, h: float,
                      stroke_color: str = "#0C0C0C", bg_color: str = "transparent",
                      stroke_width: float = 1.5, stroke_style: str = "solid",
                      frame_id: Optional[str] = None, angle: float = 0.0,
                      roundness: Optional[Dict[str, Any]] = None, opacity: int = 100,
                      stroke_w: Optional[float] = None) -> Dict[str, Any]:
        final_stroke_w = stroke_w if stroke_w is not None else stroke_width
        return {
            "type": elem_type,
            "version": 1,
            "versionNonce": random.randint(1, 2**31 - 1),
            "isDeleted": False,
            "id": rid(),
            "fillStyle": "solid",
            "strokeWidth": final_stroke_w,
            "strokeStyle": stroke_style,
            "roughness": self.roughness,
            "opacity": opacity,
            "angle": angle,
            "x": x,
            "y": y,
            "strokeColor": stroke_color,
            "backgroundColor": bg_color,
            "width": w,
            "height": h,
            "seed": random.randint(1, 2**31 - 1),
            "groupIds": [],
            "frameId": frame_id,
            "roundness": roundness,
            "boundElements": [],
            "updated": 1,
            "link": None,
            "locked": False
        }

    def add_frame(self, name: str, x: float, y: float, w: float, h: float) -> str:
        """Crea un frame contenedor en el canvas."""
        elem = self._base_element("frame", x, y, w, h, stroke_color="#CBD5E1", bg_color="transparent")
        elem["name"] = name
        self.elements.append(elem)
        return elem["id"]

    def auto_fit_frame(self, frame_id: str, padding: float = 60.0):
        """Ajusta automáticamente el ancho y alto del frame según sus elementos contenidos."""
        frame = next((e for e in self.elements if e.get("id") == frame_id and e.get("type") == "frame"), None)
        if not frame:
            return

        children = [e for e in self.elements if e.get("frameId") == frame_id and e.get("type") != "frame"]
        if not children:
            return

        fx = frame["x"]
        fy = frame["y"]

        max_x = max((c["x"] + c.get("width", 0) for c in children), default=fx + 800)
        max_y = max((c["y"] + c.get("height", 0) for c in children), default=fy + 600)

        frame["width"] = max(400.0, (max_x - fx) + padding)
        frame["height"] = max(300.0, (max_y - fy) + padding)

    def add_rect(self, x: float, y: float, w: float, h: float,
                 bg: str = "transparent", stroke: str = "#0C0C0C",
                 stroke_w: float = 1.5, stroke_style: str = "solid",
                 roundness_type: Optional[int] = 3, frame_id: Optional[str] = None,
                 angle_deg: float = 0.0) -> Dict[str, Any]:
        """Crea un rectángulo base."""
        roundness = {"type": roundness_type} if roundness_type is not None else None
        angle_rad = math.radians(angle_deg) if angle_deg != 0 else 0.0
        elem = self._base_element("rectangle", x, y, w, h, stroke, bg, stroke_w, stroke_style, frame_id, angle_rad, roundness)
        self.elements.append(elem)
        return elem

    def add_ellipse(self, x: float, y: float, w: float, h: float,
                    bg: str = "transparent", stroke: str = "#0C0C0C",
                    stroke_w: float = 1.5, frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea una elipse base."""
        elem = self._base_element("ellipse", x, y, w, h, stroke, bg, stroke_w, "solid", frame_id)
        self.elements.append(elem)
        return elem

    def add_text(self, x: float, y: float, text: str,
                 font_size: int = 14, font_family: int = 2,
                 color: str = "#0C0C0C", align: str = "left",
                 frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea un texto libre con ancho calculado generosamente para evitar cortes."""
        lines = text.split("\n")
        line_h = 1.25
        est_h = max(25.0, len(lines) * font_size * line_h)
        # Factor 0.80 + 35px para evitar truncamientos en la renderización de Excalidraw
        est_w = max((len(l) for l in lines), default=4) * (font_size * 0.80) + 35.0 if lines else 60.0

        elem = self._base_element("text", x, y, est_w, est_h, color, "transparent", frame_id=frame_id)
        elem.update({
            "fontSize": font_size,
            "fontFamily": font_family,
            "text": text,
            "textAlign": align,
            "verticalAlign": "top",
            "containerId": None,
            "originalText": text,
            "lineHeight": line_h,
            "baseline": font_size
        })
        self.elements.append(elem)
        return elem

    def add_bound_card(self, x: float, y: float, w: float, h: float, text: str,
                       bg: str = "#FFFFFF", stroke: str = "#0C0C0C",
                       text_color: str = "#0C0C0C", font_size: int = 14,
                       font_family: int = 2, align: str = "center",
                       stroke_w: float = 1.5, stroke_style: str = "solid",
                       roundness_type: Optional[int] = 3, frame_id: Optional[str] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Crea una tarjeta con texto perfectamente centrado vertical y horizontalmente."""
        container = self.add_rect(x, y, w, h, bg=bg, stroke=stroke, stroke_w=stroke_w,
                                  stroke_style=stroke_style, roundness_type=roundness_type,
                                  frame_id=frame_id)
        
        text_id = rid()
        container["boundElements"].append({"id": text_id, "type": "text"})

        lines = str(text).split('\n')
        text_h = len(lines) * font_size * 1.35
        text_y = y + max(0.0, (h - text_h) * 0.5)

        text_elem = self._base_element("text", x, text_y, w, text_h, text_color, "transparent", frame_id=frame_id)
        text_elem["id"] = text_id
        text_elem.update({
            "fontSize": font_size,
            "fontFamily": font_family,
            "text": str(text),
            "textAlign": align,
            "verticalAlign": "middle",
            "containerId": container["id"],
            "originalText": str(text),
            "lineHeight": 1.25,
            "baseline": font_size,
            "autoResize": True
        })
        self.elements.append(text_elem)
        return container, text_elem

    def add_dual_card(self, x: float, y: float, w: float, h: float,
                      title: str, sublabel: Optional[str] = None,
                      metadata: Optional[str] = None, bg: str = "#FFFFFF",
                      stroke: str = "#0C0C0C", text_color: str = "#0C0C0C",
                      stroke_w: float = 1.5, stroke_style: str = "solid",
                      roundness_type: Optional[int] = 3, frame_id: Optional[str] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Crea una tarjeta de Doble Jerarquía con texto centrado:
        - Ajuste dinámico para impedir cualquier desbordamiento de texto.
        """
        # Calcular dimensiones seguras
        calc_w, calc_h = compute_card_dimensions(title, sublabel, metadata, font_size=13, min_w=w)
        final_w = max(w, calc_w)
        final_h = max(h, calc_h)

        container = self.add_rect(x, y, final_w, final_h, bg=bg, stroke=stroke, stroke_w=stroke_w,
                                  stroke_style=stroke_style, roundness_type=roundness_type,
                                  frame_id=frame_id)
        
        text_id = rid()
        container["boundElements"].append({"id": text_id, "type": "text"})

        if sublabel and metadata:
            full_text = f"{title}\n{sublabel} {metadata}"
        elif sublabel:
            full_text = f"{title}\n{sublabel}"
        elif metadata:
            full_text = f"{title}\n{metadata}"
        else:
            full_text = title

        lines = full_text.split('\n')
        text_h = len(lines) * 13 * 1.35
        text_y = y + max(0.0, (final_h - text_h) * 0.5)

        text_elem = self._base_element("text", x, text_y, final_w, text_h, text_color, "transparent", frame_id=frame_id)
        text_elem["id"] = text_id
        text_elem.update({
            "fontSize": 13,
            "fontFamily": 2,
            "text": full_text,
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": container["id"],
            "originalText": full_text,
            "lineHeight": 1.25,
            "baseline": 13,
            "autoResize": True
        })
        self.elements.append(text_elem)
        return container, text_elem

    def add_arrow(self, x1: float, y1: float, x2: float, y2: float,
                  stroke: str = "#64748B", stroke_w: float = 1.5,
                  dashed: bool = False, arrowhead: str = "triangle",
                  label: Optional[str] = None, orthogonal: bool = False,
                  track_y: Optional[float] = None,
                  label_pos: Optional[Tuple[float, float]] = None,
                  frame_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea una flecha con soporte ortogonal, carriles de retorno (Track Lanes)
        y Pastilla Protectora (Pill Label) libre de colisiones.
        """
        dx = x2 - x1
        dy = y2 - y1
        stroke_style = "dashed" if dashed else "solid"

        points = compute_orthogonal_arrow(x1, y1, x2, y2, track_y=track_y) if orthogonal else [[0.0, 0.0], [dx, dy]]

        elem = self._base_element("arrow", x1, y1, dx, dy, stroke, "transparent",
                                  stroke_w=stroke_w, stroke_style=stroke_style, frame_id=frame_id)
        elem.update({
            "points": points,
            "lastCommittedPoint": None,
            "startBinding": None,
            "endBinding": None,
            "startArrowhead": None,
            "endArrowhead": arrowhead
        })
        self.elements.append(elem)

        if label:
            label_len = len(str(label))
            pill_w = max(65.0, label_len * 7.5 + 16.0)
            pill_h = 24.0

            if label_pos:
                mid_x = label_pos[0] - (pill_w * 0.5)
                mid_y = label_pos[1] - (pill_h * 0.5)
            elif dx < -20 and track_y is not None:
                # Flujo de retorno por carril superior
                mid_x = x1 + dx * 0.5 - (pill_w * 0.5)
                mid_y = track_y - (pill_h * 0.5)
            elif abs(dx) < 25 and abs(dy) > 100:
                # Flecha vertical larga: colocar cerca del inicio para evitar tapar nodo intermedio
                mid_x = x1 - (pill_w * 0.5)
                mid_y = y1 + 35.0 - (pill_h * 0.5)
            elif dx > 350:
                # Flecha larga que salta scopes: colocar cerca del origen para no ensuciar el scope intermedio
                mid_x = x1 + 55.0 - (pill_w * 0.5)
                mid_y = y1 - 14.0 - (pill_h * 0.5)
            else:
                mid_x = x1 + dx * 0.5 - (pill_w * 0.5)
                mid_y = y1 + dy * 0.5 - (pill_h * 0.5)

            # Fondo protector blanco
            pill_bg = self.add_rect(mid_x, mid_y, pill_w, pill_h, bg="#FFFFFF",
                                    stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            
            # Texto centrado sobre la pastilla
            pill_text = self._base_element("text", mid_x, mid_y, pill_w, pill_h, stroke, "transparent", frame_id=frame_id)
            pill_text_id = rid()
            pill_bg["boundElements"].append({"id": pill_text_id, "type": "text"})
            pill_text["id"] = pill_text_id
            pill_text.update({
                "fontSize": 11,
                "fontFamily": 3,  # Cascadia Mono
                "text": str(label),
                "textAlign": "center",
                "verticalAlign": "middle",
                "containerId": pill_bg["id"],
                "originalText": str(label),
                "lineHeight": 1.2,
                "baseline": 11
            })
            self.elements.append(pill_text)

        return elem

    def add_line(self, x1: float, y1: float, x2: float, y2: float,
                 stroke: str = "#E2E8F0", stroke_w: float = 1.5,
                 dashed: bool = False, frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea una línea divisoria o eje continuo."""
        dx = x2 - x1
        dy = y2 - y1
        stroke_style = "dashed" if dashed else "solid"

        elem = self._base_element("line", x1, y1, dx, dy, stroke, "transparent",
                                  stroke_w=stroke_w, stroke_style=stroke_style, frame_id=frame_id)
        elem.update({
            "points": [[0.0, 0.0], [dx, dy]],
            "lastCommittedPoint": None,
            "startBinding": None,
            "endBinding": None,
            "startArrowhead": None,
            "endArrowhead": None
        })
        self.elements.append(elem)
        return elem

    def add_scope_container(self, x: float, y: float, w: float, h: float,
                            label: str, stroke: str = "#CBD5E1",
                            bg: str = "#F8FAFC", frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea un contenedor de ámbito (Scope Boundary) con etiqueta superior izquierda amplia."""
        container = self.add_rect(x, y, w, h, bg=bg, stroke=stroke, stroke_w=1.0,
                                  stroke_style="solid", roundness_type=3, frame_id=frame_id)
        # Etiqueta mono en la esquina superior izquierda sin recortes
        self.add_text(x + 16, y + 12, label.upper(), font_size=11, font_family=3,
                      color="#64748B", align="left", frame_id=frame_id)
        return container

    def add_sticky_note(self, x: float, y: float, w: float, h: float,
                        text: str, bg: str = "#FFE95C", stroke: str = "#0C0C0C",
                        text_color: str = "#0C0C0C", font_size: int = 14,
                        angle_deg: float = 1.5, frame_id: Optional[str] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Crea un post-it / sticky con micro-rotación orgánica."""
        angle_rad = angle_deg * (3.14159265 / 180.0)
        container = self.add_rect(x, y, w, h, bg=bg, stroke=stroke, stroke_w=1.0, roundness_type=None, frame_id=frame_id)
        container["angle"] = angle_rad
        
        text_id = rid()
        container["boundElements"].append({"id": text_id, "type": "text"})

        lines = str(text).split('\n')
        text_h = len(lines) * font_size * 1.35
        text_y = y + max(0.0, (h - text_h) * 0.5)

        text_elem = self._base_element("text", x, text_y, w, text_h, text_color, "transparent", frame_id=frame_id)
        text_elem["id"] = text_id
        text_elem["angle"] = angle_rad
        text_elem.update({
            "fontSize": font_size,
            "fontFamily": 2,
            "text": str(text),
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": container["id"],
            "originalText": str(text),
            "lineHeight": 1.25,
            "baseline": font_size,
            "autoResize": True
        })
        self.elements.append(text_elem)
        return container, text_elem

    def add_capture_slot(self, x: float, y: float, w: float, h: float,
                         label: str = "Captura de Pantalla / Evidencia",
                         bg: str = "#EDEDED", stroke: str = "#F05A5A",
                         frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea un slot de captura con marco rojo discontinuo estilo Miro."""
        box = self.add_rect(x, y, w, h, bg=bg, stroke=stroke, stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=frame_id)
        # Texto central
        self.add_text(x + 20, y + h * 0.5 - 10, f"📷 {label}", font_size=13, font_family=2, color="#666666", frame_id=frame_id)
        return box

    def add_banner(self, x: float, y: float, w: float, h: float, text: str,
                   bg: str = "#F5BEC0", text_color: str = "#0C0C0C", font_size: int = 16,
                   frame_id: Optional[str] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Crea un banner horizontal de cierre / punchline."""
        box = self.add_rect(x, y, w, h, bg=bg, stroke=bg, roundness_type=3, frame_id=frame_id)
        text_id = rid()
        box["boundElements"].append({"id": text_id, "type": "text"})
        
        lines = str(text).split('\n')
        text_h = len(lines) * font_size * 1.35
        text_y = y + max(0.0, (h - text_h) * 0.5)
        
        text_elem = self._base_element("text", x, text_y, w, text_h, text_color, "transparent", frame_id=frame_id)
        text_elem["id"] = text_id
        text_elem.update({
            "fontSize": font_size,
            "fontFamily": 2,
            "text": str(text),
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": box["id"],
            "originalText": str(text),
            "lineHeight": 1.25,
            "baseline": font_size,
            "autoResize": True
        })
        self.elements.append(text_elem)
        return box, text_elem

    def add_metric_pill(self, x: float, y: float, label: str, value: str,
                        bg: str = "#0C0C0C", text_color: str = "#FFFFFF",
                        frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea una pastilla de métrica compacta para cabeceras."""
        w = max(110.0, (len(label) + len(value)) * 7.5 + 30.0)
        h = 36.0
        pill = self.add_rect(x, y, w, h, bg=bg, stroke=bg, roundness_type=3, frame_id=frame_id)
        full_txt = f"{label}: {value}"
        self.add_text(x + 10, y + 9, full_txt, font_size=12, font_family=2, color=text_color, frame_id=frame_id)
        return pill

    def add_chip(self, x: float, y: float, w: float, h: float,
                 number: str, label: str, bg: str = "#0F172A",
                 text_color: str = "#FFFFFF", frame_id: Optional[str] = None):
        """Crea un chip de KPI/Dashboard con número gigante arriba y etiqueta chica abajo."""
        card = self.add_rect(x, y, w, h, bg=bg, stroke=bg, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 20, y + 15, number, font_size=38, font_family=2, color=text_color, frame_id=frame_id)
        self.add_text(x + 22, y + h - 35, label, font_size=13, font_family=2, color=text_color, frame_id=frame_id)
        return card

    def to_dict(self) -> Dict[str, Any]:
        """Genera el diccionario del archivo .excalidraw completo."""
        return {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": self.elements,
            "appState": {
                "gridSize": self.grid_size,
                "viewBackgroundColor": self.bg_color
            },
            "files": {}
        }

    def save(self, filepath: str):
        """Guarda el archivo .excalidraw en formato JSON minificado estricto."""
        data = self.to_dict()
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
