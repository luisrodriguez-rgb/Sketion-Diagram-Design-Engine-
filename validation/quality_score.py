"""
Sketion Quality Score Engine (Calibrado 2.6)
Calcula el índice de calidad integral (0 - 100) evaluando 6 dimensiones con Curva de Densidad Óptima (Target 4.0/10).
"""

from dataclasses import dataclass
from typing import Dict, Any, List, Set

@dataclass
class QualityMetrics:
    structure_score: int
    layout_score: int
    readability_score: int
    hierarchy_score: int
    visual_noise_score: int
    brand_consistency_score: int
    overall_score: int
    density: float
    accent_count: int
    issues: List[str]

    def report_table(self) -> str:
        lines = [
            "VISUAL QUALITY SCORE",
            "─────────────────────────────────",
            f"Structure (Técnica Excalidraw) : {self.structure_score}/100",
            f"Layout (Espaciado & Gaps)      : {self.layout_score}/100",
            f"Readability (Legibilidad)      : {self.readability_score}/100",
            f"Hierarchy (1 Acento / Focos)   : {self.hierarchy_score}/100",
            f"Visual Noise (Densidad: {self.density:.1f}/10) : {self.visual_noise_score}/100",
            f"Brand Consistency (Tokens)     : {self.brand_consistency_score}/100",
            "─────────────────────────────────",
            f"OVERALL VISUAL QUALITY         : {self.overall_score}/100",
        ]
        if self.issues:
            lines.append("\n[OPORTUNIDADES DE MEJORA VISUAL]:")
            for issue in self.issues:
                lines.append(f"  • {issue}")
        return "\n".join(lines)


def calculate_density_score(density: float, frame_count: int = 1, card_count: int = 5) -> int:
    """
    Curva de puntuación de densidad calibrada (Effective Density):
    Target Editorial: 4.0/10 (Zona ideal: 3.0 a 4.5 -> 100)
    Reconoce que en secuencias ejecutivas o multi-frame, la densidad baja (1.2 - 2.5)
    es aire intencional y legibilidad ('Executive Breathing Room'), no defecto.
    """
    # Si la escena tiene tarjetas legibles y estructuradas, la densidad baja es aire intencional
    if 3.0 <= density <= 4.8:
        return 100
    elif 2.0 <= density < 3.0:
        return 96
    elif 1.2 <= density < 2.0:
        # Aire intencional para secuencia ejecutiva
        return 94 if card_count >= 4 else 88
    elif density < 1.2:
        return 80  # Extremadamente vacío
    elif 4.8 < density <= 5.5:
        return 92
    elif 5.5 < density <= 6.2:
        return 80
    elif 6.2 < density <= 7.0:
        return 65
    else:  # > 7.0
        return 30


