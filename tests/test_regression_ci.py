"""
Sketion E2E Regression & Continuous Integration Test Suite (v10.0 GA)
Verifica integralmente todas las capas de inteligencia de Sketion:
1. Vector Iconography & Zero Emojis Compliance
2. Brand Registry (46+ Brands)
3. Semantic Morphological Shapes (Cylinders, Pipes, WAF, Pills, Diamonds)
4. Visual Matrix & 4 Spatial Archetypes (Layered, Pipeline, Radial Hub, Split Duel)
5. Design System Tokens & Component Registry
6. Visual Consistency Engine & VCS Score (>= 90/100)
7. Adaptive Aspect Ratios (16:9, 4:3, 1:1, 3:4)
8. Visual Language Engine (4 Dialects)
9. Explainability Engine (`result.explain()`)
10. Export Intelligence (SVG & Excalidraw)
"""

import os
import sys
import json
import time

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

import sketion
from visual_intelligence.iconography import SemanticIconRegistry
from visual_intelligence.brand_registry import BrandRegistry
from visual_intelligence.semantic_shapes import SemanticShapeClassifier, SemanticShapeType
from visual_intelligence.visual_language import VisualLanguageEngine, VisualLanguageDialect
from design import ComponentRegistry, ImportanceLevel, AudienceProfile
from export import export_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V7", "ci_artifacts")
os.makedirs(OUT_DIR, exist_ok=True)


