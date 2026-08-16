"""
Sketion Hierarchy Layouts (Tree, Radial / Cerebro)
"""
from typing import List, Dict, Any

def compute_tree_layout(root_x: float, root_y: float, root_w: float, root_h: float,
                        branches: List[Dict[str, Any]], frame_w: float,
                        branch_w: float = 220, branch_h: float = 65,
                        branch_gap: float = 40, level_gap: float = 140) -> Dict[str, Any]:
    """Calcula la distribución jerárquica de Raíz -> Ramas Nivel 1 -> Subitems Nivel 2."""
    num_branches = len(branches)
    total_w = num_branches * branch_w + (num_branches - 1) * branch_gap if num_branches > 0 else branch_w
    start_x = root_x - (total_w - root_w) * 0.5

    branch_coords = []
    for i, branch in enumerate(branches):
        bx = start_x + i * (branch_w + branch_gap)
        by = root_y + level_gap
        
        subitems_coords = []
        for j, sub in enumerate(branch.get("subitems", [])):
            sx = bx + 20
            sy = by + branch_h + 25 + j * 50
            subitems_coords.append({"x": sx, "y": sy, "w": 180, "h": 40, "text": sub})

        branch_coords.append({
            "x": bx,
            "y": by,
            "w": branch_w,
            "h": branch_h,
            "title": branch.get("title", ""),
            "subitems": subitems_coords
        })

    return {
        "root": {"x": root_x, "y": root_y, "w": root_w, "h": root_h},
        "branches": branch_coords
    }

def compute_radial_layout(center_x: float, center_y: float, center_size: float,
                          branches_count: int, start_x: float, card_w: float = 280,
                          card_h: float = 90, gap_x: float = 40,
                          gap_y: float = 30) -> List[Dict[str, float]]:
    """Calcula la posición de ramas satélites para el motor CEREBRO."""
    coords = []
    for i in range(branches_count):
        col = i % 2
        row = i // 2
        bx = start_x + col * (card_w + gap_x)
        by = center_y - 40 + row * (card_h + gap_y)
        coords.append({"x": bx, "y": by, "w": card_w, "h": card_h, "idx": i})
    return coords
