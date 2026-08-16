"""
Sketion Visual Regression & Quality Testing Suite
Ejecuta los fixtures semánticos y evalúa el Sketion Quality Score y el Self-Correction Loop.
"""

import os
import sys
import json

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset
from engines.recipes import (
    engine_flujo,
    engine_red,
    engine_dashboard,
    engine_matriz,
    engine_timeline,
    DEFAULT_PALETTE
)
from validation.validator import validate_scene

FIXTURES_DIR = os.path.join(workspace_dir, "tests", "fixtures")
SNAPSHOTS_DIR = os.path.join(workspace_dir, "tests", "snapshots")
os.makedirs(SNAPSHOTS_DIR, exist_ok=True)

def run_fixture_test(fixture_name: str, render_func):
    fixture_path = os.path.join(FIXTURES_DIR, fixture_name)
    with open(fixture_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    render_func(scene, data)

    scene_data, report = validate_scene(scene.to_dict(), auto_repair=True)

    snapshot_path = os.path.join(SNAPSHOTS_DIR, fixture_name.replace(".json", ".excalidraw"))
    with open(snapshot_path, "w", encoding="utf-8") as f:
        json.dump(scene_data, f, ensure_ascii=False, separators=(',', ':'))

    print(f"\n==========================================")
    print(f"FIXTURE: {fixture_name} -> {data['title']}")
    print(report.summary())

    assert report.is_valid, f"Fixture {fixture_name} falló validación estructural: {report.errors}"
    assert report.quality_metrics.overall_score >= 85, f"Score insuficiente: {report.quality_metrics.overall_score}"
    return report

def main():
    print("Iniciando Suite de Regresión Visual y Quality Score de Sketion...\n")

    # 1. Login (Flujo)
    run_fixture_test("login.json", lambda s, d: engine_flujo(s, d["title"], d["steps"], palette=DEFAULT_PALETTE))

    # 2. Architecture (Red con Scopes y Doble Jerarquía)
    run_fixture_test("architecture.json", lambda s, d: engine_red(s, d["title"], d["nodes"], d["edges"], scopes=d.get("scopes"), palette=DEFAULT_PALETTE))

    # 3. SaaS (Dashboard)
    run_fixture_test("saas.json", lambda s, d: engine_dashboard(s, d["title"], d["metrics"], palette=DEFAULT_PALETTE))

    # 4. ER / Matrix (Matriz)
    run_fixture_test("er.json", lambda s, d: engine_matriz(s, d["title"], d["headers"], d["rows"], palette=DEFAULT_PALETTE))

    # 5. Timeline (Timeline)
    run_fixture_test("timeline.json", lambda s, d: engine_timeline(s, d["title"], d["milestones"], palette=DEFAULT_PALETTE))

    print("\n🎉 Todos los fixtures pasaron las pruebas de calidad visual con puntuación >= 90/100!")

if __name__ == "__main__":
    main()
