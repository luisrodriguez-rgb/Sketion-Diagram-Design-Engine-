"""
Sketion 27 Visual Types Generator (v10.0 GA)
Genera la galería de los 27 tipos visuales canónicos de Diagram Design:
Exporta cada uno en formato .excalidraw y .svg vectorial web estándar.
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene
from visual_intelligence.visual_types_27 import VisualTypes27Engine
from export.svg_exporter import SVGExporter

OUT_DIR = os.path.join(workspace_dir, "docs", "gallery", "27_types")
os.makedirs(OUT_DIR, exist_ok=True)

VISUAL_TYPES = [
    ("01_architecture", "Architecture", "Components + connections block diagram", VisualTypes27Engine.render_architecture),
    ("02_flowchart", "Flowchart", "Decision logic & branching flow", VisualTypes27Engine.render_flowchart),
    ("03_sequence", "Sequence", "Messages over time & lifelines", VisualTypes27Engine.render_sequence),
    ("04_state_machine", "State machine", "States + transitions & loops", VisualTypes27Engine.render_state_machine),
    ("05_er_data_model", "ER / data model", "Entities + fields & relational keys", VisualTypes27Engine.render_er_model),
    ("06_timeline", "Timeline", "Events on an axis & milestones", VisualTypes27Engine.render_timeline),
    ("07_swimlane", "Swimlane", "Cross-functional flow across roles", VisualTypes27Engine.render_swimlane),
    ("08_quadrant", "Quadrant", "Two-axis positioning & clusters", VisualTypes27Engine.render_quadrant),
    ("09_nested", "Nested", "Hierarchy by containment & inset boxes", VisualTypes27Engine.render_nested),
    ("10_tree", "Tree", "Parent -> children hierarchical branching", VisualTypes27Engine.render_tree),
    ("11_org_chart", "Org chart", "Ownership + routing tree", VisualTypes27Engine.render_org_chart),
    ("12_venn", "Venn", "3-Set overlap & intersection core", VisualTypes27Engine.render_venn),
    ("13_layer_stack", "Layer stack", "Stacked abstractions with hero tier", VisualTypes27Engine.render_layer_stack),
    ("14_pyramid_funnel", "Pyramid / funnel", "Ranked hierarchy & volume drop-off", VisualTypes27Engine.render_pyramid_funnel),
    ("15_consultant_2x2", "Consultant 2x2", "Scenario matrix with named cells", VisualTypes27Engine.render_consultant_2x2),
    ("16_radar_spider", "Radar / Spider", "Multi-axis polar comparison", VisualTypes27Engine.render_radar_spider),
    ("17_loop_flywheel", "Loop", "Flywheel stations around a central hub", VisualTypes27Engine.render_loop_flywheel),
    ("18_it_current_state", "IT current-state", "Legacy landscape vs target modernization", VisualTypes27Engine.render_it_current_state),
    ("19_high_level", "High-Level", "End-to-end stack on a cluster", VisualTypes27Engine.render_high_level),
    ("20_gantt", "Gantt", "Tasks and phases on a calendar timeline", VisualTypes27Engine.render_gantt),
    ("21_scatter_plot", "Scatter plot", "Distribution and correlation trendline", VisualTypes27Engine.render_scatter_plot),
    ("22_process", "Process", "Multi-actor sequential workflow", VisualTypes27Engine.render_process),
    ("23_medallion", "Medallion", "Multi-tier data storage with arched links", VisualTypes27Engine.render_medallion),
    ("24_data_flow", "Data flow", "Role-scoped pipeline steps", VisualTypes27Engine.render_data_flow),
    ("25_dp_integration", "DP integration", "Sources -> core -> consumers topology", VisualTypes27Engine.render_dp_integration),
    ("26_dp_security_matrix", "DP security matrix", "Per-role access permissions grid", VisualTypes27Engine.render_dp_security_matrix),
    ("27_value_chain", "Value Chain", "Enterprise value creation flow & margin", VisualTypes27Engine.render_value_chain)
]


def generate_27_gallery():
    print("=" * 115)
    print("🎨 GENERANDO GALERÍA CANÓNICA DE LOS 27 TIPOS VISUALES (DIAGRAM DESIGN)")
    print("=" * 115)

    tw, th = 1550.0, 480.0

    for file_id, name, desc, render_fn in VISUAL_TYPES:
        scene = ExcalidrawScene(roughness=0, bg_color="#F8FAFC")
        fid = scene.add_frame(f"{name.upper()} — {desc.upper()}", 10, 10, tw, th)
        
        # Subtítulo editorial
        scene.add_text(30, 35, f"DIAGRAM DESIGN ARCHETYPE · {name.upper()}", font_size=11, font_family=3, color="#64748B", frame_id=fid)
        
        render_fn(scene, 10, 10, tw, th, frame_id=fid)
        scene.auto_fit_frame(fid, padding=35.0)
        
        excal_path = os.path.join(OUT_DIR, f"{file_id}.excalidraw")
        svg_path = os.path.join(OUT_DIR, f"{file_id}.svg")
        
        scene.save(excal_path)
        SVGExporter.export(scene.to_dict(), svg_path)
        print(f"   ✅ Generado: {file_id}.svg & .excalidraw ({name})")

    print("\n" + "=" * 115)
    print(f"🏆 27 TIPOS VISUALES GENERADOS EXITOSAMENTE EN: {OUT_DIR}")
    print("=" * 115)


if __name__ == "__main__":
    generate_27_gallery()
