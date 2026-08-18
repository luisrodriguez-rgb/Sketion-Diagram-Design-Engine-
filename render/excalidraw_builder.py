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
from typing import List, Dict, Any, Optional, Tuple, Union
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
        self.files: Dict[str, Any] = {}

    def _base_element(self, elem_type: str, x: float, y: float, w: float, h: float,
                      stroke_color: str = "#0C0C0C", bg_color: str = "transparent",
                      stroke_width: float = 1.5, stroke_style: str = "solid",
                      frame_id: Optional[str] = None, angle: float = 0.0,
                      roundness: Optional[Dict[str, Any]] = None, opacity: int = 100,
                      stroke_w: Optional[float] = None) -> Dict[str, Any]:
        final_stroke_w = stroke_w if stroke_w is not None else stroke_width

        # Auto-conversión y protección de coordenadas relativas a frame
        if frame_id and elem_type != "frame":
            frame = next((e for e in self.elements if e.get("id") == frame_id and e.get("type") == "frame"), None)
            if frame:
                fx = float(frame.get("x", 0.0))
                fy = float(frame.get("y", 0.0))
                fw = float(frame.get("width", 1000.0))
                fh = float(frame.get("height", 800.0))

                # Si las coordenadas recibidas son relativas al marco (e.g. y < fy - 30 y dentro de fh), convertir a absolutas
                if y < fy - 30.0 and (0.0 <= y <= fh):
                    y = fy + y
                if x < fx - 30.0 and (0.0 <= x <= fw):
                    x = fx + x

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

    def auto_fit_frame(self, frame_id: str, padding: float = 40.0):
        """Ajusta automáticamente el ancho y alto del frame según sus elementos contenidos de forma ceñida."""
        frame = next((e for e in self.elements if e.get("id") == frame_id and e.get("type") == "frame"), None)
        if not frame:
            return

        children = [e for e in self.elements if e.get("frameId") == frame_id and e.get("type") != "frame"]
        if not children:
            return

        fx = frame["x"]
        fy = frame["y"]

        max_x = max((c["x"] + float(c.get("width", 0.0)) for c in children), default=fx + 600.0)
        max_y = max((c["y"] + float(c.get("height", 0.0)) for c in children), default=fy + 400.0)

        frame["width"] = max(400.0, (max_x - fx) + padding)
        frame["height"] = max(250.0, (max_y - fy) + padding)

    def auto_fit_all_frames(self, padding: float = 40.0):
        """Ajusta dinámicamente todos los frames del canvas para erradicar espacios vacíos sobrantes."""
        for f in [e for e in self.elements if e.get("type") == "frame"]:
            self.auto_fit_frame(f["id"], padding=padding)

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

    def add_stack_layer(self, x: float, y: float, w: float, h: float,
                        layer_num: str, title: str, doc_count: str,
                        documents: List[str],
                        bg: str = "#FFFFFF", stroke: str = "#CBD5E1",
                        header_bg: str = "#EFF6FF", header_stroke: str = "#93C5FD",
                        badge_bg: str = "#2563EB", badge_color: str = "#FFFFFF",
                        frame_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea una capa arquitectónica estructurada que llena el espacio de forma equilibrada:
        - Barra de cabecera con Badge de Capa + Título + Conteo de Documentos
        - Área de cuerpo con lista organizada de documentos/items
        """
        container = self.add_rect(x, y, w, h, bg=bg, stroke=stroke, stroke_w=1.5, roundness_type=3, frame_id=frame_id)

        # 1. Barra de cabecera
        head_h = 36.0
        self.add_rect(x, y, w, head_h, bg=header_bg, stroke=header_stroke, stroke_w=1.0, roundness_type=3, frame_id=frame_id)

        # Badge
        badge_w = max(55.0, len(layer_num) * 7.5 + 16.0)
        self.add_rect(x + 12.0, y + 7.0, badge_w, 22.0, bg=badge_bg, stroke=badge_bg, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 18.0, y + 10.0, layer_num, font_size=11, font_family=2, color=badge_color, frame_id=frame_id)

        # Título de Capa
        self.add_text(x + 18.0 + badge_w + 8.0, y + 9.0, title.upper(), font_size=13, font_family=2, color="#0F172A", frame_id=frame_id)

        # Conteo a la derecha
        doc_w = len(doc_count) * 7.2 + 10.0
        self.add_text(x + w - doc_w - 14.0, y + 10.0, doc_count, font_size=11, font_family=2, color="#64748B", frame_id=frame_id)

        # 2. Contenido del cuerpo (Lista formateada en 1 o 2 columnas o texto continuo balanceado)
        body_text = "  ·  ".join(documents) if isinstance(documents, list) else str(documents)
        self.add_text(x + 16.0, y + 46.0, body_text, font_size=12, font_family=2, color="#334155", frame_id=frame_id)

        return container

    def add_feature_card(self, x: float, y: float, w: float, h: float,
                         title: str, bullets: List[str],
                         badge: Optional[str] = None, icon: Optional[str] = None,
                         is_hero: bool = False, bg: str = "#FFFFFF",
                         stroke: str = "#CBD5E1", frame_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea una tarjeta de contenido densa y balanceada con título, icono y viñetas explicativas.
        """
        final_stroke = "#D93829" if is_hero else stroke
        final_bg = "#FFF5F2" if is_hero else bg
        stroke_w = 2.0 if is_hero else 1.5

        container = self.add_rect(x, y, w, h, bg=final_bg, stroke=final_stroke, stroke_w=stroke_w, roundness_type=3, frame_id=frame_id)

        # Badge
        if badge:
            b_bg = "#FEE2E2" if is_hero else "#F1F5F9"
            b_str = "#FCA5A5" if is_hero else "#CBD5E1"
            b_col = "#D93829" if is_hero else "#475569"
            bw = max(60.0, len(badge) * 7.2 + 16.0)
            self.add_rect(x + 14.0, y + 12.0, bw, 20.0, bg=b_bg, stroke=b_str, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            self.add_text(x + 18.0, y + 14.0, badge, font_size=10, font_family=2, color=b_col, frame_id=frame_id)

        # Icono
        if icon:
            self.add_icon(icon, x + w - 38.0, y + 12.0, size=22.0, color=final_stroke, frame_id=frame_id)

        # Título
        tit_y = y + 36.0 if badge else y + 16.0
        self.add_text(x + 16.0, tit_y, title, font_size=15, font_family=2, color="#0F172A", frame_id=frame_id)

        # Bullets
        bullets_y = tit_y + 24.0
        bullet_lines = "\n".join([f"• {b}" for b in bullets])
        self.add_text(x + 16.0, bullets_y, bullet_lines, font_size=12, font_family=2, color="#334155", frame_id=frame_id)

        return container

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

    def add_icon(self, icon_name: str, x: float, y: float, size: float = 24.0,
                 color: str = "#0C0C0C", frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Incrusta un icono vectorial monocromático de la biblioteca Tabler/SimpleIcons."""
        from .icons import get_icon_data_url
        file_id, data_url = get_icon_data_url(icon_name, color=color)
        
        # Registrar archivo en el diccionario global files de la escena
        if file_id not in self.files:
            self.files[file_id] = {
                "mimeType": "image/svg+xml",
                "id": file_id,
                "dataURL": data_url,
                "created": 1723766400000
            }
            
        elem = self._base_element("image", x, y, size, size, stroke_color="transparent",
                                  bg_color="transparent", frame_id=frame_id)
        elem.update({
            "fileId": file_id,
            "status": "saved",
            "scale": [1.0, 1.0]
        })
        self.elements.append(elem)
        return elem

    def add_diamond(self, x: float, y: float, w: float, h: float,
                    bg: str = "#FFFFFF", stroke: str = "#0F172A",
                    stroke_w: float = 1.5, frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea un nodo con forma de rombo para decisiones y bifurcaciones condicionales."""
        elem = self._base_element("diamond", x, y, w, h, stroke, bg, stroke_w=stroke_w, frame_id=frame_id)
        self.elements.append(elem)
        return elem

    def add_card_with_icon(self, x: float, y: float, w: float, h: float,
                           title: str, sublabel: Optional[str] = None,
                           icon: str = "server", bg: str = "#FFFFFF",
                           stroke: str = "#0C0C0C", text_color: str = "#0C0C0C",
                           frame_id: Optional[str] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Crea una tarjeta con icono en la esquina superior izquierda o junto al título."""
        container, text_elem = self.add_dual_card(x, y, w, h, title, sublabel=sublabel,
                                                  bg=bg, stroke=stroke, text_color=text_color,
                                                  frame_id=frame_id)
        # Añadir icono en x + 16, y + 16
        self.add_icon(icon, x + 16.0, y + 16.0, size=24.0, color=stroke, frame_id=frame_id)
        return container, text_elem

    def add_quad_card(self, x: float, y: float, w: float, h: float,
                      title: str, sublabel: Optional[str] = None,
                      badge: Optional[str] = "EXT",
                      icon: Optional[str] = None,
                      pills: Optional[List[str]] = None,
                      bg: str = "#FFFFFF", stroke: str = "#0C0C0C",
                      text_color: str = "#0F172A", font_size: Optional[int] = None,
                      is_hero: bool = False,
                      frame_id: Optional[str] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Crea la Tarjeta Editorial con Zonas de Disposición Vertical Estrictas:
        - Zona de Cabecera (Y+10 a Y+32): Badge a la izquierda + Icono a la derecha.
        - Zona de Título (Y+38): Título bold limpio sin colisión de badge.
        - Zona de Subtítulo (Y+62+): Subtítulo explicativo en 12px apilado con holgura.
        """
        card_bg = "#FFF5F2" if is_hero else bg
        card_stroke = "#D93829" if is_hero else stroke
        card_stroke_w = 2.0 if is_hero else 1.5
        
        container = self.add_rect(x, y, w, h, bg=card_bg, stroke=card_stroke,
                                  stroke_w=card_stroke_w, roundness_type=3, frame_id=frame_id)
        
        # 1. Top-Left Badge
        if badge:
            badge_font = 10
            bw = max(45.0, len(badge) * 7.2 + 16.0)
            badge_bg = "#FEE2E2" if is_hero else "#F1F5F9"
            badge_stroke = "#FCA5A5" if is_hero else "#CBD5E1"
            badge_text_col = "#D93829" if is_hero else "#475569"
            self.add_rect(x + 12.0, y + 10.0, bw, 20.0, bg=badge_bg, stroke=badge_stroke,
                          stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            self.add_text(x + 16.0, y + 12.0, badge,
                          font_size=badge_font, font_family=2, color=badge_text_col, frame_id=frame_id)

        # 2. Top-Right Icon
        if icon:
            icon_size = 22.0
            icon_col = "#D93829" if is_hero else card_stroke
            self.add_icon(icon, x + w - icon_size - 14.0, y + 10.0, size=icon_size, color=icon_col, frame_id=frame_id)

        # 3. Zonas de Contenido Vertical Estricto (Sin Montajes)
        tit_fs = font_size if font_size is not None else (14 if w < 320.0 else 15)
        body_y = y + 38.0 if (badge or icon) else y + 16.0

        # Título
        title_elem = self.add_text(x + 14.0, body_y, title, font_size=tit_fs, font_family=2, color=text_color, frame_id=frame_id)

        # Subtítulo (Calculado debajo del título con holgura segura)
        if sublabel:
            tit_lines = title.split('\n')
            tit_h = len(tit_lines) * tit_fs * 1.35
            sub_y = body_y + tit_h + 4.0
            self.add_text(x + 14.0, sub_y, sublabel, font_size=12, font_family=2, color="#475569", frame_id=frame_id)

        # 4. Bottom Data Pills (Optional)
        if pills:
            if len(pills) >= 1:
                p1 = pills[0]
                pw1 = max(30.0, len(p1) * 7.5 + 12.0)
                self.add_rect(x + 14.0, y + h - 24.0, pw1, 16.0, bg="#E2E8F0", stroke="#94A3B8", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
                self.add_text(x + 18.0, y + h - 23.0, p1, font_size=10, font_family=2, color="#334155", frame_id=frame_id)
            if len(pills) >= 2:
                p2 = pills[1]
                pw2 = max(30.0, len(p2) * 7.5 + 12.0)
                self.add_rect(x + w - pw2 - 14.0, y + h - 24.0, pw2, 16.0, bg="#E2E8F0", stroke="#94A3B8", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
                self.add_text(x + w - pw2 - 10.0, y + h - 23.0, p2, font_size=10, font_family=2, color="#334155", frame_id=frame_id)

        return container, title_elem

    def add_chevron_ribbon(self, x: float, y: float, w: float, h: float = 38.0,
                           stages: Optional[List[str]] = None,
                           bg: str = "#1E293B", text_color: str = "#FFFFFF",
                           frame_id: Optional[str] = None):
        """Crea la cinta superior de chevrons concatenados de macro-pipeline."""
        if not stages:
            stages = ["DATA SOURCES", "INGESTION", "STORAGE", "TRANSFORM", "VISUALIZATION"]
            
        stage_count = len(stages)
        stage_w = (w - (stage_count - 1) * 8.0) / stage_count
        
        for i, sname in enumerate(stages):
            sx = x + i * (stage_w + 8.0)
            self.add_rect(sx, y, stage_w, h, bg=bg, stroke=bg, roundness_type=3, frame_id=frame_id)
            self.add_text(sx + (stage_w - len(sname) * 7.5) * 0.5, y + 10.0, sname.upper(),
                          font_size=11, font_family=2, color=text_color, frame_id=frame_id)

    def add_vertical_rails(self, x: float, y: float, w: float, h: float,
                           rails: Optional[List[Dict[str, Any]]] = None,
                           frame_id: Optional[str] = None):
        """Crea los rieles laterales verticales para aspectos transversales (Orquestación, Seguridad, Observabilidad)."""
        if not rails:
            rails = [
                {"title": "ORCHESTRATION", "bg": "#1E293B", "text_color": "#FFFFFF"},
                {"title": "SECURITY", "bg": "#E03A2F", "text_color": "#FFFFFF"},
                {"title": "OBSERVABILITY", "bg": "#1E293B", "text_color": "#FFFFFF"}
            ]
            
        rail_count = len(rails)
        rail_h = (h - (rail_count - 1) * 10.0) / rail_count
        
        for i, r in enumerate(rails):
            ry = y + i * (rail_h + 10.0)
            rbg = r.get("bg", "#1E293B")
            rtxt = r.get("title", "")
            rcol = r.get("text_color", "#FFFFFF")
            
            self.add_rect(x, ry, w, rail_h, bg=rbg, stroke=rbg, roundness_type=3, frame_id=frame_id)
            
            # Texto apilado verticalmente o compacto
            stacked = "\n".join(list(rtxt))
            self.add_text(x + (w - 14.0) * 0.5, ry + 15.0, stacked,
                          font_size=10, font_family=2, color=rcol, frame_id=frame_id)

    def add_step_badge_axis(self, x: float, y: float, total_w: float,
                            steps: List[str], hero_idx: int = -1,
                            frame_id: Optional[str] = None):
        """Crea el eje superior de pasos con insignias circulares numeradas."""
        step_count = len(steps)
        spacing = total_w / max(1, step_count - 1)
        
        for i, stxt in enumerate(steps):
            cx = x + i * spacing
            is_hero = (i == hero_idx)
            
            bg = "#E03A2F" if is_hero else "#FFFFFF"
            stroke = "#E03A2F" if is_hero else "#94A3B8"
            tcol = "#FFFFFF" if is_hero else "#475569"
            
            # Círculo numerado
            self.add_ellipse(cx - 12.0, y, 24.0, 24.0, bg=bg, stroke=stroke, stroke_w=1.5, frame_id=frame_id)
            is_first = (i == 0)
            is_last = (i == stage_count - 1)
            self.add_rect(sx, y, stage_w, h, bg=bg, stroke="#334155", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            lbl_w = len(sname) * 7.5
            self.add_text(sx + (stage_w - lbl_w) * 0.5, y + (h - 14.0) * 0.5, sname,
                          font_size=12, font_family=2, color=text_color, frame_id=frame_id)

    def add_database_cylinder(self, x: float, y: float, w: float, h: float,
                              title: str, sublabel: Optional[str] = None,
                              badge: str = "DATABASE", is_hero: bool = False,
                              bg: str = "#EFF6FF", stroke: str = "#2563EB",
                              frame_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea una primitiva morfológica de Cilindro / Base de Datos con tapa elíptica proporcionada y disco inferior.
        """
        final_stroke = "#D93829" if is_hero else stroke
        final_bg = "#FFF5F2" if is_hero else bg
        stroke_w = 2.0 if is_hero else 1.5
        effective_h = max(h, 105.0)
        cap_h = min(20.0, max(12.0, effective_h * 0.14))

        # 1. Cuerpo del cilindro
        container = self.add_rect(x, y + cap_h * 0.5, w, effective_h - cap_h * 0.5, bg=final_bg, stroke=final_stroke, stroke_w=stroke_w, roundness_type=3, frame_id=frame_id)

        # 2. Tapa elíptica superior
        self.add_ellipse(x, y, w, cap_h, bg=final_bg, stroke=final_stroke, stroke_w=stroke_w, frame_id=frame_id)

        # 3. Badge & Icono en cabecera
        bw = max(55.0, len(badge) * 7.0 + 14.0)
        b_bg = "#FEE2E2" if is_hero else "#DBEAFE"
        b_str = "#FCA5A5" if is_hero else "#93C5FD"
        b_col = "#D93829" if is_hero else "#1D4ED8"
        self.add_rect(x + 14.0, y + cap_h + 8.0, bw, 18.0, bg=b_bg, stroke=b_str, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 18.0, y + cap_h + 10.0, badge, font_size=9, font_family=2, color=b_col, frame_id=frame_id)
        self.add_icon("database", x + w - 30.0, y + cap_h + 8.0, size=18.0, color=final_stroke, frame_id=frame_id)

        # 4. Título y Subtítulo en zona central despejada
        self.add_text(x + 14.0, y + cap_h + 32.0, title, font_size=13, font_family=2, color="#0F172A", frame_id=frame_id)
        if sublabel:
            self.add_text(x + 14.0, y + cap_h + 52.0, sublabel, font_size=10, font_family=1, color="#475569", frame_id=frame_id)

        return container

    def add_streaming_pipe(self, x: float, y: float, w: float, h: float,
                           title: str, topics: List[str],
                           badge: str = "STREAMING", is_hero: bool = False,
                           bg: str = "#EEF2FF", stroke: str = "#4F46E5",
                           frame_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea una primitiva morfológica de Tubería / Cola / Bus de Eventos segmentado (Kafka/RabbitMQ/Flink).
        """
        final_stroke = "#D93829" if is_hero else stroke
        final_bg = "#FFF5F2" if is_hero else bg

        # Contenedor cápsula
        container = self.add_rect(x, y, w, h, bg=final_bg, stroke=final_stroke, stroke_w=1.8, roundness_type=3, frame_id=frame_id)

        # Cabecera de Stream
        bw = max(70.0, len(badge) * 7.2 + 16.0)
        self.add_rect(x + 12.0, y + 10.0, bw, 20.0, bg="#E0E7FF", stroke="#C7D2FE", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 16.0, y + 12.0, badge, font_size=10, font_family=2, color="#3730A3", frame_id=frame_id)
        self.add_text(x + 16.0 + bw + 10.0, y + 12.0, title.upper(), font_size=12, font_family=2, color="#0F172A", frame_id=frame_id)
        self.add_icon("terminal", x + w - 34.0, y + 10.0, size=18.0, color=final_stroke, frame_id=frame_id)

        # Slots de partición horizontal
        slot_cnt = len(topics)
        slot_w = (w - 30.0 - (slot_cnt - 1) * 8.0) / max(1, slot_cnt)
        for i, top in enumerate(topics):
            sx = x + 15.0 + i * (slot_w + 8.0)
            sy = y + 38.0
            sh = h - 48.0
            self.add_rect(sx, sy, slot_w, sh, bg="#FFFFFF", stroke=final_stroke, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            self.add_text(sx + 8.0, sy + (sh * 0.5) - 7.0, f"▸ {top}", font_size=11, font_family=3, color="#1E293B", frame_id=frame_id)

        return container

    def add_security_barrier(self, x: float, y: float, w: float, h: float,
                             title: str, rules: List[str],
                             badge: str = "WAF / FIREWALL",
                             frame_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea una barrera perimetral de seguridad Zero-Trust con franja de almenas.
        """
        container = self.add_rect(x, y, w, h, bg="#F8FAFC", stroke="#64748B", stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=frame_id)
        
        # Barra superior con escudo
        self.add_rect(x, y, w, 32.0, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_icon("shield", x + 12.0, y + 6.0, size=20.0, color="#0F172A", frame_id=frame_id)
        self.add_text(x + 38.0, y + 8.0, f"{title.upper()} ({badge})", font_size=12, font_family=2, color="#0F172A", frame_id=frame_id)

        # Reglas
        for r_i, rule in enumerate(rules):
            self.add_text(x + 16.0, y + 42.0 + r_i * 22.0, f"• {rule}", font_size=11, font_family=2, color="#334155", frame_id=frame_id)

        return container

    def add_actor_node(self, x: float, y: float, w: float, h: float,
                       name: str, role: str, icon: str = "user",
                       is_hero: bool = False, frame_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea un nodo de Actor / Usuario en pastilla compacta con avatar integrado.
        """
        final_bg = "#FFF5F2" if is_hero else "#FFFFFF"
        final_stroke = "#D93829" if is_hero else "#94A3B8"

        container = self.add_rect(x, y, w, h, bg=final_bg, stroke=final_stroke, stroke_w=1.5, roundness_type=3, frame_id=frame_id)

        # Avatar circular
        self.add_ellipse(x + 12.0, y + 10.0, 36.0, 36.0, bg="#F1F5F9", stroke=final_stroke, stroke_w=1.2, frame_id=frame_id)
        self.add_icon(icon, x + 20.0, y + 18.0, size=20.0, color=final_stroke, frame_id=frame_id)

        # Texto
        self.add_text(x + 58.0, y + 12.0, name, font_size=14, font_family=2, color="#0F172A", frame_id=frame_id)
        self.add_text(x + 58.0, y + 30.0, role.upper(), font_size=10, font_family=3, color="#64748B", frame_id=frame_id)

        return container

    def add_radial_cluster(self, cx: float, cy: float, radius: float,
                           hub_title: str, satellites: List[Dict[str, Any]],
                           badge: str = "CORE HUB", is_hero: bool = True,
                           frame_id: Optional[str] = None):
        """
        Genera una topología radial real (Arquetipo A / El Cerebro) con Hub central y satélites orbitando.
        """
        # 1. Hub Central
        hw, hh = 240.0, 110.0
        hx = cx - (hw * 0.5)
        hy = cy - (hh * 0.5)
        hub_elem = self.add_quad_card(hx, hy, hw, hh, hub_title, sublabel="Núcleo Central", badge=badge, is_hero=is_hero, font_size=15, frame_id=frame_id)

        # 2. Satélites orbitando
        sat_count = len(satellites)
        if sat_count == 0:
            return

        angle_step = (2 * math.pi) / sat_count
        for i, sat in enumerate(satellites):
            angle = i * angle_step - (math.pi / 2.0)
            sx = cx + radius * math.cos(angle)
            sy = cy + radius * math.sin(angle)
            sw, sh = 200.0, 85.0
            spx = sx - (sw * 0.5)
            spy = sy - (sh * 0.5)

            # Tarjeta de satélite
            s_tit = sat.get("title", f"Satellite {i+1}")
            s_sub = sat.get("sublabel", "")
            s_badge = sat.get("badge", f"SAT {i+1}")
            s_icon = sat.get("icon", "server")
            self.add_quad_card(spx, spy, sw, sh, s_tit, sublabel=s_sub, badge=s_badge, icon=s_icon, font_size=13, frame_id=frame_id)

            # Flecha radial bidireccional / ortogonal
            self.add_arrow(cx + (hw * 0.5 * math.cos(angle)),
                           cy + (hh * 0.5 * math.sin(angle)),
                           spx + (sw * 0.5) - (sw * 0.5 * math.cos(angle)),
                           spy + (sh * 0.5) - (sh * 0.5 * math.sin(angle)),
                           stroke="#94A3B8", stroke_w=1.2, dashed=True, frame_id=frame_id)

    def add_split_duel(self, x: float, y: float, w: float, h: float,
                       left_title: str, left_items: List[str],
                       right_title: str, right_items: List[str],
                       left_label: str = "ANTES (LEGACY)", right_label: str = "DESPUÉS (TARGET)",
                       frame_id: Optional[str] = None):
        """
        Genera un Duelo Comparativo (Arquetipo D / El Duelo VS) con paneles contrastados.
        """
        col_w = (w - 40.0) * 0.5

        # Columna Izquierda (Legacy / Fricción)
        self.add_rect(x, y, col_w, h, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=frame_id)
        self.add_rect(x, y, col_w, 36.0, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 16.0, y + 10.0, f"[LEGACY] {left_label.upper()} — {left_title}", font_size=13, font_family=2, color="#991B1B", frame_id=frame_id)
        for i, item in enumerate(left_items):
            self.add_text(x + 16.0, y + 52.0 + i * 26.0, f"[-] {item}", font_size=12, font_family=2, color="#475569", frame_id=frame_id)

        # Columna Derecha (Target / Solución Hero)
        rx = x + col_w + 40.0
        self.add_rect(rx, y, col_w, h, bg="#F0FDF4", stroke="#86EFAC", stroke_w=2.0, roundness_type=3, frame_id=frame_id)
        self.add_rect(rx, y, col_w, 36.0, bg="#DCFCE7", stroke="#86EFAC", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(rx + 16.0, y + 10.0, f"[TARGET] {right_label.upper()} — {right_title}", font_size=13, font_family=2, color="#166534", frame_id=frame_id)
        for j, ritem in enumerate(right_items):
            self.add_text(rx + 16.0, y + 52.0 + j * 26.0, f"[+] {ritem}", font_size=12, font_family=2, color="#15803D", frame_id=frame_id)

        # Conector central VS
        self.add_ellipse(x + col_w + 5.0, y + (h * 0.5) - 15.0, 30.0, 30.0, bg="#0F172A", stroke="#0F172A", stroke_w=1.0, frame_id=frame_id)
        self.add_text(x + col_w + 12.0, y + (h * 0.5) - 7.0, "VS", font_size=10, font_family=3, color="#FFFFFF", frame_id=frame_id)

    def add_code_block(self, x: float, y: float, w: float, h: float,
                       title: str, code_lines: Union[List[str], str],
                       lang: str = "PYTHON", is_dark: bool = True,
                       frame_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Crea un bloque de código / terminal interactivo con barra de título, controles de ventana y sintaxis legible.
        """
        bg_color = "#0F172A" if is_dark else "#F8FAFC"
        stroke_color = "#334155" if is_dark else "#CBD5E1"
        header_bg = "#1E293B" if is_dark else "#F1F5F9"
        text_color = "#38BDF8" if is_dark else "#0F172A"
        code_color = "#E2E8F0" if is_dark else "#1E293B"

        container = self.add_rect(x, y, w, h, bg=bg_color, stroke=stroke_color, stroke_w=1.2, roundness_type=3, frame_id=frame_id)
        
        # Barra superior de terminal
        head_h = 28.0
        self.add_rect(x, y, w, head_h, bg=header_bg, stroke=stroke_color, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        
        # 3 botones de ventana (macOS dots)
        dots = [("#EF4444", 12.0), ("#F59E0B", 24.0), ("#10B981", 36.0)]
        for dot_col, dot_x in dots:
            self.add_ellipse(x + dot_x, y + 9.0, 8.0, 8.0, bg=dot_col, stroke=dot_col, stroke_w=1.0, frame_id=frame_id)
            
        # Título y Lenguaje
        self.add_text(x + 54.0, y + 7.0, title, font_size=10, font_family=3, color=text_color, frame_id=frame_id)
        self.add_text(x + w - len(lang) * 7.0 - 16.0, y + 7.0, lang.upper(), font_size=9, font_family=3, color="#64748B", frame_id=frame_id)
        
        # Código interno con formato
        code_text = "\n".join(code_lines) if isinstance(code_lines, list) else str(code_lines)
        self.add_text(x + 14.0, y + 36.0, code_text, font_size=9, font_family=3, color=code_color, frame_id=frame_id)
        return container

    def add_uml_class(self, x: float, y: float, w: float, h: float,
                      class_name: str, stereotype: str = "",
                      attributes: Optional[List[str]] = None,
                      methods: Optional[List[str]] = None,
                      is_hero: bool = False,
                      frame_id: Optional[str] = None):
        """Crea una clase UML completa con 3 compartimentos (Nombre, Atributos, Métodos)."""
        final_bg = "#FFF5F2" if is_hero else "#FFFFFF"
        final_stroke = "#D93829" if is_hero else "#0F172A"
        
        # Contenedor principal
        self.add_rect(x, y, w, h, bg=final_bg, stroke=final_stroke, stroke_w=1.8 if is_hero else 1.5, roundness_type=3, frame_id=frame_id)
        
        # Cabecera
        header_h = 38.0 if stereotype else 28.0
        self.add_rect(x, y, w, header_h, bg="#F1F5F9" if not is_hero else "#FFE4E1", stroke=final_stroke, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        if stereotype:
            self.add_text(x + 10.0, y + 4.0, f"<<{stereotype}>>", font_size=9, font_family=3, color="#64748B", frame_id=frame_id)
            self.add_text(x + 10.0, y + 18.0, class_name, font_size=12, font_family=3, color="#0F172A", frame_id=frame_id)
        else:
            self.add_text(x + 10.0, y + 6.0, class_name, font_size=12, font_family=3, color="#0F172A", frame_id=frame_id)
            
        cur_y = y + header_h + 8.0
        # Atributos
        if attributes:
            for attr in attributes:
                self.add_text(x + 12.0, cur_y, f"+ {attr}", font_size=10, font_family=3, color="#334155", frame_id=frame_id)
                cur_y += 18.0
        
        # Separador
        self.add_line(x, cur_y + 4.0, x + w, cur_y + 4.0, stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id)
        cur_y += 12.0
        
        # Métodos
        if methods:
            for meth in methods:
                self.add_text(x + 12.0, cur_y, f"+ {meth}()", font_size=10, font_family=3, color="#0F172A", frame_id=frame_id)
                cur_y += 18.0

    def add_k8s_node(self, x: float, y: float, w: float, h: float,
                     node_name: str, role: str = "Worker Node",
                     pods: Optional[List[Dict[str, str]]] = None,
                     is_hero: bool = False, frame_id: Optional[str] = None):
        """Crea un nodo de Kubernetes con Kubelet, Kube-Proxy y cápsulas Pod encapsuladas."""
        final_bg = "#F8FAFC" if not is_hero else "#FFF5F2"
        final_stroke = "#0284C7" if not is_hero else "#D93829"
        
        self.add_rect(x, y, w, h, bg=final_bg, stroke=final_stroke, stroke_w=1.8, stroke_style="dashed", roundness_type=3, frame_id=frame_id)
        self.add_rect(x, y, w, 32.0, bg="#E0F2FE" if not is_hero else "#FFE4E1", stroke=final_stroke, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 12.0, y + 8.0, f"NODE: {node_name.upper()} ({role.upper()})", font_size=11, font_family=3, color="#0369A1" if not is_hero else "#D93829", frame_id=frame_id)
        
        # Kubelet & Proxy
        self.add_rect(x + 12.0, y + 42.0, (w - 32.0) * 0.48, 26.0, bg="#FFFFFF", stroke="#94A3B8", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 18.0, y + 48.0, "kubelet (Agent)", font_size=9, font_family=3, color="#475569", frame_id=frame_id)
        
        self.add_rect(x + 16.0 + (w - 32.0) * 0.48, y + 42.0, (w - 32.0) * 0.48, 26.0, bg="#FFFFFF", stroke="#94A3B8", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 22.0 + (w - 32.0) * 0.48, y + 48.0, "kube-proxy (IPVS)", font_size=9, font_family=3, color="#475569", frame_id=frame_id)
        
        # Pods
        if pods:
            pod_w = (w - 32.0) / len(pods) - 8.0
            for p_idx, pod in enumerate(pods):
                px = x + 12.0 + p_idx * (pod_w + 8.0)
                py = y + 78.0
                ph = h - 90.0
                p_name = pod if isinstance(pod, str) else pod.get('name', 'app')
                p_img = "v1.28" if isinstance(pod, str) else pod.get('image', 'v1')
                p_status = "Running" if isinstance(pod, str) else pod.get('status', 'Running')
                self.add_rect(px, py, pod_w, ph, bg="#FFFFFF", stroke="#0284C7", stroke_w=1.2, roundness_type=3, frame_id=frame_id)
                self.add_text(px + 8.0, py + 8.0, f"POD: {p_name}", font_size=10, font_family=3, color="#0284C7", frame_id=frame_id)
                self.add_text(px + 8.0, py + 26.0, f"Image: {p_img}\nStatus: {p_status}", font_size=9, font_family=3, color="#64748B", frame_id=frame_id)

    def add_cornell_notes(self, x: float, y: float, w: float, h: float,
                          topic: str, cues: List[str], notes: List[str], summary: str,
                          frame_id: Optional[str] = None):
        """Crea una estructura de apuntes Cornell profesional (Cues 30%, Notes 70%, Summary inferior)."""
        self.add_rect(x, y, w, h, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.8, roundness_type=3, frame_id=frame_id)
        
        # Header
        self.add_rect(x, y, w, 40.0, bg="#FFF5F2", stroke="#D93829", stroke_w=1.2, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 16.0, y + 12.0, f"APUNTES CORNELL: {topic.upper()}", font_size=12, font_family=3, color="#D93829", frame_id=frame_id)
        
        body_h = h - 130.0
        cue_w = w * 0.28
        note_w = w - cue_w - 20.0
        
        # Cue Column (Preguntas / Ideas Clave)
        self.add_rect(x + 10.0, y + 50.0, cue_w, body_h, bg="#F8FAFC", stroke="#E2E8F0", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 18.0, y + 58.0, "IDEAS CLAVE & CUES", font_size=10, font_family=3, color="#64748B", frame_id=frame_id)
        for i, cue in enumerate(cues):
            self.add_text(x + 18.0, y + 84.0 + i * 26.0, f"* {cue}", font_size=10, font_family=3, color="#0F172A", frame_id=frame_id)
            
        # Notes Column (Notas de Clase)
        self.add_rect(x + cue_w + 16.0, y + 50.0, note_w, body_h, bg="#FFFFFF", stroke="#E2E8F0", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        self.add_text(x + cue_w + 24.0, y + 58.0, "NOTAS DETALLADAS & EJEMPLOS", font_size=10, font_family=3, color="#64748B", frame_id=frame_id)
        for j, note in enumerate(notes):
            self.add_text(x + cue_w + 24.0, y + 84.0 + j * 24.0, f"- {note}", font_size=10, font_family=3, color="#334155", frame_id=frame_id)
            
    def add_a3_report(self, x: float, y: float, w: float, h: float,
                      title: str, sections: Optional[List[Dict[str, Any]]] = None, frame_id: Optional[str] = None):
        """Crea una estructura de reporte ejecutivo Toyota A3 de 7 bloques asimétricos."""
        self.add_rect(x, y, w, h, bg="#FFFFFF", stroke="#0F172A", stroke_w=2.0, roundness_type=3, frame_id=frame_id)
        
        # Título
        self.add_rect(x, y, w, 36.0, bg="#FFF5F2", stroke="#D93829", stroke_w=1.2, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 16.0, y + 10.0, f"TOYOTA A3 PROBLEM SOLVING REPORT: {title.upper()}", font_size=12, font_family=3, color="#D93829", frame_id=frame_id)
        
        col_w = (w - 30.0) * 0.5
        top_h = (h - 60.0) * 0.48
        bot_h = (h - 60.0) * 0.48
        
        # Columna Izquierda: 1. Background / 2. Current State / 3. Target State
        self.add_rect(x + 10.0, y + 46.0, col_w, top_h, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 18.0, y + 54.0, "1. CONTEXTO & ESTADO ACTUAL", font_size=11, font_family=3, color="#0F172A", frame_id=frame_id)
        self.add_text(x + 18.0, y + 78.0, "• Identificación de pérdidas de tiempo y fricción.\n• Diagrama de flujo actual del proceso.\n• Cuantificación del problema en horas/semana.", font_size=10, font_family=3, color="#475569", frame_id=frame_id)
        
        self.add_rect(x + 10.0, y + 56.0 + top_h, col_w, bot_h, bg="#FFF5F2", stroke="#D93829", stroke_w=1.5, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 18.0, y + 64.0 + top_h, "2. ANÁLISIS DE CAUSA RAÍZ (5 PORQUÉS)", font_size=11, font_family=3, color="#D93829", frame_id=frame_id)
        self.add_text(x + 18.0, y + 88.0 + top_h, "1. ¿Por qué se retrasa? -> Alineación manual lenta.\n2. ¿Por qué manual? -> Sin arquetipos automáticos.\n3. ¿Por qué? -> Causa raíz: Falta de generadores modulares.", font_size=10, font_family=3, color="#334155", frame_id=frame_id)
        
        # Columna Derecha: 4. Contramedidas / 5. Plan de Acción / 6. Seguimiento
        rx = x + 20.0 + col_w
        self.add_rect(rx, y + 46.0, col_w, top_h, bg="#F0FDF4", stroke="#86EFAC", stroke_w=1.5, roundness_type=3, frame_id=frame_id)
        self.add_text(rx + 18.0, y + 54.0, "3. CONTRAMEDIDAS PROPUESTAS", font_size=11, font_family=3, color="#166534", frame_id=frame_id)
        self.add_text(rx + 18.0, y + 78.0, "[+] Constructor de 150 plantillas ricas especializadas.\n[+] Eliminación del 100% de placeholders genéricos.\n[+] Auditoría continua de consistencia visual VCS >= 99.", font_size=10, font_family=3, color="#15803D", frame_id=frame_id)
        
        self.add_rect(rx, y + 56.0 + top_h, col_w, bot_h, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=frame_id)
        self.add_text(rx + 18.0, y + 64.0 + top_h, "4. PLAN DE EJECUCIÓN & SEGUIMIENTO (PDCA)", font_size=11, font_family=3, color="#0F172A", frame_id=frame_id)
        self.add_text(rx + 18.0, y + 88.0 + top_h, "• Semana 1: Regenerar las 150 plantillas con datos reales.\n• Semana 2: Validación cruzada de SVG y Excalidraw.\n• Métricas: VCS > 99.0 | 0 Emojis | 100% Diversidad.", font_size=10, font_family=3, color="#475569", frame_id=frame_id)

    def add_kanban_board(self, x: float, y: float, w: float, h: float,
                         board_title: str, columns: List[Dict[str, Any]], frame_id: Optional[str] = None):
        """Crea un tablero Kanban ágil multicolumna con tarjetas estructuradas."""
        col_count = max(1, len(columns))
        col_w = (w - (col_count - 1) * 15.0) / col_count
        
        for i, col in enumerate(columns):
            cx = x + i * (col_w + 15.0)
            is_hero_col = col.get("is_hero", False)
            col_bg = "#FFF5F2" if is_hero_col else "#F8FAFC"
            col_stroke = "#D93829" if is_hero_col else "#CBD5E1"
            
            # Contenedor columna
            self.add_rect(cx, y, col_w, h, bg=col_bg, stroke=col_stroke, stroke_w=1.5, roundness_type=3, frame_id=frame_id)
            
            # Cabecera columna
            self.add_rect(cx, y, col_w, 36.0, bg="#FFFFFF", stroke=col_stroke, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            self.add_text(cx + 12.0, y + 10.0, f"{col.get('title', 'Column').upper()} ({len(col.get('cards', []))})", font_size=11, font_family=3, color="#D93829" if is_hero_col else "#0F172A", frame_id=frame_id)
            
            # Tarjetas
            card_y = y + 46.0
            for card in col.get("cards", []):
                self.add_rect(cx + 8.0, card_y, col_w - 16.0, 75.0, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=frame_id)
                self.add_text(cx + 16.0, card_y + 8.0, card.get("title", "Task"), font_size=11, font_family=3, color="#0F172A", frame_id=frame_id)
                self.add_text(cx + 16.0, card_y + 26.0, card.get("desc", ""), font_size=9, font_family=3, color="#64748B", frame_id=frame_id)
                
                tag = card.get("tag", "P1")
                self.add_rect(cx + col_w - 65.0, card_y + 48.0, 48.0, 18.0, bg="#FFF5F2" if tag in ["P0", "P1", "BUG"] else "#F1F5F9", stroke="#D93829" if tag in ["P0", "P1", "BUG"] else "#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
                self.add_text(cx + col_w - 55.0, card_y + 52.0, tag, font_size=8, font_family=3, color="#D93829" if tag in ["P0", "P1", "BUG"] else "#475569", frame_id=frame_id)
                
                card_y += 85.0

    def add_legend_footer(self, x: float, y: float, w: float,
                          swatches: Optional[List[Dict[str, Any]]] = None,
                          note: Optional[str] = None,
                          frame_id: Optional[str] = None):
        """Crea el bloque inferior de leyenda estructurada y filosofía editorial con envoltura segura."""
        self.add_text(x, y, "LEGEND", font_size=11, font_family=2, color="#64748B", frame_id=frame_id)
        
        cur_x = x + 70.0
        if swatches:
            for sw in swatches:
                label = sw.get("label", "")
                bg = sw.get("bg", "#FFFFFF")
                stroke = sw.get("stroke", "#0C0C0C")
                is_dashed = sw.get("dashed", False)
                is_arrow = sw.get("is_arrow", False)
                
                if is_arrow:
                    self.add_line(cur_x, y + 8.0, cur_x + 30.0, y + 8.0, stroke=stroke, stroke_w=1.5, dashed=is_dashed, frame_id=frame_id)
                    cur_x += 38.0
                else:
                    self.add_rect(cur_x, y, 24.0, 14.0, bg=bg, stroke=stroke, stroke_w=1.5, roundness_type=3, frame_id=frame_id)
                    cur_x += 30.0
                    
                self.add_text(cur_x, y + 1.0, label, font_size=11, font_family=2, color="#334155", frame_id=frame_id)
                cur_x += len(label) * 7.5 + 25.0
                
        if note:
            note_lines = note.split("\n")
            note_w = max((len(l) for l in note_lines), default=4) * (11 * 0.80) + 35.0
            # Si no cabe a la derecha de los swatches, ubicarlo en la siguiente línea
            if cur_x + note_w > x + w - 20.0:
                self.add_text(x, y + 24.0, note, font_size=11, font_family=2, color="#64748B", frame_id=frame_id)
            else:
                self.add_text(x + w - note_w, y + 1.0, note, font_size=11, font_family=2, color="#64748B", frame_id=frame_id)

    def add_radar_chart(self, cx: float, cy: float, rad: float,
                        axes: List[str], scores: List[float],
                        title: str = "RADAR EVALUATION",
                        frame_id: Optional[str] = None):
        """Crea un gráfico de radar polar profesional con círculos concéntricos y polígono de datos."""
        import math
        n = len(axes)
        if n < 3:
            return
            
        # Concéntricos
        for r_fac in [0.33, 0.66, 1.0]:
            p_rad = rad * r_fac
            for i in range(n):
                a1 = (i * 2 * math.pi / n) - (math.pi / 2)
                a2 = ((i + 1) * 2 * math.pi / n) - (math.pi / 2)
                x1, y1 = cx + p_rad * math.cos(a1), cy + p_rad * math.sin(a1)
                x2, y2 = cx + p_rad * math.cos(a2), cy + p_rad * math.sin(a2)
                self.add_line(x1, y1, x2, y2, stroke="#CBD5E1", stroke_w=1.0, dashed=True, frame_id=frame_id)
                
        # Ejes radiales
        for i, ax_name in enumerate(axes):
            angle = (i * 2 * math.pi / n) - (math.pi / 2)
            sx = cx + rad * math.cos(angle)
            sy = cy + rad * math.sin(angle)
            self.add_line(cx, cy, sx, sy, stroke="#94A3B8", stroke_w=1.2, frame_id=frame_id)
            lx = cx + (rad + 30.0) * math.cos(angle) - 30.0
            ly = cy + (rad + 18.0) * math.sin(angle) - 8.0
            self.add_text(lx, ly, ax_name, font_size=10, font_family=3, color="#0F172A", frame_id=frame_id)
            
        # Polígono de datos
        pts = []
        for i, sc in enumerate(scores):
            sc_val = min(1.0, max(0.0, sc))
            angle = (i * 2 * math.pi / n) - (math.pi / 2)
            pts.append((cx + (rad * sc_val) * math.cos(angle), cy + (rad * sc_val) * math.sin(angle)))
            
        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i + 1) % len(pts)]
            self.add_line(p1[0], p1[1], p2[0], p2[1], stroke="#D93829", stroke_w=2.2, frame_id=frame_id)
            self.add_ellipse(p1[0] - 4.0, p1[1] - 4.0, 8.0, 8.0, bg="#D93829", stroke="#FFFFFF", stroke_w=1.5, frame_id=frame_id)

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
            "files": self.files
        }

    def save(self, filepath: str):
        """Guarda el archivo .excalidraw en formato JSON minificado estricto."""
        data = self.to_dict()
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

    def export_svg(self, filepath: str) -> str:
        """Exporta la escena directamente a formato SVG."""
        from export import export_scene
        return export_scene(self, filepath, format="svg")

    def export_excalidraw(self, filepath: str) -> str:
        """Exporta la escena directamente a formato Excalidraw JSON."""
        from export import export_scene
        return export_scene(self, filepath, format="excalidraw")
