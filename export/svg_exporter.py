"""
Sketion Export Intelligence — SVG Exporter (v9.1)
Convierte una escena de Sketion / Excalidraw en un archivo SVG vectorial puro y estándar
con soporte para tipografía web (Inter/Roboto), formas polimórficas, íconos y badges.
"""

from typing import Dict, Any, List
import html
import math


class SVGExporter:
    """Exportador de alta fidelidad de escenas Excalidraw a gráficos vectoriales SVG."""

    @classmethod
    def export(cls, scene_dict: Dict[str, Any], output_path: str, padding: float = 40.0) -> str:
        elements = scene_dict.get("elements", [])
        if not elements:
            svg_empty = '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"></svg>'
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(svg_empty)
            return output_path

        # 1. Calcular Bounding Box global
        min_x = min(e.get("x", 0.0) for e in elements)
        min_y = min(e.get("y", 0.0) for e in elements)
        max_x = max(e.get("x", 0.0) + e.get("width", 0.0) for e in elements)
        max_y = max(e.get("y", 0.0) + e.get("height", 0.0) for e in elements)

        view_x = min_x - padding
        view_y = min_y - padding
        view_w = (max_x - min_x) + (padding * 2.0)
        view_h = (max_y - min_y) + (padding * 2.0)

        svg_parts: List[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_x:.1f} {view_y:.1f} {view_w:.1f} {view_h:.1f}" width="{view_w:.1f}" height="{view_h:.1f}">',
            '  <defs>',
            '    <style>',
            '      @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap");',
            '      text { font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }',
            '    </style>',
            '    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">',
            '      <polygon points="0 0, 10 3.5, 0 7" fill="#2563EB" />',
            '    </marker>',
            '    <marker id="arrowhead-hero" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">',
            '      <polygon points="0 0, 10 3.5, 0 7" fill="#D93829" />',
            '    </marker>',
            '    <marker id="arrowhead-danger" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">',
            '      <polygon points="0 0, 10 3.5, 0 7" fill="#DC2626" />',
            '    </marker>',
            '  </defs>',
            f'  <rect x="{view_x:.1f}" y="{view_y:.1f}" width="{view_w:.1f}" height="{view_h:.1f}" fill="{scene_dict.get("appState", {}).get("viewBackgroundColor", "#F8FAFC")}" />'
        ]

        # 2. Renderizar Elementos
        for el in elements:
            t = el.get("type")
            x = el.get("x", 0.0)
            y = el.get("y", 0.0)
            w = el.get("width", 0.0)
            h = el.get("height", 0.0)
            stroke = el.get("strokeColor", "#0F172A")
            bg = el.get("backgroundColor", "transparent")
            stroke_w = el.get("strokeWidth", 1.0)
            dash = ' stroke-dasharray="6,6"' if el.get("strokeStyle") == "dashed" else ""

            if t in ["rectangle", "frame"]:
                rx = 6.0 if el.get("roundness") else 0.0
                svg_parts.append(f'  <rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{bg}" stroke="{stroke}" stroke-width="{stroke_w:.1f}"{dash} />')
            
            elif t == "ellipse":
                cx = x + (w * 0.5)
                cy = y + (h * 0.5)
                svg_parts.append(f'  <ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{w*0.5:.1f}" ry="{h*0.5:.1f}" fill="{bg}" stroke="{stroke}" stroke-width="{stroke_w:.1f}"{dash} />')
            
            elif t == "diamond":
                p1 = f"{x + w*0.5:.1f},{y:.1f}"
                p2 = f"{x + w:.1f},{y + h*0.5:.1f}"
                p3 = f"{x + w*0.5:.1f},{y + h:.1f}"
                p4 = f"{x:.1f},{y + h*0.5:.1f}"
                svg_parts.append(f'  <polygon points="{p1} {p2} {p3} {p4}" fill="{bg}" stroke="{stroke}" stroke-width="{stroke_w:.1f}"{dash} />')

            elif t == "line":
                points = el.get("points", [[0, 0], [w, h]])
                if len(points) >= 2:
                    x1 = x + points[0][0]
                    y1 = y + points[0][1]
                    x2 = x + points[1][0]
                    y2 = y + points[1][1]
                    svg_parts.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{stroke_w:.1f}"{dash} />')

            elif t == "arrow":
                points = el.get("points", [[0, 0], [w, h]])
                if len(points) >= 2:
                    x1 = x + points[0][0]
                    y1 = y + points[0][1]
                    x2 = x + points[1][0]
                    y2 = y + points[1][1]
                    marker = "arrowhead-hero" if stroke == "#D93829" else ("arrowhead-danger" if stroke == "#DC2626" else "arrowhead")
                    svg_parts.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{stroke_w:.1f}"{dash} marker-end="url(#{marker})" />')

            elif t == "text":
                text_content = html.escape(el.get("text", ""))
                font_size = el.get("fontSize", 14)
                font_weight = "600" if font_size >= 14 else "400"
                # Ajuste de línea base
                svg_parts.append(f'  <text x="{x:.1f}" y="{y + font_size:.1f}" fill="{stroke}" font-size="{font_size}px" font-weight="{font_weight}">{text_content}</text>')

            elif t == "freedraw":
                pts = el.get("points", [])
                if pts:
                    path_data = "M " + " ".join(f"{x + p[0]:.1f},{y + p[1]:.1f}" for p in pts)
                    svg_parts.append(f'  <path d="{path_data}" fill="none" stroke="{stroke}" stroke-width="{stroke_w:.1f}" stroke-linecap="round" stroke-linejoin="round" />')

        svg_parts.append('</svg>')

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(svg_parts))

        return output_path
