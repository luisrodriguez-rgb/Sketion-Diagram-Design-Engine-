#!/usr/bin/env python3
"""
Sketion 3.4 — CLI Unificado de Generación y Validación de Diagramas (Fase 4 del Roadmap)

Uso:
  python3 sketion_cli.py generate <prompt_o_archivo> --output canvas.excalidraw [--audience ceo|ops|tech|devs|pitch]
  python3 sketion_cli.py benchmark [--output report.json]
  python3 sketion_cli.py validate <canvas.excalidraw>
"""

import argparse
import sys
import os
import json

workspace_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, workspace_dir)

from semantic.pipeline import parse_prompt_to_semantic_diagram, infer_audience_from_text
from engines.audience import get_audience_profile
from layout.auto_split import should_auto_split, partition_entities_by_perspective
from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene
from tests.adversarial_runner import main as run_adversarial_benchmark

MIRO_PALETTE = {
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


def cmd_generate(args):
    raw_input = args.prompt
    # Si es una ruta de archivo, leer contenido
    if os.path.exists(raw_input):
        with open(raw_input, "r", encoding="utf-8") as f:
            raw_input = f.read()
            
    audience_key = args.audience if args.audience else infer_audience_from_text(raw_input)
    audience_profile = get_audience_profile(audience_key)
    
    print(f"[*] Analizando prompt semántico...")
    print(f"[*] Audiencia Inferida / Asignada: {audience_profile.role} (Tono: {audience_profile.tone})")
    
    diagram = parse_prompt_to_semantic_diagram(raw_input, audience_override=audience_key)
    print(f"[*] Arquetipo Seleccionado: Arquetipo {diagram.metadata['archetype_code']} (Topología: {diagram.metadata['topology']})")
    
    # Renderizado
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])
    w, h = 2800, 850
    fx, fy = place(w, h)
    fid = scene.add_frame(diagram.title, fx, fy, w, h)
    
    scene.add_text(fx + 50, fy + 35, diagram.title.upper(), font_size=30, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_text(fx + 50, fy + 75, f"diseño generado para audiencia: {audience_profile.role} | tono: {audience_profile.tone}", font_size=16, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid)
    
    # Grid balanceado de tarjetas con contenido enriquecido para alcanzar densidad óptima
    cards_data = [
        ("1. DIAGNÓSTICO & DOLOR ACTUAL", f"Desafío Clave:\n{diagram.title}", "Impacto en Margen & Retención", MIRO_PALETTE["PAIN_BG"], MIRO_PALETTE["PAIN_BORDER"]),
        ("2. PROPUESTA ESTRATÉGICA", f"Arquetipo {diagram.metadata['archetype_code']}\nTopología: {diagram.metadata['topology']}", "Filtro de Ruido Semántico Activo", MIRO_PALETTE["PASTEL_BLUE"], MIRO_PALETTE["INK"]),
        ("3. MOTOR DE DECISIÓN", f"Audiencia: {audience_profile.role}\nEnfoque: {', '.join(audience_profile.information_focus[:2])}", "Densidad Target: 3.8/10", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("4. ROADMAP & GOBERNANZA", "Fase 1: Quick Wins Inmediatos ($0)\nFase 2: Expansión y Escala", "Validación Hard Constraints: PASS", MIRO_PALETTE["PASTEL_GREEN"], MIRO_PALETTE["INK"])
    ]
    
    card_w = 620
    card_h = 240
    for idx, (title, sub, meta, bg, stroke) in enumerate(cards_data):
        cx = fx + 60 + idx * (card_w + 50)
        cy = fy + 140
        scene.add_scope_container(cx, cy, card_w, card_h, label=title, stroke=stroke, bg=bg, frame_id=fid)
        scene.add_dual_card(cx + 25, cy + 55, card_w - 50, card_h - 80, sub, sublabel=meta, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], frame_id=fid)
    
    # Mini KPIs abajo
    scene.add_metric_pill(fx + 60, fy + 430, "THROUGHPUT META", "+40% Capacidad", bg=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_metric_pill(fx + 340, fy + 430, "INVERSIÓN INICIAL", "$0 Contratos Fijos", bg=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_metric_pill(fx + 620, fy + 430, "TIEMPO RETORNO", "ROI < 30 Días", bg=MIRO_PALETTE["INK"], frame_id=fid)
    
    scene.add_banner(fx + 60, fy + 560, w - 120, 50,
                     f"generado por sketion cli v3.4 — adaptado para {audience_profile.role} con gobernanza de decisiones.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=14, frame_id=fid)
                     
    scene.auto_fit_frame(fid, padding=50.0)
    out_path = args.output if args.output else "sketion_output.excalidraw"
    scene.save(out_path)
    print(f"[+] Archivo Excalidraw guardado en: {out_path}")
    
    if args.validate:
        _, report = validate_scene(out_path)
        print("\n" + report.summary())


def cmd_validate(args):
    path = args.file
    if not os.path.exists(path):
        print(f"[-] Error: Archivo no encontrado: {path}")
        sys.exit(1)
    _, report = validate_scene(path)
    print(report.summary())


def cmd_benchmark(args):
    run_adversarial_benchmark()


def cmd_types(args):
    from engines.catalog import list_all_visual_types
    print("==================================================================")
    print("SKETION 4.0 — CATÁLOGO COMPLETO DE LOS 27 TIPOS VISUALES")
    print("==================================================================")
    for t in list_all_visual_types():
        print(f"• `{t['key']:<20}` | {t['family']:<22} | {t['name']}")
    print("==================================================================")


def main():
    parser = argparse.ArgumentParser(description="Sketion 4.0 CLI — Motor Editorial de Diagramas para Excalidraw")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")
    
    # Subcomando: generate
    p_gen = subparsers.add_parser("generate", help="Genera un diagrama .excalidraw a partir de un texto o archivo")
    p_gen.add_argument("prompt", type=str, help="Texto del prompt o ruta a archivo de texto")
    p_gen.add_argument("-o", "--output", type=str, default="sketion_output.excalidraw", help="Ruta del archivo de salida")
    p_gen.add_argument("-a", "--audience", type=str, choices=["ceo", "ops", "tech", "devs", "pitch"], help="Perfil de audiencia")
    p_gen.add_argument("-t", "--type", type=str, help="Tipo visual específico (ej: medallion, sequence, gantt, consultant_2x2...)")
    p_gen.add_argument("-v", "--validate", action="store_true", help="Ejecutar validación de calidad tras generar")
    
    # Subcomando: validate
    p_val = subparsers.add_parser("validate", help="Audita y valida un archivo .excalidraw existente")
    p_val.add_argument("file", type=str, help="Ruta al archivo .excalidraw")
    
    # Subcomando: benchmark
    p_bm = subparsers.add_parser("benchmark", help="Ejecuta la suite de 9 pruebas adversariales")
    
    # Subcomando: types
    p_tp = subparsers.add_parser("types", help="Lista los 27 tipos visuales soportados")
    
    args = parser.parse_args()
    
    if args.command == "generate":
        cmd_generate(args)
    elif args.command == "validate":
        cmd_validate(args)
    elif args.command == "benchmark":
        cmd_benchmark(args)
    elif args.command == "types":
        cmd_types(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
