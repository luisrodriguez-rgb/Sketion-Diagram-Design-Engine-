"""
Sketion 20 Structural Composition Patterns (v11.0 GA)
Catálogo de los 20 patrones de composición visual que transforman un ContentModel
en una disposición gráfica armónica, conectada, diferenciada y determinista.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
import math

from semantic.content_model import ContentModel, SystemNodeType
from layout.layout_solver import LayoutSolver, LayoutAlgorithm
from design.theme_engine import ThemeEngine, VisualStyleType, SemanticColorRole
from render.excalidraw_builder import ExcalidrawScene


class CompositionPattern(Enum):
    LAYERED_ARCHITECTURE = "layered_architecture"
    RADIAL_HUB = "radial_hub"
    HIERARCHICAL_TREE = "hierarchical_tree"
    PIPELINE_FLOW = "pipeline_flow"
    MATRIX_2X2 = "matrix_2x2"
    SWIMLANE_PROCESS = "swimlane_process"
    DUAL_SPLIT = "dual_split"
    TIMELINE_ROADMAP = "timeline_roadmap"
    CORNELL_NOTES = "cornell_notes"
    A3_REPORT = "a3_report"
    KANBAN_BOARD = "kanban_board"
    RADAR_SPIDER = "radar_spider"
    HEXAGONAL_PORTS = "hexagonal_ports"
    K8S_TOPOLOGY = "k8s_topology"
    UML_CLASS_MODEL = "uml_class_model"
    SERVICE_BLUEPRINT = "service_blueprint"
    FUNNEL_CONVERSION = "funnel_conversion"
    DATA_LAKEHOUSE = "data_lakehouse"
    SECURITY_BARRIER = "security_barrier"
    NARRATIVE_BOARD = "narrative_board"


@dataclass
class PatternMetadata:
    pattern: CompositionPattern
    name: str
    preferred_domain: str
    layout_algorithm: LayoutAlgorithm
    typical_density: str
    expected_card_ratio: float
    description: str


class CompositionPatternRegistry:
    """Registro y descriptor de los 20 patrones estructurales de Sketion."""

    _PATTERNS: Dict[CompositionPattern, PatternMetadata] = {
        CompositionPattern.LAYERED_ARCHITECTURE: PatternMetadata(
            CompositionPattern.LAYERED_ARCHITECTURE, "Layered Architecture", "software",
            LayoutAlgorithm.LAYERED, "high", 0.45, "Capas horizontales o verticales (Clients -> Edge -> Core -> DB)"
        ),
        CompositionPattern.RADIAL_HUB: PatternMetadata(
            CompositionPattern.RADIAL_HUB, "Radial Ecosystem / Mind Map", "education",
            LayoutAlgorithm.RADIAL, "medium", 0.30, "Hub central con nodos satélites distribuidos polarmente"
        ),
        CompositionPattern.HIERARCHICAL_TREE: PatternMetadata(
            CompositionPattern.HIERARCHICAL_TREE, "Hierarchical Tree", "business",
            LayoutAlgorithm.TREE, "medium", 0.50, "Árbol jerárquico de arriba a abajo con niveles de desglose"
        ),
        CompositionPattern.PIPELINE_FLOW: PatternMetadata(
            CompositionPattern.PIPELINE_FLOW, "Pipeline Flow", "data",
            LayoutAlgorithm.TIMELINE, "medium", 0.40, "Secuencia de etapas lineales con validaciones intermedias"
        ),
        CompositionPattern.MATRIX_2X2: PatternMetadata(
            CompositionPattern.MATRIX_2X2, "Matrix 2x2 Quadrant", "business",
            LayoutAlgorithm.MATRIX, "medium", 0.50, "Cuatro cuadrantes estratégicos sobre dos ejes continuos"
        ),
        CompositionPattern.SWIMLANE_PROCESS: PatternMetadata(
            CompositionPattern.SWIMLANE_PROCESS, "Swimlane Process", "engineering",
            LayoutAlgorithm.SWIMLANE, "high", 0.40, "Carriles horizontales funcionales por rol o departamento"
        ),
        CompositionPattern.DUAL_SPLIT: PatternMetadata(
            CompositionPattern.DUAL_SPLIT, "Dual Split Comparison", "ux",
            LayoutAlgorithm.HIERARCHICAL, "medium", 0.40, "Comparativa bilateral (Antes vs Después / Problema vs Solución)"
        ),
        CompositionPattern.TIMELINE_ROADMAP: PatternMetadata(
            CompositionPattern.TIMELINE_ROADMAP, "Timeline Roadmap", "agile",
            LayoutAlgorithm.TIMELINE, "medium", 0.30, "Espina cronológica con hitos y entregables fechados"
        ),
        CompositionPattern.CORNELL_NOTES: PatternMetadata(
            CompositionPattern.CORNELL_NOTES, "Cornell Notes", "education",
            LayoutAlgorithm.HIERARCHICAL, "medium", 0.20, "Formato áureo con columna de ideas, notas y resumen"
        ),
        CompositionPattern.A3_REPORT: PatternMetadata(
            CompositionPattern.A3_REPORT, "Toyota A3 Report", "engineering",
            LayoutAlgorithm.MATRIX, "high", 0.30, "Retícula de 7 cuadrantes PDCA para resolución de problemas"
        ),
        CompositionPattern.KANBAN_BOARD: PatternMetadata(
            CompositionPattern.KANBAN_BOARD, "Kanban Board", "agile",
            LayoutAlgorithm.HIERARCHICAL, "high", 0.80, "Columnas de estado de flujo con tarjetas de trabajo y badges"
        ),
        CompositionPattern.RADAR_SPIDER: PatternMetadata(
            CompositionPattern.RADAR_SPIDER, "Radar Evaluation", "ux",
            LayoutAlgorithm.RADIAL, "high", 0.10, "Gráfico polar con polígonos concéntricos de evaluación de métricas"
        ),
        CompositionPattern.HEXAGONAL_PORTS: PatternMetadata(
            CompositionPattern.HEXAGONAL_PORTS, "Hexagonal Ports & Adapters", "software",
            LayoutAlgorithm.HIERARCHICAL, "high", 0.40, "Core de dominio central aislado con adaptadores in/out"
        ),
        CompositionPattern.K8S_TOPOLOGY: PatternMetadata(
            CompositionPattern.K8S_TOPOLOGY, "Kubernetes Node Topology", "software",
            LayoutAlgorithm.LAYERED, "very_high", 0.30, "Nodos Master y Workers con Pods y servicios encapsulados"
        ),
        CompositionPattern.UML_CLASS_MODEL: PatternMetadata(
            CompositionPattern.UML_CLASS_MODEL, "UML Class Model", "software",
            LayoutAlgorithm.HIERARCHICAL, "high", 0.20, "Clases de 3 compartimentos con visibilidad y tipado"
        ),
        CompositionPattern.SERVICE_BLUEPRINT: PatternMetadata(
            CompositionPattern.SERVICE_BLUEPRINT, "Service Blueprint", "ux",
            LayoutAlgorithm.SWIMLANE, "very_high", 0.35, "4 capas de interacción: Evidencia, Cliente, Frontstage, Backstage"
        ),
        CompositionPattern.FUNNEL_CONVERSION: PatternMetadata(
            CompositionPattern.FUNNEL_CONVERSION, "Conversion Funnel", "business",
            LayoutAlgorithm.TIMELINE, "medium", 0.25, "Embudo decreciente de conversión con tasas de retención"
        ),
        CompositionPattern.DATA_LAKEHOUSE: PatternMetadata(
            CompositionPattern.DATA_LAKEHOUSE, "Data Lakehouse Medallion", "data",
            LayoutAlgorithm.TIMELINE, "high", 0.35, "Capas Bronze (Raw) -> Silver (Cleaned) -> Gold (Aggregated)"
        ),
        CompositionPattern.SECURITY_BARRIER: PatternMetadata(
            CompositionPattern.SECURITY_BARRIER, "Defense-in-Depth Security", "software",
            LayoutAlgorithm.HIERARCHICAL, "high", 0.35, "Perímetro WAF con barreras defensivas y enlaces mTLS"
        ),
        CompositionPattern.NARRATIVE_BOARD: PatternMetadata(
            CompositionPattern.NARRATIVE_BOARD, "Narrative Executive Board", "business",
            LayoutAlgorithm.HIERARCHICAL, "very_high", 0.35, "Historia técnica completa: Contexto -> Problema -> Análisis -> Solución -> Métricas"
        )
    }

    @classmethod
    def select_pattern(cls, content: ContentModel) -> CompositionPattern:
        """Selecciona el patrón de composición óptimo a partir del contenido semántico."""
        if content.composition_pattern_hint:
            hint = content.composition_pattern_hint.lower()
            for pat in cls._PATTERNS:
                if pat.value == hint or hint in pat.value:
                    return pat

        d = content.domain.lower()
        title_lower = content.title.lower()

        if "mind map" in title_lower or "ecosystem" in title_lower or "ecosistema" in title_lower or "porter" in title_lower:
            return CompositionPattern.RADIAL_HUB
        elif "cornell" in title_lower or "apuntes" in title_lower:
            return CompositionPattern.CORNELL_NOTES
        elif "a3" in title_lower or "toyota" in title_lower or "5s" in title_lower or "fmea" in title_lower:
            return CompositionPattern.A3_REPORT
        elif "kanban" in title_lower or "sprint" in title_lower and "board" in title_lower:
            return CompositionPattern.KANBAN_BOARD
        elif "k8s" in title_lower or "kubernetes" in title_lower:
            return CompositionPattern.K8S_TOPOLOGY
        elif "uml" in title_lower or "class" in title_lower:
            return CompositionPattern.UML_CLASS_MODEL
        elif "security" in title_lower or "zero-trust" in title_lower or "waf" in title_lower or "seguridad" in title_lower:
            return CompositionPattern.SECURITY_BARRIER
        elif "lakehouse" in title_lower or "medallion" in title_lower:
            return CompositionPattern.DATA_LAKEHOUSE
        elif "radar" in title_lower or "spider" in title_lower or "competencia" in title_lower:
            return CompositionPattern.RADAR_SPIDER
        elif "blueprint" in title_lower or "service" in title_lower and "frontstage" in title_lower:
            return CompositionPattern.SERVICE_BLUEPRINT
        elif "tree" in title_lower or "desglose" in title_lower or "wbs" in title_lower or "arquitectura de informacion" in title_lower:
            return CompositionPattern.HIERARCHICAL_TREE
        elif "timeline" in title_lower or "roadmap" in title_lower or "hitos" in title_lower:
            return CompositionPattern.TIMELINE_ROADMAP
        elif "matrix" in title_lower or "swot" in title_lower or "bcg" in title_lower or "riesgo" in title_lower:
            return CompositionPattern.MATRIX_2X2
        elif "swimlane" in title_lower or "balanceo" in title_lower or "carril" in title_lower:
            return CompositionPattern.SWIMLANE_PROCESS
        elif "empatia" in title_lower or "scamper" in title_lower or "heuristica" in title_lower or "rice" in title_lower or "usabilidad" in title_lower:
            return CompositionPattern.DUAL_SPLIT
        elif d == "software":
            return CompositionPattern.LAYERED_ARCHITECTURE
        elif d == "data":
            return CompositionPattern.PIPELINE_FLOW
        elif d == "engineering":
            return CompositionPattern.HIERARCHICAL_TREE
        elif d == "ux":
            return CompositionPattern.DUAL_SPLIT
        else:
            return CompositionPattern.NARRATIVE_BOARD

    @classmethod
    def render_pattern(cls,
                       pattern: CompositionPattern,
                       content: ContentModel,
                       scene: ExcalidrawScene,
                       frame_id: Optional[str] = None,
                       style: VisualStyleType = VisualStyleType.EDITORIAL):
        """
        Renderiza la firma geométrica auténtica y especializada de cualquiera de los 20 patrones.
        Evita absolutamente la 'monocultura de cajas en línea horizontal'.
        """
        theme = ThemeEngine.get_theme(style)
        nodes = content.systems
        labels = [n.label for n in nodes] if nodes else ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

        # ── 1. RADIAL_HUB (Hub polar con satélites en círculo) ────────────────
        if pattern == CompositionPattern.RADIAL_HUB:
            cx, cy = 720.0, 480.0
            r_hub = 260.0
            # Hub central
            hero_label = nodes[0].label if nodes else "NODO CENTRAL"
            scene.add_rect(cx - 130.0, cy - 50.0, 260.0, 100.0, bg=theme.surface_elevated, stroke=theme.primary_hero, stroke_w=2.0, roundness_type=3, frame_id=frame_id)
            scene.add_text(cx - 110.0, cy - 12.0, hero_label[:28].upper(), font_size=12, font_family=theme.font_family, color=theme.primary_hero, frame_id=frame_id)

            satellites = labels[1:] if len(labels) > 1 else ["Satélite A", "Satélite B", "Satélite C", "Satélite D"]
            n_sat = len(satellites)
            for i, sat in enumerate(satellites):
                angle = (i * 2.0 * math.pi / n_sat) - (math.pi / 2.0)
                sx = cx + r_hub * math.cos(angle)
                sy = cy + r_hub * math.sin(angle)
                scene.add_rect(sx - 100.0, sy - 35.0, 200.0, 70.0, bg=theme.surface, stroke=theme.border, stroke_w=1.2, roundness_type=3, frame_id=frame_id)
                scene.add_text(sx - 85.0, sy - 10.0, sat[:24], font_size=11, font_family=theme.font_family, color=theme.text_main, frame_id=frame_id)
                # Conector bidireccional al centro
                scene.add_arrow(sx, sy, cx, cy, stroke=theme.secondary_accent, stroke_w=1.5, frame_id=frame_id)

        # ── 2. A3_REPORT (7 cuadrantes PDCA) ──────────────────────────────────
        elif pattern == CompositionPattern.A3_REPORT:
            scene.add_a3_report(60.0, 100.0, 1320.0, 740.0, title=content.title, frame_id=frame_id)

        # ── 3. CORNELL_NOTES (3 zonas áureas) ──────────────────────────────────
        elif pattern == CompositionPattern.CORNELL_NOTES:
            cues = labels[:3] if len(labels) >= 3 else ["Cuestión Clave 1", "Concepto Central", "Duda Metodológica"]
            notes_p = labels[3:] if len(labels) > 3 else ["Desarrollo de la idea principal", "Evidencias y fórmulas", "Aplicaciones prácticas"]
            scene.add_cornell_notes(60.0, 100.0, 1320.0, 740.0, topic=content.title, cues=cues, notes=notes_p, summary=content.goal or "Síntesis ejecutiva de la lección.", frame_id=frame_id)

        # ── 4. KANBAN_BOARD (Columnas verticales con tarjetas) ────────────────
        elif pattern == CompositionPattern.KANBAN_BOARD:
            cols = [
                {"name": "BACKLOG", "cards": [{"title": labels[0] if len(labels) > 0 else "Tarea A", "desc": "Prioridad Alta", "badge": "P0"}]},
                {"name": "EN PROCESO", "cards": [{"title": labels[1] if len(labels) > 1 else "Tarea B", "desc": "En desarrollo", "badge": "DEV"}]},
                {"name": "EN REVISIÓN", "cards": [{"title": labels[2] if len(labels) > 2 else "Tarea C", "desc": "Code Review", "badge": "QA"}]},
                {"name": "COMPLETADO", "cards": [{"title": labels[3] if len(labels) > 3 else "Tarea D", "desc": "Desplegado en Prod", "badge": "DONE"}]}
            ]
            scene.add_kanban_board(60.0, 100.0, 1320.0, 740.0, columns=cols, frame_id=frame_id)

        # ── 5. RADAR_SPIDER (Evaluación polar) ─────────────────────────────────
        elif pattern == CompositionPattern.RADAR_SPIDER:
            axes = labels[:6] if len(labels) >= 6 else ["Escalabilidad", "Seguridad", "Mantenibilidad", "Rendimiento", "Costos", "Observabilidad"]
            scene.add_radar_chart(720.0, 480.0, 260.0, axes=axes, scores=[0.85, 0.90, 0.75, 0.95, 0.70, 0.88], title=content.title, frame_id=frame_id)

        # ── 6. MATRIX_2X2 (4 cuadrantes estratégicos) ─────────────────────────
        elif pattern == CompositionPattern.MATRIX_2X2:
            mw, mh = 1320.0, 740.0
            ox, oy = 60.0, 100.0
            qw = (mw - 40.0) * 0.5
            qh = (mh - 40.0) * 0.5

            # Ejes cruzados
            scene.add_line(ox + qw + 20.0, oy, ox + qw + 20.0, oy + mh, stroke=theme.border, stroke_w=2.0, frame_id=frame_id)
            scene.add_line(ox, oy + qh + 20.0, ox + mw, oy + qh + 20.0, stroke=theme.border, stroke_w=2.0, frame_id=frame_id)

            quads = [
                (ox, oy, "Q1: ALTO IMPACTO / BAJO ESFUERZO", labels[0] if len(labels) > 0 else "Iniciativa Rápida", theme.surface_elevated),
                (ox + qw + 40.0, oy, "Q2: ALTO IMPACTO / ALTO ESFUERZO", labels[1] if len(labels) > 1 else "Apuesta Estratégica", theme.surface),
                (ox, oy + qh + 40.0, "Q3: BAJO IMPACTO / BAJO ESFUERZO", labels[2] if len(labels) > 2 else "Mejora Menor", theme.surface),
                (ox + qw + 40.0, oy + qh + 40.0, "Q4: BAJO IMPACTO / ALTO ESFUERZO", labels[3] if len(labels) > 3 else "Descartar / Evaluar", theme.surface)
            ]
            for qx, qy, qtitle, qdesc, qbg in quads:
                scene.add_rect(qx, qy, qw, qh, bg=qbg, stroke=theme.border, stroke_w=1.2, roundness_type=3, frame_id=frame_id)
                scene.add_text(qx + 20.0, qy + 25.0, qtitle, font_size=12, font_family=theme.font_family, color=theme.primary_hero, frame_id=frame_id)
                scene.add_text(qx + 20.0, qy + 70.0, f"• {qdesc}", font_size=12, font_family=theme.font_family, color=theme.text_main, frame_id=frame_id)

        # ── 7. SWIMLANE_PROCESS (Carriles horizontales funcionales) ────────────
        elif pattern == CompositionPattern.SWIMLANE_PROCESS:
            lanes = ["1. PLANIFICACIÓN", "2. INGENIERÍA / DEV", "3. VALIDACIÓN / QA", "4. DESPLIEGUE / OPS"]
            lh = 175.0
            for i, lane in enumerate(lanes):
                ly = 100.0 + i * 185.0
                # Header de carril
                scene.add_rect(60.0, ly, 220.0, lh, bg=theme.surface_elevated, stroke=theme.border, stroke_w=1.2, roundness_type=3, frame_id=frame_id)
                scene.add_text(75.0, ly + 75.0, lane, font_size=11, font_family=theme.font_family, color=theme.primary_hero, frame_id=frame_id)
                # Cuerpo de carril
                scene.add_rect(290.0, ly, 1090.0, lh, bg=theme.surface, stroke=theme.border, stroke_w=1.0, stroke_style="dashed", roundness_type=3, frame_id=frame_id)
                # Tarjeta de actividad dentro del carril
                act_label = labels[i] if i < len(labels) else f"Actividad {i+1}"
                scene.add_rect(330.0 + i * 220.0, ly + 40.0, 240.0, 95.0, bg=theme.background, stroke=theme.primary_hero if i==1 else theme.border, stroke_w=1.5 if i==1 else 1.0, roundness_type=3, frame_id=frame_id)
                scene.add_text(345.0 + i * 220.0, ly + 75.0, act_label[:22], font_size=11, font_family=theme.font_family, color=theme.text_main, frame_id=frame_id)
                if i < len(lanes) - 1:
                    # Flecha escalonada al siguiente carril
                    scene.add_arrow(450.0 + i * 220.0, ly + 135.0, 450.0 + (i+1) * 220.0, ly + 185.0 + 40.0, stroke=theme.primary_hero, stroke_w=1.5, frame_id=frame_id)

        # ── 8. K8S_TOPOLOGY (Master Control Plane + Workers con Pods) ─────────
        elif pattern == CompositionPattern.K8S_TOPOLOGY:
            scene.add_k8s_node(60.0, 100.0, 400.0, 740.0, node_name="k8s-master-01", role="control_plane", pods=["apiserver", "etcd-cluster", "kube-scheduler", "controller-mgr"], frame_id=frame_id)
            scene.add_k8s_node(490.0, 100.0, 430.0, 740.0, node_name="k8s-worker-01", role="worker", pods=["payment-api-pod-1", "payment-api-pod-2", "envoy-sidecar"], frame_id=frame_id)
            scene.add_k8s_node(950.0, 100.0, 430.0, 740.0, node_name="k8s-worker-02", role="worker", pods=["settlement-worker", "kafka-consumer", "fluent-bit"], frame_id=frame_id)
            # Enlaces
            scene.add_arrow(460.0, 400.0, 490.0, 400.0, stroke="#2563EB", stroke_w=2.0, frame_id=frame_id)
            scene.add_arrow(920.0, 400.0, 950.0, 400.0, stroke="#2563EB", stroke_w=2.0, frame_id=frame_id)

        # ── 9. SECURITY_BARRIER (Perímetro WAF con mTLS y DB Cifrada) ─────────
        elif pattern == CompositionPattern.SECURITY_BARRIER:
            # 1. Actor
            scene.add_actor_node(60.0, 360.0, 200.0, 180.0, "Cliente / Usuario", "HTTPS / TLS 1.3", frame_id=frame_id)
            # 2. WAF Perimeter
            scene.add_security_barrier(300.0, 180.0, 240.0, 540.0, "Cloudflare WAF", ["DDoS Layer 7", "IP Reputation", "SSL Inspection"], frame_id=frame_id)
            # 3. Core Service Hero
            scene.add_quad_card(580.0, 330.0, 280.0, 240.0, labels[1] if len(labels) > 1 else "Payment Core", "mTLS Zero-Trust Gateway", badge="CORE SERVICE", is_hero=True, frame_id=frame_id)
            # 4. Stream Queue
            scene.add_streaming_pipe(900.0, 360.0, 220.0, 180.0, "Kafka Audit Stream", ["audit.events.v1"], frame_id=frame_id)
            # 5. Encrypted DB Cylinder
            scene.add_database_cylinder(1160.0, 330.0, 220.0, 240.0, "Aurora PostgreSQL", "AES-256 Storage", frame_id=frame_id)

            # Conectores
            scene.add_arrow(260.0, 450.0, 300.0, 450.0, stroke="#0F172A", stroke_w=1.8, frame_id=frame_id)
            scene.add_arrow(540.0, 450.0, 580.0, 450.0, stroke="#D93829", stroke_w=2.0, frame_id=frame_id)
            scene.add_arrow(860.0, 450.0, 900.0, 450.0, stroke="#0F172A", stroke_w=1.5, frame_id=frame_id)
            scene.add_arrow(860.0, 480.0, 1160.0, 480.0, stroke="#D93829", stroke_w=2.0, frame_id=frame_id)

        # ── 10. DATA_LAKEHOUSE (Medallion Bronze, Silver, Gold) ───────────────
        elif pattern == CompositionPattern.DATA_LAKEHOUSE:
            tiers = [
                (60.0, "BRONZE ZONE (RAW)", "#FFF5F2", "#D97706", "Ingesta cruda JSON/Avro"),
                (500.0, "SILVER ZONE (CLEANSED)", "#F8FAFC", "#2563EB", "Modelos limpios dbt"),
                (940.0, "GOLD ZONE (AGGREGATED)", "#EFF6FF", "#059669", "Datamarts y Métricas BI")
            ]
            for tx, tname, tbg, tstroke, tdesc in tiers:
                scene.add_rect(tx, 100.0, 420.0, 740.0, bg=tbg, stroke=tstroke, stroke_w=1.8, roundness_type=3, frame_id=frame_id)
                scene.add_text(tx + 20.0, 130.0, tname, font_size=13, font_family=theme.font_family, color=tstroke, frame_id=frame_id)
                scene.add_database_cylinder(tx + 40.0, 200.0, 340.0, 200.0, tname.split()[0] + " Storage", tdesc, frame_id=frame_id)
                scene.add_quad_card(tx + 40.0, 440.0, 340.0, 140.0, "Transformador Spark", "Validación de esquema", badge="ENGINE", frame_id=frame_id)

            # Conectores entre zonas
            scene.add_arrow(480.0, 300.0, 500.0, 300.0, stroke="#D97706", stroke_w=2.0, frame_id=frame_id)
            scene.add_arrow(920.0, 300.0, 940.0, 300.0, stroke="#2563EB", stroke_w=2.0, frame_id=frame_id)

        # ── 11. UML_CLASS_MODEL (Clases de 3 compartimentos) ───────────────────
        elif pattern == CompositionPattern.UML_CLASS_MODEL:
            scene.add_uml_class(100.0, 200.0, 320.0, 260.0, "PaymentTransaction", ["+ id: UUID", "+ amount: Decimal", "+ currency: String"], ["+ execute(): Bool", "+ refund(): Bool"], frame_id=frame_id)
            scene.add_uml_class(560.0, 200.0, 320.0, 260.0, "LedgerEntry", ["+ entryId: UUID", "+ accountId: UUID", "+ balance: Decimal"], ["+ postEntry(): Void", "+ lock(): Void"], frame_id=frame_id)
            scene.add_uml_class(1020.0, 200.0, 320.0, 260.0, "SettlementBatch", ["+ batchId: UUID", "+ itemsCount: Int", "+ status: BatchStatus"], ["+ closeBatch(): Void", "+ exportISO(): File"], frame_id=frame_id)
            # Conectores de asociación
            scene.add_arrow(420.0, 330.0, 560.0, 330.0, stroke="#0F172A", stroke_w=1.5, frame_id=frame_id)
            scene.add_arrow(880.0, 330.0, 1020.0, 330.0, stroke="#0F172A", stroke_w=1.5, frame_id=frame_id)

        # ── 12. DUAL_SPLIT (Bilateral Antes vs Después / Problema vs Solución)
        elif pattern == CompositionPattern.DUAL_SPLIT:
            scene.add_rect(60.0, 100.0, 630.0, 740.0, bg="#FFF5F2", stroke="#DC2626", stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=frame_id)
            scene.add_text(90.0, 140.0, "ESTADO ACTUAL / PROBLEMA & FRICCIÓN", font_size=13, font_family=theme.font_family, color="#DC2626", frame_id=frame_id)
            scene.add_quad_card(100.0, 220.0, 550.0, 160.0, labels[0] if len(labels)>0 else "Monolito Acoplado", "Latencia alta y fallos en cascada", badge="FRICTION", frame_id=frame_id)
            scene.add_quad_card(100.0, 420.0, 550.0, 160.0, labels[1] if len(labels)>1 else "Base de Datos Saturada", "Locks en tablas críticas", badge="BOTTLENECK", frame_id=frame_id)

            scene.add_rect(750.0, 100.0, 630.0, 740.0, bg="#EFF6FF", stroke="#2563EB", stroke_w=2.0, roundness_type=3, frame_id=frame_id)
            scene.add_text(780.0, 140.0, "ESTADO OBJETIVO / ARQUITECTURA PROPUESTA", font_size=13, font_family=theme.font_family, color="#2563EB", frame_id=frame_id)
            scene.add_quad_card(790.0, 220.0, 550.0, 160.0, labels[2] if len(labels)>2 else "Microservicios Autónomos", "Aislamiento por dominio y eventos", badge="SOLUTION", is_hero=True, frame_id=frame_id)
            scene.add_quad_card(790.0, 420.0, 550.0, 160.0, labels[3] if len(labels)>3 else "Bases de Datos Políglotas", "Escalabilidad horizontal independiente", badge="RESILIENCE", frame_id=frame_id)

            scene.add_arrow(690.0, 450.0, 750.0, 450.0, stroke="#2563EB", stroke_w=2.5, frame_id=frame_id)

        # ── 13. HIERARCHICAL_TREE (Árbol de arriba a abajo) ────────────────────
        elif pattern == CompositionPattern.HIERARCHICAL_TREE:
            # Nivel 0 (Raíz)
            scene.add_quad_card(560.0, 100.0, 320.0, 110.0, labels[0] if len(labels)>0 else "Sistema Raíz", "Dominio Principal", badge="ROOT", is_hero=True, frame_id=frame_id)
            # Nivel 1 (2 Ramas)
            scene.add_quad_card(260.0, 300.0, 280.0, 110.0, labels[1] if len(labels)>1 else "Rama A", "Subsistema 1", badge="BRANCH", frame_id=frame_id)
            scene.add_quad_card(900.0, 300.0, 280.0, 110.0, labels[2] if len(labels)>2 else "Rama B", "Subsistema 2", badge="BRANCH", frame_id=frame_id)
            # Nivel 2 (Hojas)
            scene.add_quad_card(120.0, 500.0, 240.0, 100.0, labels[3] if len(labels)>3 else "Hoja A1", "Detalle", badge="LEAF", frame_id=frame_id)
            scene.add_quad_card(400.0, 500.0, 240.0, 100.0, labels[4] if len(labels)>4 else "Hoja A2", "Detalle", badge="LEAF", frame_id=frame_id)
            scene.add_quad_card(760.0, 500.0, 240.0, 100.0, "Hoja B1", "Detalle", badge="LEAF", frame_id=frame_id)
            scene.add_quad_card(1040.0, 500.0, 240.0, 100.0, "Hoja B2", "Detalle", badge="LEAF", frame_id=frame_id)

            # Enlaces de árbol
            scene.add_arrow(720.0, 210.0, 400.0, 300.0, stroke="#0F172A", stroke_w=1.5, frame_id=frame_id)
            scene.add_arrow(720.0, 210.0, 1040.0, 300.0, stroke="#0F172A", stroke_w=1.5, frame_id=frame_id)
            scene.add_arrow(400.0, 410.0, 240.0, 500.0, stroke="#64748B", stroke_w=1.2, frame_id=frame_id)
            scene.add_arrow(400.0, 410.0, 520.0, 500.0, stroke="#64748B", stroke_w=1.2, frame_id=frame_id)

        # ── 14. TIMELINE_ROADMAP (Espina cronológica con hitos alternos) ──────
        elif pattern == CompositionPattern.TIMELINE_ROADMAP:
            # Espina central horizontal
            scene.add_line(100.0, 450.0, 1340.0, 450.0, stroke="#D93829", stroke_w=3.0, frame_id=frame_id)
            m_labels = labels[:4] if len(labels)>=4 else ["Q1: MVP", "Q2: Alpha", "Q3: Beta", "Q4: GA Launch"]
            for i, ml in enumerate(m_labels):
                mx = 180.0 + i * 300.0
                is_top = (i % 2 == 0)
                my = 220.0 if is_top else 520.0
                # Nodo hito en la espina
                scene.add_ellipse(mx + 90.0, 442.0, 16.0, 16.0, bg="#D93829", stroke="#FFFFFF", stroke_w=2.0, frame_id=frame_id)
                # Línea de unión
                scene.add_line(mx + 98.0, 442.0 if is_top else 458.0, mx + 98.0, my + (120.0 if is_top else 0.0), stroke="#94A3B8", stroke_w=1.2, dashed=True, frame_id=frame_id)
                # Tarjeta de hito
                scene.add_quad_card(mx, my, 200.0, 120.0, ml, f"Entregable #{i+1}", badge=f"FASE {i+1}", is_hero=(i==0), frame_id=frame_id)

        # ── 15. LAYERED_ARCHITECTURE (Capas horizontales clásicas con Cylinders)
        elif pattern == CompositionPattern.LAYERED_ARCHITECTURE:
            tiers = ["1. CAPA CLIENTE / CANALES", "2. INGRESS & SEGURIDAD", "3. CORE MICROSERVICIOS", "4. PERSISTENCIA & EVENTOS"]
            for i, tname in enumerate(tiers):
                ty = 100.0 + i * 190.0
                scene.add_rect(60.0, ty, 1320.0, 160.0, bg=theme.surface_elevated if i==2 else theme.surface, stroke=theme.primary_hero if i==2 else theme.border, stroke_w=1.8 if i==2 else 1.2, roundness_type=3, frame_id=frame_id)
                scene.add_text(80.0, ty + 25.0, tname, font_size=13, font_family=theme.font_family, color=theme.primary_hero if i==2 else theme.neutral, frame_id=frame_id)

                if i == 0:
                    scene.add_actor_node(300.0, ty + 45.0, 240.0, 95.0, "Web Portal", "HTTPS / React", frame_id=frame_id)
                    scene.add_actor_node(800.0, ty + 45.0, 240.0, 95.0, "Mobile App", "iOS / Android", frame_id=frame_id)
                elif i == 1:
                    scene.add_security_barrier(240.0, ty + 40.0, 400.0, 105.0, "Cloudflare WAF", ["DDoS", "TLS 1.3"], frame_id=frame_id)
                    scene.add_quad_card(740.0, ty + 45.0, 360.0, 95.0, "Envoy API Gateway", "JWT Auth & Routing", badge="INGRESS", frame_id=frame_id)
                elif i == 2:
                    scene.add_quad_card(200.0, ty + 45.0, 280.0, 95.0, labels[1] if len(labels)>1 else "Payment Service", "Saga Orchestration", badge="SERVICE", is_hero=True, frame_id=frame_id)
                    scene.add_quad_card(540.0, ty + 45.0, 280.0, 95.0, labels[2] if len(labels)>2 else "Accounts Engine", "Balance Management", badge="SERVICE", frame_id=frame_id)
                    scene.add_quad_card(880.0, ty + 45.0, 280.0, 95.0, "Notification Worker", "Email & Push", badge="ASYNC", frame_id=frame_id)
                elif i == 3:
                    scene.add_database_cylinder(240.0, ty + 35.0, 300.0, 115.0, "Aurora PostgreSQL", "ACID Master-Replica", frame_id=frame_id)
                    scene.add_streaming_pipe(600.0, ty + 45.0, 300.0, 95.0, "Kafka Event Bus", ["events.tx.v1"], frame_id=frame_id)
                    scene.add_database_cylinder(960.0, ty + 35.0, 300.0, 115.0, "Redis Cache", "Sub-ms Session Store", frame_id=frame_id)

                # Flechas de conexión entre capas
                if i < len(tiers) - 1:
                    scene.add_arrow(720.0, ty + 160.0, 720.0, ty + 190.0, stroke=theme.primary_hero if i==1 else theme.neutral, stroke_w=1.8, frame_id=frame_id)

        # ── 16. PIPELINE_FLOW (Secuencia horizontal con chevron) ───────────────
        elif pattern == CompositionPattern.PIPELINE_FLOW:
            stages = labels[:5] if len(labels)>=5 else ["1. Ingesta", "2. Validación", "3. Transformación", "4. Enriquecimiento", "5. Destino"]
            pw = (1320.0 - (len(stages)-1)*40.0) / len(stages)
            for i, stg in enumerate(stages):
                sx = 60.0 + i * (pw + 40.0)
                scene.add_rect(sx, 320.0, pw, 240.0, bg=theme.surface_elevated if i==2 else theme.surface, stroke=theme.primary_hero if i==2 else theme.border, stroke_w=1.8 if i==2 else 1.2, roundness_type=3, frame_id=frame_id)
                scene.add_text(sx + 15.0, 350.0, f"FASE 0{i+1}", font_size=10, font_family=theme.font_family, color=theme.primary_hero if i==2 else theme.neutral, frame_id=frame_id)
                scene.add_text(sx + 15.0, 410.0, stg[:20], font_size=12, font_family=theme.font_family, color=theme.text_main, frame_id=frame_id)
                if i < len(stages) - 1:
                    scene.add_arrow(sx + pw, 440.0, sx + pw + 40.0, 440.0, stroke=theme.primary_hero if i==1 else theme.neutral, stroke_w=2.0, frame_id=frame_id)

        # ── DEFAULT FALLBACK (Layout Solver Declarativo) ──────────────────────
        else:
            algo = cls._PATTERNS.get(pattern, cls._PATTERNS[CompositionPattern.LAYERED_ARCHITECTURE]).layout_algorithm
            solver = LayoutSolver(algorithm=algo, origin_x=80.0, origin_y=100.0)
            for i, node in enumerate(nodes):
                solver.add_node(node.id, node.label, is_hero=node.is_hero, layer_index=node.layer_index, shape=node.node_type.value)
            for r in content.relationships:
                solver.connect(r.source_id, r.target_id, label=r.label)
            solver.render_to_scene(scene, frame_id=frame_id)
