"""
Sketion Narrative Board & Presentation Composer (v11.0)
Modela historias técnicas y ejecutivas integradas y permite proyectarlas como:
1. Vista Deep-Dive (Tablero integral conectado en un solo canvas).
2. Vista Presentación (Secuencia de frames coordinados tipo slides con StyleLock).
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

from semantic.content_model import ContentModel, SystemNodeSpec, MetricSpec
from layout.layout_solver import LayoutSolver, LayoutAlgorithm
from design.theme_engine import ThemeEngine, VisualStyleType, SemanticColorRole
from render.excalidraw_builder import ExcalidrawScene


@dataclass
class NarrativeSection:
    """Sección narrativa dentro de una historia técnica."""
    title: str
    phase_number: int
    summary: str
    key_points: List[str]
    is_hero: bool = False
    metrics: List[Dict[str, str]] = field(default_factory=list)


@dataclass
class NarrativeBoard:
    """Estructura de historia técnica completa de nivel 3 (Narrative)."""
    title: str
    subtitle: str
    domain: str = "business"
    sections: List[NarrativeSection] = field(default_factory=list)
    style: VisualStyleType = VisualStyleType.EXECUTIVE


class NarrativeComposer:
    """Compositor de historias técnicas y presentaciones coordinadas."""

    @classmethod
    def create_standard_story(cls, title: str, domain: str = "business") -> NarrativeBoard:
        """Crea una estructura narrativa de 6 fases estándar: Contexto -> Problema -> Análisis -> Estrategia -> Ejecución -> Métricas."""
        sections = [
            NarrativeSection("1. CONTEXTO & VISION", 1, "Estado actual del ecosistema y visión estratégica.", ["Demanda de modernización cloud", "Objetivo de eficiencia operativa"], is_hero=False),
            NarrativeSection("2. EL PROBLEMA / FRICCION", 2, "Puntos de dolor críticos y cuellos de botella.", ["Tiempo de respuesta elevado en pico", "Costos de infraestructura duplicados"], is_hero=True),
            NarrativeSection("3. ANALISIS ARQUITECTONICO", 3, "Diagnóstico técnico de causa raíz y dependencias.", ["Monolito con acoplamiento en base de datos", "Falta de aislamiento de dominios"], is_hero=False),
            NarrativeSection("4. ESTRATEGIA DE SOLUCION", 4, "Arquitectura objetivo y principios directores.", ["Migración a microservicios con eventos Kafka", "Despliegue Multi-AZ en Kubernetes"], is_hero=True),
            NarrativeSection("5. PLAN DE EJECUCION", 5, "Roadmap de fases e hitos de entrega continua.", ["Fase 1: Core Payments", "Fase 2: Conciliación", "Fase 3: Analytics"], is_hero=False),
            NarrativeSection("6. METRICAS & KPIS", 6, "Indicadores clave de rendimiento y ROI.", ["Latencia P99: -65%", "Disponibilidad: 99.99%", "Costo Cloud: -30%"], is_hero=False)
        ]
        return NarrativeBoard(title=title, subtitle="Narrative Technical Deep-Dive", domain=domain, sections=sections)

    @classmethod
    def render_deep_dive_board(cls, board: NarrativeBoard, scene: ExcalidrawScene, style: VisualStyleType = VisualStyleType.EDITORIAL):
        """Renderiza la historia completa como un tablero conectado en un solo lienzo ancho."""
        theme = ThemeEngine.get_theme(style)
        tw, th = 2200.0, 960.0
        fid = scene.add_frame(board.title, 0.0, 0.0, tw, th)

        # Header del tablero
        scene.add_rect(40.0, 30.0, tw - 80.0, 70.0, bg=theme.surface_elevated, stroke=theme.primary_hero, stroke_w=1.8, roundness_type=3, frame_id=fid)
        scene.add_text(60.0, 50.0, board.title.upper(), font_size=18, font_family=theme.font_family, color=theme.primary_hero, frame_id=fid)
        scene.add_text(tw - 380.0, 56.0, "NARRATIVE DEEP-DIVE BOARD", font_size=11, font_family=theme.font_family, color=theme.neutral, frame_id=fid)

        # 6 Secciones conectadas horizontalmente
        n_sec = len(board.sections)
        sec_w = (tw - 80.0 - (n_sec - 1) * 35.0) / n_sec

        for i, sec in enumerate(board.sections):
            sx = 40.0 + i * (sec_w + 35.0)
            sy = 130.0
            sh = 760.0

            is_h = sec.is_hero
            scene.add_rect(sx, sy, sec_w, sh, bg=theme.surface_elevated if is_h else theme.surface, stroke=theme.primary_hero if is_h else theme.border, stroke_w=1.8 if is_h else 1.2, roundness_type=3, frame_id=fid)
            scene.add_text(sx + 16.0, sy + 25.0, sec.title, font_size=12, font_family=theme.font_family, color=theme.primary_hero if is_h else theme.text_main, frame_id=fid)
            scene.add_text(sx + 16.0, sy + 70.0, sec.summary, font_size=10, font_family=theme.font_family, color=theme.text_muted, frame_id=fid)

            for pi, pt in enumerate(sec.key_points):
                py = sy + 150.0 + pi * 85.0
                scene.add_rect(sx + 12.0, py, sec_w - 24.0, 70.0, bg=theme.background, stroke=theme.border, stroke_w=1.0, roundness_type=3, frame_id=fid)
                scene.add_text(sx + 20.0, py + 22.0, f"• {pt}", font_size=10, font_family=theme.font_family, color=theme.text_main, frame_id=fid)

            # Conector horizontal a la siguiente sección
            if i < n_sec - 1:
                next_sx = sx + sec_w + 35.0
                mid_y = sy + sh * 0.5
                scene.add_arrow(sx + sec_w, mid_y, next_sx, mid_y, stroke=theme.primary_hero if is_h else theme.neutral, stroke_w=1.8, frame_id=fid)

    @classmethod
    def render_presentation_slides(cls, board: NarrativeBoard, scene: ExcalidrawScene, style: VisualStyleType = VisualStyleType.EXECUTIVE):
        """Renderiza cada sección como un frame individual tipo slide para presentaciones."""
        theme = ThemeEngine.get_theme(style)
        slide_w = 1440.0
        slide_h = 900.0

        for i, sec in enumerate(board.sections):
            ox = i * 1600.0
            fid = scene.add_frame(f"Slide {i+1}: {sec.title}", ox, 0.0, slide_w, slide_h)

            # Slide Header
            scene.add_rect(ox + 60.0, 50.0, slide_w - 120.0, 90.0, bg=theme.surface_elevated, stroke=theme.primary_hero, stroke_w=2.0, roundness_type=3, frame_id=fid)
            scene.add_text(ox + 90.0, 80.0, f"[{i+1}/{len(board.sections)}]  {sec.title}", font_size=20, font_family=theme.font_family, color=theme.primary_hero, frame_id=fid)

            # Slide Body Card
            scene.add_rect(ox + 60.0, 180.0, slide_w - 120.0, 640.0, bg=theme.surface, stroke=theme.border, stroke_w=1.5, roundness_type=3, frame_id=fid)
            scene.add_text(ox + 90.0, 220.0, sec.summary, font_size=15, font_family=theme.font_family, color=theme.text_muted, frame_id=fid)

            for pi, pt in enumerate(sec.key_points):
                py = 320.0 + pi * 130.0
                scene.add_rect(ox + 90.0, py, slide_w - 180.0, 100.0, bg=theme.background, stroke=theme.border, stroke_w=1.2, roundness_type=3, frame_id=fid)
                scene.add_text(ox + 120.0, py + 35.0, f"• {pt}", font_size=14, font_family=theme.font_family, color=theme.text_main, frame_id=fid)