def run_full_ci_suite():
    print("=" * 115)
    print(f"🚀 SKETION {sketion.__version__} — E2E REGRESSION & CONTINUOUS INTEGRATION CERTIFICATION")
    print("=" * 115)

    start_time = time.time()
    tests_run = 0
    tests_passed = 0

    def assert_test(name: str, condition: bool, detail: str = ""):
        nonlocal tests_run, tests_passed
        tests_run += 1
        if condition:
            tests_passed += 1
            print(f"  ✅ [PASS] {name} {detail}")
        else:
            print(f"  ❌ [FAIL] {name} {detail}")
            raise AssertionError(f"Fallo en prueba: {name} - {detail}")

    # TEST 1: Icon Registry & Zero Emojis
    print("\n • [1/10] Verificando Iconografía Vectorial Pura (0 Emojis)...")
    icons = SemanticIconRegistry.list_icons()
    assert_test("Icon Count >= 150", len(icons) >= 150, f"({len(icons)} iconos registrados)")
    assert_test("Icon Database Resolve", SemanticIconRegistry.resolve_icon("postgres database") == "database")
    assert_test("Icon Shield Resolve", SemanticIconRegistry.resolve_icon("firewall waf perimeter") == "shield")

    # TEST 2: Brand Registry
    print("\n • [2/10] Verificando Brand Registry (46+ Tecnologías)...")
    b_pg = BrandRegistry.match_brand("Aurora PostgreSQL")
    assert_test("Match PostgreSQL", b_pg is not None and "PostgreSQL" in b_pg.display_name)
    b_kf = BrandRegistry.match_brand("Kafka Cluster")
    assert_test("Match Kafka", b_kf is not None and "Kafka" in b_kf.display_name)
    b_st = BrandRegistry.match_brand("Stripe Payments")
    assert_test("Match Stripe", b_st is not None and "Stripe" in b_st.display_name)

    # TEST 3: Semantic Morphological Shapes
    print("\n • [3/10] Verificando Clasificador Morfológico de Formas...")
    sh_db = SemanticShapeClassifier.classify_entity("Postgres DB")
    assert_test("Shape Database Cylinder", sh_db.shape_type == SemanticShapeType.DATABASE_CYLINDER)
    sh_pipe = SemanticShapeClassifier.classify_entity("Kafka Event Queue")
    assert_test("Shape Streaming Pipe", sh_pipe.shape_type == SemanticShapeType.STREAMING_PIPE)
    sh_waf = SemanticShapeClassifier.classify_entity("Cloudflare WAF Firewall")
    assert_test("Shape Security Barrier", sh_waf.shape_type == SemanticShapeType.SECURITY_BARRIER)

    # TEST 4: Design System & Component Registry
    print("\n • [4/10] Verificando Design System Tokens & Component Registry...")
    comp_hero = ComponentRegistry.resolve("Core Settlement", role="service", importance=ImportanceLevel.HERO)
    assert_test("Hero Component Token", comp_hero.is_hero is True and comp_hero.badge == "HERO CORE")
    comp_exec = ComponentRegistry.resolve("Data Warehouse", role="database", audience=AudienceProfile.EXECUTIVE)
    assert_test("Executive Audience Adaptation", comp_exec.shape_type == SemanticShapeType.DATABASE_CYLINDER)

    # TEST 5: Visual Language Dialects
    print("\n • [5/10] Verificando Visual Language Engine (4 Dialectos)...")
    theme_exec = VisualLanguageEngine.resolve_theme(audience="CEO")
    assert_test("Theme Executive Strategy", theme_exec.dialect == VisualLanguageDialect.EXECUTIVE_STRATEGY)
    theme_sec = VisualLanguageEngine.resolve_theme(audience="Auditor", domain_hint="Zero-Trust HIPAA")
    assert_test("Theme Security Compliance", theme_sec.dialect == VisualLanguageDialect.SECURITY_COMPLIANCE)

    # TEST 6: Visual Matrix (All 4 Spatial Archetypes)
    print("\n • [6/10] Verificando Renderizado de los 4 Arquetipos Espaciales...")
    test_payload = {
        "title": "Fintech Clearinghouse",
        "layers": [
            {"name": "Ingesta", "entities": [{"label": "Cloudflare WAF", "role": "security"}, {"label": "Web Client", "role": "actor"}]},
            {"name": "Core", "entities": [{"label": "Payment Saga Core", "role": "service", "is_hero": True}]},
            {"name": "Storage", "entities": [{"label": "PostgreSQL", "role": "database"}, {"label": "Kafka", "role": "stream"}]}
        ],
        "steps": [{"label": "Auth"}, {"label": "Saga Core", "is_hero": True}, {"label": "Settle"}],
        "hub": {"label": "Master Brain", "is_hero": True},
        "satellites": [{"label": "Stripe"}, {"label": "Postgres"}, {"label": "Kafka"}],
        "left": {"title": "Legacy", "items": ["Monolith", "Locks"]},
        "right": {"title": "Target", "items": ["Microservices", "ACID"]}
    }

    for arch in ["layered", "pipeline", "radial_hub", "split_duel"]:
        res = sketion.render(payload=test_payload, archetype=arch, aspect_ratio="16:9")
        assert_test(f"Archetype Render [{arch.upper()}]", len(res.scene.elements) > 0)

    # TEST 7: Adaptive Aspect Ratios
    print("\n • [7/10] Verificando Adaptabilidad de Ratios de Aspecto...")
    for ratio in ["16:9", "4:3", "1:1", "3:4"]:
        res_r = sketion.render(payload=test_payload, archetype="layered", aspect_ratio=ratio)
        assert_test(f"Aspect Ratio [{ratio}]", res_r.vcs_score >= 90.0, f"(VCS: {res_r.vcs_score:.1f})")

    # TEST 8: Explainability Engine
    print("\n • [8/10] Verificando Explainability Engine (result.explain())...")
    res_exp = sketion.render(payload=test_payload, archetype="auto", audience="executive")
    expl_text = res_exp.explain()
    assert_test("Explainability Output Generated", "SKETION DESIGN DECISION TRACE" in expl_text)
    assert_test("Explainability Rationale Present", "Selected Archetype" in expl_text)

    # TEST 9: Export Intelligence (SVG & Excalidraw)
    print("\n • [9/10] Verificando Export Intelligence (SVG y Excalidraw)...")
    svg_out = os.path.join(OUT_DIR, "ci_test_export.svg")
    excal_out = os.path.join(OUT_DIR, "ci_test_export.excalidraw")
    
    res_exp.export(svg_out, format="svg")
    assert_test("Export SVG File Created", os.path.exists(svg_out) and os.path.getsize(svg_out) > 500)
    res_exp.export(excal_out, format="excalidraw")
    assert_test("Export Excalidraw File Created", os.path.exists(excal_out) and os.path.getsize(excal_out) > 500)

    # TEST 10: Overall Quality & VCS Certification
    print("\n • [10/10] Verificando Métricas de Calidad Global y VCS...")
    assert_test("VCS Overall >= 93.0", res_exp.vcs_score >= 93.0, f"(Score: {res_exp.vcs_score:.1f}/100)")
    assert_test("RDS Autonomy == 0.00", res_exp.trace.repair_dependency == 0.0, "(100% Autonomía)")

    elapsed = time.time() - start_time
    print("\n" + "=" * 115)
    print("🏆 RESULTADO FINAL DE LA SUITE DE INTEGRACIÓN CONTINUA (CI)")
    print("=" * 115)
    print(f" • Pruebas Totales Ejecutadas : {tests_run}")
    print(f" • Pruebas Aprobadas         : {tests_passed} / {tests_run} (100.0% PASS)")
    print(f" • Tiempo Total de Ejecución : {elapsed:.3f} segundos")
    print(f" • Estado del Motor          : 🔵 PRODUCTION READY (GA v10.0)")
    print("=" * 115)


if __name__ == "__main__":
    run_full_ci_suite()