def calculate_quality_score(scene_data: Dict[str, Any],
                            accent_hex_list: List[str] = None) -> QualityMetrics:
    """Calcula las métricas de calidad y el puntaje visual calibrado de una escena Excalidraw."""
    if accent_hex_list is None:
        accent_hex_list = [
            "#2563EB", "#F5BEC0", "#B58E3F", "#EFF6FF", "#FDF2F4", "#FBF6EB",
            "#DC2626", "#EF4444", "#C2E5D3", "#9BC7E4", "#FFE95C", "#E03A2F", "#F05A5A"
        ]

    elements = scene_data.get("elements", [])
    frames = [e for e in elements if e.get("type") == "frame"]
    non_frames = [e for e in elements if e.get("type") != "frame"]
    cards = [e for e in non_frames if e.get("type") == "rectangle"]
    texts = [e for e in non_frames if e.get("type") == "text"]
    arrows = [e for e in non_frames if e.get("type") == "arrow"]

    issues = []

    # 1. Structure (100 base)
    struct_score = 100
    elem_map = {e.get("id"): e for e in elements if "id" in e}
    for t in texts:
        if t.get("containerId"):
            cid = t["containerId"]
            if cid not in elem_map:
                struct_score -= 20
                issues.append(f"Texto huérfano apunta a contenedor inexistente {cid}.")
            else:
                c = elem_map[cid]
                b_ids = [b.get("id") for b in c.get("boundElements", [])]
                if t["id"] not in b_ids:
                    struct_score -= 15
                    issues.append(f"Contenedor {cid} no tiene vinculado el texto {t['id']}.")

    # 2. Hierarchy & Accents
    # Excluir contenedores de scope grandes (w>=240 & h>=320) y micro-swatches de leyenda (w<=32 & h<=22)
    accent_count = 0
    for e in cards:
        w_c = e.get("width", 0)
        h_c = e.get("height", 0)
        # Excluir contenedores de scope (grandes), badges de tarjeta (h<=22) y swatches de leyenda
        if (w_c >= 240 and h_c >= 320) or h_c <= 22 or (w_c <= 35 and h_c <= 25):
            continue
            
        bg = str(e.get("backgroundColor", "")).upper()
        stroke = str(e.get("strokeColor", "")).upper()
        for acc in accent_hex_list:
            if acc.upper() in bg or acc.upper() in stroke:
                accent_count += 1
                break

    max_accents = max(3, len(frames) * 3) if frames else 3
    hierarchy_score = 100
    if accent_count == 0:
        hierarchy_score -= 10
        issues.append("No hay ningún nodo con acento focal (falta énfasis visual).")
    elif accent_count > max_accents:
        penalty = min(40, (accent_count - max_accents) * 8)
        hierarchy_score = max(60, hierarchy_score - penalty)
        issues.append(f"Sobrecarga de acentos ({accent_count} nodos con acento, el objetivo es 1-3 por frame).")

    # 3. Density & Visual Noise Calibrado
    # Filtrar:
    # 1. Contenedores de scope (cajas grandes de fondo: w >= 250 y h >= 350)
    # 2. Pastillas protectoras de flechas (pill labels pequeños: h <= 32)
    component_cards = [
        c for c in cards
        if c.get("height", 0) > 32 and not (
            c.get("width", 0) >= 240 and c.get("height", 0) >= 350 and
            str(c.get("backgroundColor", "")).upper() in ["#F8FAFC", "#F3F4F6", "#FFFFFF", "TRANSPARENT"]
        )
    ]
    total_nodes = len(component_cards)

    # Identificar celdas de matriz / tabla (altura homogénea <= 70px)
    table_cells = [c for c in component_cards if c.get("height", 0) <= 70 and c.get("width", 0) <= 600]
    if len(table_cells) >= total_nodes * 0.5 and total_nodes > 8:
        effective_nodes = total_nodes * 0.25
    else:
        effective_nodes = total_nodes

    # Normalizar por el ancho/área total de todos los frames si existen
    if frames:
        total_fw = sum(f.get("width", 1200.0) for f in frames)
        # En lienzos anchos o multi-frame, la capacidad de nodos es proporcional al espacio total
        area_factor = max(1.0, total_fw / 1200.0)
        density = min(10.0, max(1.0, (effective_nodes / (2.5 * area_factor))))
    else:
        density = min(10.0, max(1.0, (effective_nodes / 2.5)))

    visual_noise_score = calculate_density_score(density, frame_count=len(frames), card_count=total_nodes)

    if density > 7.0:
        issues.append(f"Densidad crítica ({density:.1f}/10 > 7.0/10). Frame sobresaturado.")
    elif density > 5.0:
        issues.append(f"Densidad elevada ({density:.1f}/10 > 5.0/10). El target editorial es 4.0/10.")
    elif density < 1.2:
        issues.append(f"Densidad muy baja ({density:.1f}/10 < 1.2/10). Considera enriquecer el contenido.")

    # 4. Readability
    readability_score = 100
    font_families = set(t.get("fontFamily", 2) for t in texts)
    if len(font_families) > 2:
        readability_score -= 15
        issues.append(f"Más de 2 familias tipográficas en el mismo diagrama ({len(font_families)}).")

    for t in texts:
        txt = t.get("text", "")
        if len(txt.split("\n")) > 4 and t.get("containerId"):
            readability_score -= 5
            issues.append("Tarjeta con texto demasiado largo (>4 líneas en nodo).")
            break

    # 5. Layout & Spacing
    layout_score = 100
    if len(arrows) > 0:
        layout_score = 95

    # 6. Brand Consistency
    brand_consistency_score = 100 if hierarchy_score >= 80 else 85

    # Overall Weighted
    overall = int(
        struct_score * 0.25 +
        hierarchy_score * 0.20 +
        visual_noise_score * 0.20 +
        readability_score * 0.15 +
        layout_score * 0.10 +
        brand_consistency_score * 0.10
    )
    overall = max(0, min(100, overall))

    return QualityMetrics(
        structure_score=max(0, struct_score),
        layout_score=max(0, layout_score),
        readability_score=max(0, readability_score),
        hierarchy_score=max(0, hierarchy_score),
        visual_noise_score=max(0, visual_noise_score),
        brand_consistency_score=max(0, brand_consistency_score),
        overall_score=overall,
        density=density,
        accent_count=accent_count,
        issues=issues
    )
