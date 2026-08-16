"""
Sketion Excalidraw Builder Core (Render Layer)
Generador de escenas .excalidraw válidas, compactas, ligeras y con vinculación estricta de elementos.
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
        """Crea un texto libre (no vinculado a una caja)."""
        lines = text.split("\n")
        line_h = 1.25
        est_h = len(lines) * font_size * line_h
        est_w = max(len(l) for l in lines) * (font_size * 0.55) if lines else 50

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
        """
        Crea una tarjeta rectangular con texto estrictamente vinculado.
        Garantiza que containerId y boundElements estén perfectamente sincronizados.
        """
        container = self.add_rect(x, y, w, h, bg=bg, stroke=stroke, stroke_w=stroke_w,
                                  stroke_style=stroke_style, roundness_type=roundness_type,
                                  frame_id=frame_id)
        
        text_id = rid()
        container["boundElements"].append({"id": text_id, "type": "text"})

        text_elem = self._base_element("text", x, y, w, h, text_color, "transparent", frame_id=frame_id)
        text_elem["id"] = text_id
        text_elem.update({
            "fontSize": font_size,
            "fontFamily": font_family,
            "text": text,
            "textAlign": align,
            "verticalAlign": "middle",
            "containerId": container["id"],
            "originalText": text,
            "lineHeight": 1.25,
            "baseline": font_size
        })
        self.elements.append(text_elem)
        return container, text_elem

    def add_arrow(self, x1: float, y1: float, x2: float, y2: float,
                  stroke: str = "#64748B", stroke_w: float = 1.5,
                  dashed: bool = False, arrowhead: str = "triangle",
                  label: Optional[str] = None, orthogonal: bool = False,
                  frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea una flecha con coordenadas relativas y soporte ortogonal."""
        dx = x2 - x1
        dy = y2 - y1
        stroke_style = "dashed" if dashed else "solid"

        points = compute_orthogonal_arrow(x1, y1, x2, y2) if orthogonal else [[0.0, 0.0], [dx, dy]]

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
            mid_x = x1 + dx * 0.5
            mid_y = y1 + dy * 0.5 - 12
            self.add_text(mid_x, mid_y, label, font_size=11, font_family=3, color=stroke, align="center", frame_id=frame_id)

        return elem

    def add_line(self, x1: float, y1: float, x2: float, y2: float,
                 stroke: str = "#E2E8F0", stroke_w: float = 1.5,
                 dashed: bool = False, frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea una línea divisoria o eje."""
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

    def add_sticky_label(self, x: float, y: float, text: str,
                         bg: str = "#FEF08A", stroke: str = "#0C0C0C",
                         font_size: int = 15, angle_deg: float = -2.0,
                         frame_id: Optional[str] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Crea una etiqueta tipo Post-It rotada sutilmente (-2 a 2 grados)."""
        w = max(220.0, len(text) * font_size * 0.6)
        h = 55.0
        angle_rad = math.radians(angle_deg)
        
        container = self._base_element("rectangle", x, y, w, h, stroke, bg, 1.5, "solid",
                                       frame_id, angle_rad, {"type": 1})
        self.elements.append(container)

        text_id = rid()
        container["boundElements"].append({"id": text_id, "type": "text"})

        text_elem = self._base_element("text", x, y, w, h, stroke, "transparent", frame_id=frame_id, angle=angle_rad)
        text_elem["id"] = text_id
        text_elem.update({
            "fontSize": font_size,
            "fontFamily": 2,
            "text": text,
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": container["id"],
            "originalText": text,
            "lineHeight": 1.25,
            "baseline": font_size
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
        Crea una tarjeta de Doble Jerarquía:
        - Título principal en Sans bold (fontFamily: 2)
        - Subetiqueta técnica / rol en Cascadia mono (fontFamily: 3)
        """
        container = self.add_rect(x, y, w, h, bg=bg, stroke=stroke, stroke_w=stroke_w,
                                  stroke_style=stroke_style, roundness_type=roundness_type,
                                  frame_id=frame_id)
        
        text_id = rid()
        container["boundElements"].append({"id": text_id, "type": "text"})

        # Ensamblar texto estructurado
        if sublabel and metadata:
            full_text = f"{title}\n{sublabel} {metadata}"
        elif sublabel:
            full_text = f"{title}\n{sublabel}"
        elif metadata:
            full_text = f"{title}\n{metadata}"
        else:
            full_text = title

        text_elem = self._base_element("text", x, y, w, h, text_color, "transparent", frame_id=frame_id)
        text_elem["id"] = text_id
        text_elem.update({
            "fontSize": 14,
            "fontFamily": 2,
            "text": full_text,
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": container["id"],
            "originalText": full_text,
            "lineHeight": 1.25,
            "baseline": 14
        })
        self.elements.append(text_elem)
        return container, text_elem

    def add_scope_container(self, x: float, y: float, w: float, h: float,
                            label: str, stroke: str = "#CBD5E1",
                            bg: str = "#F8FAFC", frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Crea un contenedor de ámbito (Scope Boundary) con etiqueta superior izquierda mono."""
        container = self.add_rect(x, y, w, h, bg=bg, stroke=stroke, stroke_w=1.0,
                                  stroke_style="solid", roundness_type=3, frame_id=frame_id)
        # Etiqueta mono en la esquina superior izquierda
        self.add_text(x + 16, y + 12, label.upper(), font_size=11, font_family=3,
                      color="#64748B", align="left", frame_id=frame_id)
        return container

    def add_chip(self, x: float, y: float, w: float, h: float,
                 number: str, label: str, bg: str = "#0F172A",
                 text_color: str = "#FFFFFF", frame_id: Optional[str] = None):
        """Crea un chip de KPI/Dashboard con número gigante arriba y etiqueta chica abajo."""
        card = self.add_rect(x, y, w, h, bg=bg, stroke=bg, roundness_type=3, frame_id=frame_id)
        self.add_text(x + 20, y + 15, number, font_size=42, font_family=2, color=text_color, frame_id=frame_id)
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
