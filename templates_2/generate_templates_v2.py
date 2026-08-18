"""
Sketion Expansion Library v2 Master Orchestrator (v10.0 GA)
Invoca los 10 generadores modulares especializados para producir las 150 plantillas de templates_2.
Genera template_manifest.json con metadatos completos y clasificación de complejidad.
"""

import os
import sys
import json

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from templates_2.generators.common import MANIFEST_RECORDS, BASE_DIR
from templates_2.generators import (
    gen_01_estudio,
    gen_02_ingenieria,
    gen_03_software,
    gen_04_data_ai,
    gen_05_negocios,
    gen_06_producto,
    gen_07_ux,
    gen_08_design_thinking,
    gen_09_agile,
    gen_10_productividad
)

def main():
    print("=" * 110)
    print("INICIANDO COMPILACION MODULAR DE SKETION EXPANSION LIBRARY V2 (150 PLANTILLAS)")
    print("=" * 110)
    
    MANIFEST_RECORDS.clear()
    
    gen_01_estudio.generate()
    gen_02_ingenieria.generate()
    gen_03_software.generate()
    gen_04_data_ai.generate()
    gen_05_negocios.generate()
    gen_06_producto.generate()
    gen_07_ux.generate()
    gen_08_design_thinking.generate()
    gen_09_agile.generate()
    gen_10_productividad.generate()

    manifest_data = {
        "version": "2.0.0",
        "total_templates": len(MANIFEST_RECORDS),
        "total_categories": 10,
        "grand_total_ecosystem": 62 + len(MANIFEST_RECORDS),
        "standards": {
            "emojis": 0,
            "typography": "Inter (fontFamily: 3)",
            "orthogonal_routing": "90 degrees",
            "min_padding": "35px",
            "vcs_benchmark": ">= 99.0 / 100"
        },
        "templates": MANIFEST_RECORDS
    }

    manifest_path = os.path.join(BASE_DIR, "template_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    print("=" * 110)
    print(f"COMPILACION EXITOSA DE LAS 150 PLANTILLAS EN: {BASE_DIR}")
    print(f"TOTAL PLANTILLAS PRODUCIDAS: {len(MANIFEST_RECORDS)}")
    print(f"MANIFEST GUARDADO EN: {manifest_path}")
    print("=" * 110)

if __name__ == "__main__":
    main()
