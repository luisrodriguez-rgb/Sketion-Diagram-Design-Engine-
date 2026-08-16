"""
Sketion 4.0 — Motores de Arquitectura de Software y Nube (engines/software_types.py)
Implementa:
12. Architecture (Components + Connections + VPC / Subnets)
13. High-Level (End-to-End Stack on a Cluster)
14. Sequence (Messages Over Time with Lifelines & Activation Boxes)
15. State Machine (States + Transitions + Lifecycle Guardrails)
16. Layer Stack (Stacked Technological Abstractions)
17. Nested (Hierarchy by Containment)
18. Flowchart (Decision Logic with Branching)
"""

from typing import Dict, Any, List, Optional, Tuple
from render.excalidraw_builder import ExcalidrawScene

PALETTE = {
    "CANVAS": "#F4F4F4",
    "CARD": "#FFFFFF",
    "CARD_BORDER": "#BDBDBD",
    "INK": "#0C0C0C",
    "MUTED": "#8B8B8B",
    "STICKY": "#FFE95C",
    "PAIN_RED": "#E03A2F",
    "PAIN_BG": "#FDEFEF",
    "PAIN_BORDER": "#F05A5A",
    "BANNER_PINK": "#F5BEC0",
    "PASTEL_BLUE": "#9BC7E4",
    "PASTEL_GREEN": "#C2E5D3"
}


