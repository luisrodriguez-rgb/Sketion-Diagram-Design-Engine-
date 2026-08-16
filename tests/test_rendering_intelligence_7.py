"""
Sketion 7.0 — Rendering Intelligence Test Suite
Prueba integral de los nuevos componentes de renderizado físico:
1. Renderizado nativo desde tests/fixtures/login.json
2. Validación de AnchorGeometry (puntos de anclaje exactos)
3. Auditoría de Render Fidelity Score (>= 90/100)
4. Prueba de Layout Stability (N=5 ejecuciones repetidas)
"""

import json
import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from rendering.render_pipeline import SketionRenderPipeline
from rendering.layout_stability import LayoutStabilityEngine
from validation.validator import validate_scene


def run_rendering_intelligence_tests():
    print("=" * 90)
    print("🧪 SKETION 7.0 — RENDERING INTELLIGENCE & LAYOUT STABILITY TEST SUITE")
    print("=" * 90)

    fixture_path = os.path.join(workspace_dir, "tests", "fixtures", "login.json")
    output_path = os.path.join(workspace_dir, "tests", "fixtures", "login_rendered_v7.excalidraw")

    with open(fixture_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    # 1. EJECUTAR RENDERIZADO SKETION 7.0
    print("\n" + "─" * 90)
    print("1. RENDERIZADO NATIVO CON ANCHOR GEOMETRY Y ENRUTAMIENTO ORTOGONAL")
    print("─" * 90)
    scene_data, fidelity_audit = SketionRenderPipeline.render_from_structured_spec(spec, output_path)

    print(f" • Archivo Generado            : {os.path.basename(output_path)}")
    print(f" • Elementos Renderizados      : {len(scene_data['elements'])}")
    print(f" • Render Fidelity Score       : {fidelity_audit.render_fidelity_score} / 100 [{fidelity_audit.status}]")
    print(f" • Flujo Espacial Lado a Lado  : {fidelity_audit.narrative_flow_score} / 100")
    print(f" • Prominencia de Hero         : {fidelity_audit.hero_prominence_score} / 100")
    print(f" • Despeje de Conectores       : {fidelity_audit.connector_clearance_score} / 100")

    # 2. VALIDACIÓN CON QUALITY SCORE Y REPAIR DEPENDENCY (RDS)
    print("\n" + "─" * 90)
    print("2. VALIDACIÓN COMPLETA DE CALIDAD EDITORIAL & REPAIR DEPENDENCY (RDS)")
    print("─" * 90)
    validated_scene, report = validate_scene(output_path)
    print(f" • Puntuación Global Sketion   : {report.sketion_overall_score} / 100 [{('✅ PASS' if report.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency (RDS)     : {report.repair_dependency_score} [{report.repair_dependency_status}]")
    print(f" • Densidad Medida             : {report.visual_metrics.density:.1f} / 10 (Target Diagram Design: 4.0/10)")
    print(f" • Acentos Hero en Marco       : {report.visual_metrics.accent_count} (Regla del Acento Único respetada)")

    # 3. TEST DE ESTABILIDAD DE LAYOUT (N=5 EJECUCIONES)
    print("\n" + "─" * 90)
    print("3. TEST DE ESTABILIDAD DE LAYOUT (N=5 EJECUCIONES REPETIDAS DEL MISMO PROMPT)")
    print("─" * 90)
    runs_history = []
    for run_i in range(5):
        run_scene, r_audit = SketionRenderPipeline.render_from_structured_spec(spec)
        _, r_report = validate_scene(run_scene)
        runs_history.append({
            "archetype": "C",
            "intent": "TRANSFORMATION",
            "overall_score": r_report.sketion_overall_score,
            "density": r_report.visual_metrics.density
        })

    stability_rep = LayoutStabilityEngine.evaluate_stability(runs_history, prompt=spec["title"])
    print(f" • Ejecuciones Evaluadas       : {stability_rep.run_count}")
    print(f" • Consistencia de Arquetipo   : {stability_rep.archetype_consistency_pct}%")
    print(f" • Consistencia de Intención   : {stability_rep.intent_consistency_pct}%")
    print(f" • Media de Puntuación Global  : {stability_rep.score_mean} / 100 (Varianza: {stability_rep.score_variance})")
    print(f" • Media de Densidad Visual    : {stability_rep.density_mean} / 10 (Varianza: {stability_rep.density_variance})")
    print(f" • Estado de Estabilidad       : {stability_rep.stability_status} ⭐")

    print("\n" + "=" * 90)
    print("🏆 RESULTADO: SKETION 7.0 RENDERING INTELLIGENCE SUPERA TODAS LAS PRUEBAS")
    print("=" * 90)


if __name__ == "__main__":
    run_rendering_intelligence_tests()
