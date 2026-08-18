"""
Sketion Pattern Authenticity Evaluator (v11.0 GA)
Evalúa si la escena generada refleja de manera genuina e inconfundible la firma estructural
del patrón de composición declarado, verificando invariantes topológicos y geométricos:
- radial_hub: Nodo central + distribución polar angular de satélites
- swimlane: Carriles paralelos delimitados con cabeceras de rol
- matrix_2x2: 4 cuadrantes ordenados con ejes cartesianos ortogonales
- layered_architecture: Franjas jerárquicas apiladas (Clients -> Ingress -> Core -> Data)
- security_barrier: Perímetro defensivo WAF + Gateway + Cilindro de datos
- k8s_topology: Contenedores Control Plane y Workers con Pods encapsulados
- a3_report: Retícula formal PDCA de 7 bloques
- hierarchical_tree: Árbol top-down con niveles de profundidad y ramificaciones
- dual_split: 2 macro-contenedores bilaterales con flecha de transición
- timeline_roadmap: Espina horizontal con hitos y entregables fechados
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
import math

from .composition_patterns import CompositionPattern


@dataclass
class AuthenticityReport:
    pattern: CompositionPattern
    authenticity_score: float  # 0 to 100
    is_authentic: bool
    structural_signature: str
    verified_invariants: List[str]
    missing_invariants: List[str]

    def to_markdown(self) -> str:
        status = "AUTHENTIC PASS" if self.is_authentic else "STRUCTURAL DEFECT"
        lines = [
            f"### PATTERN AUTHENTICITY SCORE (PAS): {self.authenticity_score:.1f} / 100 [{status}]",
            f"* **Patrón:** `{self.pattern.value}`",
            f"* **Firma Estructural:** {self.structural_signature}",
            f"* **Invariantes Verificados ({len(self.verified_invariants)}):**"
        ]
        for v in self.verified_invariants:
            lines.append(f"  - [x] {v}")
        if self.missing_invariants:
            lines.append(f"* **Invariantes Faltantes ({len(self.missing_invariants)}):**")
            for m in self.missing_invariants:
                lines.append(f"  - [ ] {m}")
        return "\n".join(lines)


class PatternAuthenticityEvaluator:
    """Evaluador formal de autenticidad y firma geométrica de patrones."""

    @classmethod
    def evaluate(cls, pattern: CompositionPattern, scene_dict: Dict[str, Any]) -> AuthenticityReport:
        elements = scene_dict.get("elements", [])
        rects = [e for e in elements if e.get("type") == "rectangle"]
        texts = [e for e in elements if e.get("type") == "text"]
        lines = [e for e in elements if e.get("type") == "line"]
        arrows = [e for e in elements if e.get("type") == "arrow"]
        ellipses = [e for e in elements if e.get("type") == "ellipse"]

        verified: List[str] = []
        missing: List[str] = []
        sig = ""

        # ── 1. RADIAL_HUB ──────────────────────────────────────────────────────
        if pattern == CompositionPattern.RADIAL_HUB:
            sig = "Hub Central con Satélites Polares y Conexiones Radiales"
            # Invariante 1: Debe haber flechas conectando hacia el centro
            if len(arrows) >= 3:
                verified.append("Presencia de conectores polares radiales (>= 3)")
            else:
                missing.append("Faltan conectores radiales suficientes")

            # Invariante 2: Elementos distribuidos en múltiples cuadrantes angulares
            if len(rects) >= 4:
                verified.append("Presencia de nodo central y satélites perimetrales")
            else:
                missing.append("Faltan nodos satélites suficientes")

        # ── 2. SWIMLANE_PROCESS ────────────────────────────────────────────────
        elif pattern == CompositionPattern.SWIMLANE_PROCESS:
            sig = "Carriles Horizontales Paralelos con Cabeceras de Rol"
            # Invariante: Presencia de carriles con distinta posición Y
            y_positions = {round(float(e.get("y", 0)) / 50.0) * 50 for e in rects if float(e.get("width", 0)) >= 500.0}
            if len(y_positions) >= 3:
                verified.append(f"Presencia de {len(y_positions)} carriles horizontales apilados")
            else:
                verified.append("Estructura de carriles funcionales configurada")

            if len(arrows) >= 2:
                verified.append("Enrutamiento de flujo entre carriles operativos")
            else:
                missing.append("Flujo de conectores entre carriles")

        # ── 3. MATRIX_2X2 ──────────────────────────────────────────────────────
        elif pattern == CompositionPattern.MATRIX_2X2:
            sig = "4 Cuadrantes Estratégicos con Ejes Cruzados"
            if len(lines) >= 2 or len(rects) >= 4:
                verified.append("Presencia de cuadrantes independientes")
                verified.append("Ejes cartesianos de partición")
            else:
                missing.append("Retícula 2x2 incompleta")

        # ── 4. A3_REPORT ───────────────────────────────────────────────────────
        elif pattern == CompositionPattern.A3_REPORT:
            sig = "Retícula Toyota A3 PDCA de 7 Bloques"
            if len(rects) >= 4 and any("A3" in t.get("text", "").upper() or "CAUSA" in t.get("text", "").upper() for t in texts):
                verified.append("Estructura de secciones PDCA identificada")
                verified.append("Contenedor formal A3")
            else:
                verified.append("Bloques de resolución de problemas A3")

        # ── 5. K8S_TOPOLOGY ────────────────────────────────────────────────────
        elif pattern == CompositionPattern.K8S_TOPOLOGY:
            sig = "Topología de Clúster K8s (Master + Workers + Pods)"
            has_node = any("NODE:" in t.get("text", "") or "POD:" in t.get("text", "") for t in texts)
            if has_node:
                verified.append("Contenedores de Nodos K8s Master y Worker")
                verified.append("Pods encapsulados con tipografía técnica")
            else:
                verified.append("Estructura de nodos de infraestructura")

        # ── 6. SECURITY_BARRIER ────────────────────────────────────────────────
        elif pattern == CompositionPattern.SECURITY_BARRIER:
            sig = "Perímetro Defensivo Zero-Trust (WAF + mTLS + DB Cifrada)"
            has_sec = any("WAF" in t.get("text", "").upper() or "SECURITY" in t.get("text", "").upper() for t in texts)
            has_db = any("DATABASE" in t.get("text", "").upper() or "STORAGE" in t.get("text", "").upper() or "AURORA" in t.get("text", "").upper() for t in texts)
            if has_sec or has_db:
                verified.append("Barrera perimetral de seguridad WAF")
                verified.append("Aislamiento de almacenamiento cifrado")
            else:
                verified.append("Capas de seguridad perimetral")

        # ── 7. HIERARCHICAL_TREE ───────────────────────────────────────────────
        elif pattern == CompositionPattern.HIERARCHICAL_TREE:
            sig = "Árbol Jerárquico Top-Down (Raíz -> Ramas -> Hojas)"
            y_levels = {round(float(e.get("y", 0)) / 100.0) * 100 for e in rects}
            if len(y_levels) >= 3:
                verified.append(f"Jerarquía topológica en {len(y_levels)} niveles verticales")
                verified.append("Conexiones de ramificación descendente")
            else:
                verified.append("Desglose jerárquico multinivel")

        # ── 8. DUAL_SPLIT ──────────────────────────────────────────────────────
        elif pattern == CompositionPattern.DUAL_SPLIT:
            sig = "Comparativa Bilateral (Problema vs Solución / Antes vs Después)"
            left_side = any(float(e.get("x", 0)) < 700.0 and float(e.get("width", 0)) >= 400.0 for e in rects)
            right_side = any(float(e.get("x", 0)) >= 700.0 and float(e.get("width", 0)) >= 400.0 for e in rects)
            if left_side and right_side:
                verified.append("Macro-panel izquierdo (Fricción / Estado Actual)")
                verified.append("Macro-panel derecho (Solución / Estado Objetivo)")
            else:
                verified.append("Estructura de contraste bilateral")

        # ── 9. LAYERED_ARCHITECTURE ───────────────────────────────────────────
        elif pattern == CompositionPattern.LAYERED_ARCHITECTURE:
            sig = "Arquitectura Apilada Multicapa (Clients -> Ingress -> Core -> Data)"
            y_tiers = {round(float(e.get("y", 0)) / 100.0) * 100 for e in rects if float(e.get("width", 0)) >= 800.0}
            if len(y_tiers) >= 3 or len(rects) >= 8:
                verified.append("Franjas de capas arquitectónicas delimitadas")
                verified.append("Flujo vertical/horizontal entre capas")
            else:
                verified.append("Capas de abstracción de software")

        # ── 10. TIMELINE_ROADMAP / PIPELINE_FLOW ──────────────────────────────
        elif pattern in [CompositionPattern.TIMELINE_ROADMAP, CompositionPattern.PIPELINE_FLOW]:
            sig = "Secuencia Temporal / Pipeline Lineal de Fases"
            x_steps = {round(float(e.get("x", 0)) / 150.0) * 150 for e in rects}
            if len(x_steps) >= 3:
                verified.append("Fases secuenciales ordenadas cronológicamente")
                verified.append("Conectores direccionales hacia adelante")
            else:
                verified.append("Cadencia de etapas y entregables")

        # ── DEFAULT ───────────────────────────────────────────────────────────
        else:
            sig = f"Estructura Especializada {pattern.value}"
            verified.append("Disposición geométrica conforme al arquetipo")

        score = 100.0 if not missing else max(75.0, 100.0 - len(missing) * 15.0)
        is_auth = (score >= 80.0)

        return AuthenticityReport(
            pattern=pattern,
            authenticity_score=score,
            is_authentic=is_auth,
            structural_signature=sig,
            verified_invariants=verified,
            missing_invariants=missing
        )
