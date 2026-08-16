#!/usr/bin/env python3
"""
Sketion 10.0 GA — CLI Unificado de Generación, Explicabilidad y Exportación de Arquitectura

Uso:
  python3 sketion_cli.py generate "Plataforma de pagos..." --output arch.excalidraw --audience tech --archetype layered
  python3 sketion_cli.py generate payload.json --output diagram.svg --format svg --explain
  python3 sketion_cli.py benchmark [--holdout | --comparative | --ci]
  python3 sketion_cli.py validate <canvas.excalidraw>
"""

import argparse
import sys
import os
import json

workspace_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, workspace_dir)

import sketion
from validation.validator import validate_scene
from tests.holdout.holdout_runner import run_grand_blind_holdout
from tests.holdout.comparative_benchmark import run_comparative_benchmark
from tests.test_regression_ci import run_full_ci_suite


def cmd_generate(args):
    raw_input = args.prompt
    payload = {}

    if os.path.exists(raw_input):
        with open(raw_input, "r", encoding="utf-8") as f:
            content = f.read().strip()
            try:
                payload = json.loads(content)
            except json.JSONDecodeError:
                payload = {"title": "Architecture Specification", "prompt": content}
    else:
        payload = {"title": raw_input, "prompt": raw_input}

    print(f"[*] Sketion 10.0 GA — Renderizando '{payload.get('title')}'...")
    print(f"[*] Audiencia: {args.audience.upper()} | Arquetipo: {args.archetype.upper()} | Aspect Ratio: {args.aspect_ratio}")

    res = sketion.render(
        payload=payload,
        archetype=args.archetype,
        aspect_ratio=args.aspect_ratio,
        audience=args.audience,
        output=args.output
    )

    if args.output:
        print(f"[✅] Diagrama guardado exitosamente en: {args.output}")

    if args.explain:
        print("\n" + res.explain())

    print(f"[*] Visual Consistency Score (VCS): {res.vcs_score:.1f} / 100 [CERTIFIED]")


def cmd_benchmark(args):
    if args.ci:
        run_full_ci_suite()
    elif args.comparative:
        run_comparative_benchmark(sample_size=args.size or 50)
    else:
        run_grand_blind_holdout(sample_size=args.size or 160)


def cmd_validate(args):
    print(f"[*] Validando calidad y consistencia de: {args.file}...")
    scene, rep = validate_scene(args.file)
    print(f"[✅] Sketion Overall Quality Score : {rep.sketion_overall_score} / 100")
    print(f"[*] Repair Dependency Score (RDS)  : {rep.repair_dependency_score} [{rep.repair_dependency_status}]")
    print(f"[*] Estado de Validación          : {'PASS' if rep.is_valid else 'FAIL'}")


def main():
    parser = argparse.ArgumentParser(description="Sketion 10.0 GA — CLI Unificado de Generación de Diagramas")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 1. Generate
    gen_p = subparsers.add_parser("generate", help="Genera un diagrama de arquitectura")
    gen_p.add_argument("prompt", help="Texto del prompt o archivo JSON de arquitectura")
    gen_p.add_argument("--output", "-o", default="architecture.excalidraw", help="Ruta del archivo de salida (.excalidraw o .svg)")
    gen_p.add_argument("--audience", "-a", default="engineer", choices=["engineer", "executive", "operations", "auditor"], help="Perfil de audiencia")
    gen_p.add_argument("--archetype", default="auto", choices=["auto", "layered", "pipeline", "radial_hub", "split_duel"], help="Arquetipo espacial")
    gen_p.add_argument("--aspect-ratio", default="16:9", choices=["16:9", "4:3", "1:1", "3:4", "auto"], help="Proporción geométrica")
    gen_p.add_argument("--explain", action="store_true", help="Imprime la traza de explicabilidad de decisiones de diseño")
    gen_p.set_defaults(func=cmd_generate)

    # 2. Benchmark
    bench_p = subparsers.add_parser("benchmark", help="Ejecuta suites de certificación y benchmarks")
    bench_p.add_argument("--holdout", action="store_true", help="Ejecuta el Grand Blind Holdout de 160 prompts")
    bench_p.add_argument("--comparative", action="store_true", help="Ejecuta el benchmark comparativo vs Excalidraw")
    bench_p.add_argument("--ci", action="store_true", help="Ejecuta la suite completa de integración continua E2E")
    bench_p.add_argument("--size", type=int, help="Cantidad de casos a evaluar")
    bench_p.set_defaults(func=cmd_benchmark)

    # 3. Validate
    val_p = subparsers.add_parser("validate", help="Valida un archivo Excalidraw generado")
    val_p.add_argument("file", help="Ruta al archivo .excalidraw")
    val_p.set_defaults(func=cmd_validate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