# =============================================================================
# 12. ARCHITECTURE (COMPONENTS + CONNECTIONS)
# =============================================================================
def render_architecture(scene: ExcalidrawScene, title: str,
                        scopes: List[Dict[str, Any]], connections: List[Tuple[str, str, str]],
                        x: float, y: float, w: float = 2800.0, h: float = 850.0,
                        frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"ARCHITECTURE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "arquitectura de software distribuida con boundaries de red y scopes seguros", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    sc_count = len(scopes)
    sc_w = (w - 120.0 - (sc_count - 1) * 65.0) / sc_count
    node_coords = {}

    for si, sc in enumerate(scopes):
        sx = x + 60.0 + si * (sc_w + 65.0)
        sy = y + 130.0
        sh = 550.0
        s_title = sc.get("title", f"Scope {si+1}")
        s_nodes = sc.get("nodes", [])
        
        scene.add_scope_container(sx, sy, sc_w, sh, label=s_title, stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)

        for ni, node in enumerate(s_nodes):
            nid = node.get("id", f"n_{si}_{ni}")
            ntitle = node.get("title", "Service")
            nsub = node.get("sub", "")
            is_hero = node.get("is_hero", False)
            
            ny = sy + 65.0 + ni * 115.0
            bg = PALETTE["PASTEL_GREEN"] if is_hero else "#FFFFFF"
            container, _ = scene.add_dual_card(sx + 20.0, ny, sc_w - 40.0, 90.0, ntitle, sublabel=nsub,
                                               bg=bg, stroke=PALETTE["INK"], text_color=PALETTE["INK"], frame_id=fid)
            node_coords[nid] = (container["x"], container["y"], container["width"], container["height"])

    for from_id, to_id, clbl in connections:
        if from_id in node_coords and to_id in node_coords:
            fx, fy, fw, fh = node_coords[from_id]
            tx, ty, tw, th = node_coords[to_id]
            if tx >= fx + fw:
                scene.add_arrow(fx + fw, fy + fh * 0.5, tx, ty + th * 0.5,
                                stroke=PALETTE["MUTED"], stroke_w=1.5, label=clbl, orthogonal=True, frame_id=fid)
            elif tx < fx:
                scene.add_arrow(fx, fy + 20.0, tx + tw, ty + 20.0,
                                stroke=PALETTE["MUTED"], stroke_w=1.5, label=clbl, orthogonal=True, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 13. HIGH-LEVEL (END-TO-END CLUSTER STACK)
# =============================================================================
def render_high_level(scene: ExcalidrawScene, title: str,
                      top_orchestrator: str, cluster_layers: List[Dict[str, Any]],
                      x: float, y: float, w: float = 2800.0, h: float = 850.0,
                      frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"HIGH-LEVEL: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "diagrama de alto nivel: orquestacion central y capas de infraestructura", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Top Orchestrator Banner
    scene.add_bound_card(x + 60.0, y + 130.0, w - 120.0, 75.0, top_orchestrator.upper(),
                         bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF",
                         font_size=14, roundness_type=3, frame_id=fid)

    # Cluster Layers
    layer_w = (w - 120.0) / len(cluster_layers)
    for li, layer in enumerate(cluster_layers):
        lx = x + 60.0 + li * layer_w
        ly = y + 230.0
        lh = 450.0
        ltitle = layer.get("title", f"Layer {li+1}")
        litems = layer.get("items", [])
        
        scene.add_scope_container(lx, ly, layer_w - 20.0, lh, label=ltitle, stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
        for ii, itxt in enumerate(litems):
            scene.add_bound_card(lx + 20.0, ly + 65.0 + ii * 100.0, layer_w - 60.0, 80.0, itxt,
                                 bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"], font_size=12, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 14. SEQUENCE (MESSAGES OVER TIME WITH ACTIVATION BOXES)
# =============================================================================
def render_sequence(scene: ExcalidrawScene, title: str,
                    actors: List[str], messages: List[Tuple[int, int, str, bool]],
                    x: float, y: float, w: float = 2800.0, h: float = 850.0,
                    frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"SEQUENCE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "diagrama de secuencia temporal con lineas de vida y cajas de activacion", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    act_count = len(actors)
    spacing = (w - 300.0) / max(1, act_count - 1)
    act_x = []

    # Actores y Líneas de Vida
    for ai, aname in enumerate(actors):
        ax = x + 150.0 + ai * spacing
        act_x.append(ax)
        is_hero = (ai == len(actors) - 1)
        
        # Actor Card
        bg = PALETTE["PASTEL_GREEN"] if is_hero else PALETTE["INK"]
        text_color = PALETTE["INK"] if is_hero else "#FFFFFF"
        scene.add_bound_card(ax - 120.0, y + 130.0, 240.0, 60.0, aname,
                             bg=bg, stroke=PALETTE["INK"], text_color=text_color,
                             font_size=13, roundness_type=3, frame_id=fid)
        
        # Lifeline vertical
        scene.add_line(ax, y + 190.0, ax, y + 680.0, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, dashed=True, frame_id=fid)

    # Mensajes
    for mi, (from_a, to_a, msg_text, is_return) in enumerate(messages):
        my = y + 240.0 + mi * 65.0
        x1 = act_x[from_a]
        x2 = act_x[to_a]
        
        # Activation Box en destino
        scene.add_rect(x2 - 8.0, my - 15.0, 16.0, 45.0, bg="#FFFFFF", stroke=PALETTE["INK"], stroke_w=1.0, frame_id=fid)
        
        # Flecha de mensaje
        scene.add_arrow(x1, my, x2, my, stroke=PALETTE["INK"], stroke_w=1.5,
                        dashed=is_return, label=msg_text, orthogonal=False, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 15. STATE MACHINE (STATES + TRANSITIONS)
# =============================================================================
def render_state_machine(scene: ExcalidrawScene, title: str,
                         states: List[Dict[str, Any]], transitions: List[Tuple[str, str, str]],
                         x: float, y: float, w: float = 2800.0, h: float = 850.0,
                         frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"STATE MACHINE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "maquina de estados finitos con transiciones y guardas de ciclo de vida", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    st_coords = {}
    st_count = len(states)
    st_w = 340.0
    st_h = 130.0
    spacing = (w - 200.0) / max(1, st_count)

    for si, state in enumerate(states):
        sid = state.get("id", f"st_{si}")
        sname = state.get("name", f"State {si+1}")
        sdesc = state.get("desc", "")
        is_hero = state.get("is_hero", False)
        is_final = state.get("is_final", False)
        
        sx = x + 100.0 + si * spacing
        sy = y + 320.0
        
        bg = PALETTE["PASTEL_GREEN"] if is_hero else (PALETTE["PASTEL_BLUE"] if is_final else "#FFFFFF")
        c, _ = scene.add_dual_card(sx, sy, st_w, st_h, sname.upper(), sublabel=sdesc,
                                   bg=bg, stroke=PALETTE["INK"], text_color=PALETTE["INK"], frame_id=fid)
        st_coords[sid] = (c["x"], c["y"], c["width"], c["height"])

    for fid_a, fid_b, tlabel in transitions:
        if fid_a in st_coords and fid_b in st_coords:
            ax, ay, aw, ah = st_coords[fid_a]
            bx, by, bw, bh = st_coords[fid_b]
            if bx >= ax + aw:
                scene.add_arrow(ax + aw, ay + ah * 0.5, bx, by + bh * 0.5,
                                stroke=PALETTE["INK"], stroke_w=1.5, label=tlabel, orthogonal=True, frame_id=fid)
            elif bx < ax:
                scene.add_arrow(ax, ay + 25.0, bx + bw, by + 25.0,
                                stroke=PALETTE["INK"], stroke_w=1.5, label=tlabel, orthogonal=True, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 16. LAYER STACK (STACKED ABSTRACTIONS)
# =============================================================================
def render_layer_stack(scene: ExcalidrawScene, title: str,
                       layers: List[Dict[str, Any]], x: float, y: float,
                       w: float = 2800.0, h: float = 850.0,
                       frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"LAYER STACK: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "pila de capas de abstraccion de software estructuradas verticalmente", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    l_count = len(layers)
    layer_h = 95.0
    start_y = y + 140.0
    card_w = w - 240.0

    for li, ldata in enumerate(layers):
        ly = start_y + li * (layer_h + 15.0)
        lname = ldata.get("name", f"Layer {li+1}")
        lsub = ldata.get("sub", "")
        is_hero = ldata.get("is_hero", False)
        
        bg = PALETTE["PASTEL_GREEN"] if is_hero else "#FFFFFF"
        scene.add_dual_card(x + 120.0, ly, card_w, layer_h, f"L{li+1}: {lname.upper()}", sublabel=lsub,
                            bg=bg, stroke=PALETTE["INK"], text_color=PALETTE["INK"], frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 17. NESTED (HIERARCHY BY CONTAINMENT)
# =============================================================================
def render_nested(scene: ExcalidrawScene, title: str,
                  outer_label: str, middle_label: str, inner_label: str,
                  x: float, y: float, w: float = 2800.0, h: float = 850.0,
                  frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"NESTED: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "jerarquia por contencion fisica y scopes anidados", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Outer
    scene.add_scope_container(x + 100.0, y + 140.0, w - 200.0, 550.0, label=outer_label.upper(), stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
    # Middle
    scene.add_scope_container(x + 300.0, y + 220.0, w - 600.0, 400.0, label=middle_label.upper(), stroke=PALETTE["CARD_BORDER"], bg=PALETTE["PASTEL_BLUE"], frame_id=fid)
    # Inner (Core Hero)
    scene.add_scope_container(x + 600.0, y + 300.0, w - 1200.0, 240.0, label=inner_label.upper(), stroke=PALETTE["INK"], bg=PALETTE["PASTEL_GREEN"], frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 18. FLOWCHART (DECISION LOGIC WITH BRANCHING)
# =============================================================================
def render_flowchart(scene: ExcalidrawScene, title: str,
                     nodes: List[Dict[str, Any]], branches: List[Tuple[int, int, str]],
                     x: float, y: float, w: float = 2800.0, h: float = 850.0,
                     frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"FLOWCHART: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "flujograma de decision logica y bifurcacion de caminos", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    node_coords = []
    card_w = 360.0
    card_h = 100.0
    spacing = (w - 200.0) / max(1, len(nodes))

    for ni, node in enumerate(nodes):
        nx = x + 100.0 + ni * spacing
        ny = y + 340.0
        ntxt = node.get("text", f"Paso {ni+1}")
        is_decision = node.get("is_decision", False)
        
        bg = PALETTE["STICKY"] if is_decision else "#FFFFFF"
        scene.add_bound_card(nx, ny, card_w, card_h, ntxt,
                             bg=bg, stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                             font_size=13, roundness_type=3, frame_id=fid)
        node_coords.append((nx, ny, card_w, card_h))

    for from_i, to_i, blbl in branches:
        if from_i < len(node_coords) and to_i < len(node_coords):
            fx, fy, fw, fh = node_coords[from_i]
            tx, ty, tw, th = node_coords[to_i]
            scene.add_arrow(fx + fw, fy + fh * 0.5, tx, ty + th * 0.5,
                            stroke=PALETTE["INK"], stroke_w=1.5, label=blbl, orthogonal=True, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid
