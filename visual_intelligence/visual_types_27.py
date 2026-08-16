"""
Sketion 27 Visual Types Engine (v10.0 GA)
Implementa la taxonomía visual completa y auténtica inspirada en Diagram Design / Nico's Kit:
Cada uno de los 27 tipos posee su propia geometría real:
1. Architecture       10. Tree               19. Gantt
2. Flowchart          11. Org chart          20. Scatter plot
3. Sequence           12. Venn               21. Process
4. State machine      13. Layer stack        22. Medallion
5. ER data model      14. Pyramid funnel     23. Data flow
6. Timeline           15. Consultant 2x2     24. DP integration
7. Swimlane           16. Radar spider       25. DP security matrix
8. Quadrant           17. Loop flywheel      26. Value Chain
9. Nested             18. IT current-state   27. High-Level
"""

from enum import Enum
import math
from typing import Dict, Any, List, Optional, Union
from render.excalidraw_builder import ExcalidrawScene


class VisualType27(Enum):
    ARCHITECTURE = "architecture"
    FLOWCHART = "flowchart"
    SEQUENCE = "sequence"
    STATE_MACHINE = "state_machine"
    ER_DATA_MODEL = "er_data_model"
    TIMELINE = "timeline"
    SWIMLANE = "swimlane"
    QUADRANT = "quadrant"
    NESTED = "nested"
    TREE = "tree"
    ORG_CHART = "org_chart"
    VENN = "venn"
    LAYER_STACK = "layer_stack"
    PYRAMID_FUNNEL = "pyramid_funnel"
    CONSULTANT_2X2 = "consultant_2x2"
    RADAR_SPIDER = "radar_spider"
    LOOP_FLYWHEEL = "loop_flywheel"
    IT_CURRENT_STATE = "it_current_state"
    HIGH_LEVEL = "high_level"
    GANTT = "gantt"
    SCATTER_PLOT = "scatter_plot"
    PROCESS = "process"
    MEDALLION = "medallion"
    DATA_FLOW = "data_flow"
    DP_INTEGRATION = "dp_integration"
    DP_SECURITY_MATRIX = "dp_security_matrix"
    VALUE_CHAIN = "value_chain"


class VisualTypes27Engine:
    """Motor especializado para renderizar los 27 tipos visuales canónicos de Diagram Design."""

    # -----------------------------------------------------------------------------------------------
    # 01. ARCHITECTURE (Components + Connections)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_architecture(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        # Contenedor Cloud
        scene.add_rect(x + 20, y + 20, w - 40, h - 40, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 40, y + 35, "AWS CLOUD ENVIRONMENT (US-EAST-1)", font_size=11, font_family=3, color="#64748B", frame_id=frame_id)

        # Capa Ingress
        scene.add_quad_card(x + 50, y + 70, 220, 110, "CloudFront Edge", "Global Anycast CDN", badge="EDGE", icon="cloud", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 50, y + 210, 220, 110, "ALB Ingress Gateway", "mTLS & Path Routing", badge="INGRESS", icon="gateway", is_hero=False, frame_id=frame_id)

        # Capa Core (Hero)
        scene.add_quad_card(x + 350, y + 130, 280, 140, "Core API Gateway", "JWT Auth & Rate Limiter", badge="HERO CORE", icon="server", is_hero=True, frame_id=frame_id)

        # Capa Microservicios
        scene.add_quad_card(x + 710, y + 70, 240, 110, "Order Service", "Saga Coordinator", badge="SERVICE", icon="server", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 710, y + 210, 240, 110, "Payment Service", "Stripe & Visa Proxy", badge="SERVICE", icon="server", is_hero=False, frame_id=frame_id)

        # Capa Persistencia
        scene.add_database_cylinder(x + 1030, y + 70, 240, 115, "Aurora PostgreSQL", "ACID Orders Store", badge="ACID DB", is_hero=False, frame_id=frame_id)
        scene.add_streaming_pipe(x + 1030, y + 210, 280, 115, "Kafka Event Bus", ["order.created", "tx.settled"], badge="STREAM", frame_id=frame_id)

        # Conectores
        scene.add_arrow(x + 270, y + 125, x + 350, y + 170, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 270, y + 265, x + 350, y + 230, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 630, y + 170, x + 710, y + 125, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 630, y + 230, x + 710, y + 265, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 950, y + 125, x + 1030, y + 125, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 950, y + 265, x + 1030, y + 265, stroke="#94A3B8", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 02. FLOWCHART (Decision Logic)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_flowchart(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        # Start
        scene.add_actor_node(x + 60, y + 170, 200, 55, "User Submits Order", role="START TRIGGER", icon="user", is_hero=False, frame_id=frame_id)
        
        # Step 1
        scene.add_quad_card(x + 320, y + 145, 220, 105, "Validate Stock", "Inventory Check", badge="STEP 1", icon="server", is_hero=False, frame_id=frame_id)
        
        # Decision Diamond
        scene.add_diamond(x + 600, y + 130, 160, 135, bg="#FFFBEB", stroke="#D97706", stroke_w=1.8, frame_id=frame_id)
        scene.add_text(x + 625, y + 185, "Stock > 0?", font_size=13, font_family=2, color="#92400E", frame_id=frame_id)
        
        # Branch YES (Hero)
        scene.add_quad_card(x + 840, y + 70, 260, 115, "Authorize Payment", "Capture Credit Card", badge="HERO CORE", icon="server", is_hero=True, frame_id=frame_id)
        scene.add_quad_card(x + 1170, y + 70, 220, 115, "Dispatch Order", "Generate Tracking", badge="SUCCESS", icon="server", is_hero=False, frame_id=frame_id)
        
        # Branch NO
        scene.add_quad_card(x + 840, y + 250, 260, 105, "Reject & Notify", "Send Out-Of-Stock Email", badge="FALLBACK", icon="server", is_hero=False, frame_id=frame_id)
        
        # Arrows
        scene.add_arrow(x + 260, y + 197, x + 320, y + 197, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 540, y + 197, x + 600, y + 197, stroke="#94A3B8", frame_id=frame_id)
        
        # YES Arrow
        scene.add_arrow(x + 760, y + 165, x + 840, y + 125, stroke="#16A34A", stroke_w=2.0, frame_id=frame_id)
        scene.add_text(x + 780, y + 135, "YES", font_size=11, font_family=3, color="#16A34A", frame_id=frame_id)
        scene.add_arrow(x + 1100, y + 125, x + 1170, y + 125, stroke="#16A34A", frame_id=frame_id)
        
        # NO Arrow
        scene.add_arrow(x + 760, y + 230, x + 840, y + 300, stroke="#DC2626", stroke_w=1.5, dashed=True, frame_id=frame_id)
        scene.add_text(x + 780, y + 265, "NO", font_size=11, font_family=3, color="#DC2626", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 03. SEQUENCE (Messages Over Time)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_sequence(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        actors = [
            ("Client Web", "CLIENT", x + 80),
            ("API Gateway", "GATEWAY", x + 380),
            ("Payment Core", "HERO SAGA", x + 680),
            ("Bank Gateway", "EXTERNAL", x + 980),
            ("Database", "LEDGER", x + 1240)
        ]
        
        # Lifelines & Actor Boxes
        for name, role, ax in actors:
            is_hero = "HERO" in role
            bg = "#FFF5F2" if is_hero else "#F8FAFC"
            strk = "#D93829" if is_hero else "#64748B"
            scene.add_rect(ax - 70, y + 40, 140, 45, bg=bg, stroke=strk, stroke_w=1.5, roundness_type=3, frame_id=frame_id)
            scene.add_text(ax - 55, y + 52, name, font_size=12, font_family=2, color="#0F172A", frame_id=frame_id)
            # Vertical lifeline
            scene.add_line(ax, y + 90, ax, y + h - 50, stroke="#CBD5E1", stroke_w=1.2, dashed=True, frame_id=frame_id)
        
        # Messages
        messages = [
            (x + 80, x + 380, y + 120, "1. POST /v1/charge (idempotency-key)", "#0F172A", False),
            (x + 380, x + 680, y + 170, "2. Initialize Payment Saga", "#0F172A", False),
            (x + 680, x + 980, y + 220, "3. Authorize via Visa Direct", "#D93829", False),
            (x + 980, x + 680, y + 270, "4. 200 OK (Auth Code: #89201)", "#16A34A", True),
            (x + 680, x + 1240, y + 320, "5. Write ACID Ledger Balance", "#0F172A", False),
            (x + 680, x + 80, y + 370, "6. 201 Created (Receipt JSON)", "#16A34A", True),
        ]
        for x1, x2, my, txt, col, dashed in messages:
            scene.add_arrow(x1, my, x2, my, stroke=col, stroke_w=1.5, dashed=dashed, frame_id=frame_id)
            scene.add_text(min(x1, x2) + 20, my - 16, txt, font_size=11, font_family=3, color=col, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 04. STATE MACHINE (States & Transitions)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_state_machine(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        states = [
            ("INIT", "Transacción Creada", x + 80, y + 170, False),
            ("AUTHORIZED", "Fondos Retenidos", x + 380, y + 170, False),
            ("CAPTURED", "Liquidación Exitosa", x + 720, y + 170, True),  # Hero state
            ("SETTLED", "Balance Confirmado", x + 1060, y + 170, False)
        ]
        for name, sub, sx, sy, is_hero in states:
            bg = "#FFF5F2" if is_hero else "#FFFFFF"
            strk = "#D93829" if is_hero else "#64748B"
            scene.add_rect(sx, sy, 220, 90, bg=bg, stroke=strk, stroke_w=2.0 if is_hero else 1.5, roundness_type=3, frame_id=frame_id)
            scene.add_text(sx + 20, sy + 20, name, font_size=14, font_family=2, color="#0F172A", frame_id=frame_id)
            scene.add_text(sx + 20, sy + 48, sub, font_size=11, font_family=2, color="#64748B", frame_id=frame_id)
        
        # Transitions Forward
        scene.add_arrow(x + 300, y + 215, x + 380, y + 215, stroke="#16A34A", stroke_w=1.5, frame_id=frame_id)
        scene.add_text(x + 310, y + 195, "auth()", font_size=10, font_family=3, color="#16A34A", frame_id=frame_id)

        scene.add_arrow(x + 600, y + 215, x + 720, y + 215, stroke="#16A34A", stroke_w=2.0, frame_id=frame_id)
        scene.add_text(x + 625, y + 195, "capture()", font_size=10, font_family=3, color="#D93829", frame_id=frame_id)

        scene.add_arrow(x + 940, y + 215, x + 1060, y + 215, stroke="#16A34A", stroke_w=1.5, frame_id=frame_id)
        scene.add_text(x + 970, y + 195, "settle()", font_size=10, font_family=3, color="#16A34A", frame_id=frame_id)

        # Fallback Fail State
        scene.add_rect(x + 550, y + 330, 220, 80, bg="#FEF2F2", stroke="#FCA5A5", stroke_w=1.5, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 570, y + 348, "FAILED / VOIDED", font_size=13, font_family=2, color="#991B1B", frame_id=frame_id)
        scene.add_text(x + 570, y + 372, "Reintento o Reversa", font_size=11, font_family=2, color="#7F1D1D", frame_id=frame_id)

        scene.add_arrow(x + 490, y + 260, x + 550, y + 360, stroke="#DC2626", stroke_w=1.2, dashed=True, frame_id=frame_id)
        scene.add_text(x + 460, y + 310, "declined", font_size=10, font_family=3, color="#DC2626", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 05. ER / DATA MODEL (Entities + Fields)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_er_model(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        tables = [
            ("users", x + 60, y + 60, [("id", "UUID [PK]"), ("email", "VARCHAR(255)"), ("full_name", "VARCHAR(120)"), ("created_at", "TIMESTAMP")]),
            ("orders", x + 440, y + 60, [("id", "UUID [PK]"), ("user_id", "UUID [FK]"), ("amount", "DECIMAL(12,2)"), ("status", "VARCHAR(32)"), ("created_at", "TIMESTAMP")]),
            ("payments", x + 840, y + 60, [("id", "UUID [PK]"), ("order_id", "UUID [FK]"), ("processor_tx_id", "VARCHAR(64)"), ("status", "VARCHAR(20)"), ("captured_at", "TIMESTAMP")]),
            ("audit_logs", x + 1200, y + 60, [("id", "BIGINT [PK]"), ("entity_id", "UUID"), ("action", "VARCHAR(50)"), ("payload", "JSONB"), ("timestamp", "TIMESTAMP")])
        ]
        
        for name, tx, ty, fields in tables:
            is_hero = name == "orders"
            tb_w = 280
            tb_h = 45 + len(fields) * 30
            # Header
            head_bg = "#FEE2E2" if is_hero else "#F1F5F9"
            head_strk = "#FCA5A5" if is_hero else "#CBD5E1"
            scene.add_rect(tx, ty, tb_w, tb_h, bg="#FFFFFF", stroke=head_strk, stroke_w=1.5, roundness_type=3, frame_id=frame_id)
            scene.add_rect(tx, ty, tb_w, 35, bg=head_bg, stroke=head_strk, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            scene.add_text(tx + 14, ty + 9, f"TABLE: {name.upper()}", font_size=12, font_family=3, color="#0F172A", frame_id=frame_id)
            
            # Fields
            for idx, (f_name, f_type) in enumerate(fields):
                fy = ty + 45 + idx * 30
                scene.add_text(tx + 14, fy, f_name, font_size=12, font_family=2, color="#0F172A", frame_id=frame_id)
                scene.add_text(tx + 140, fy, f_type, font_size=11, font_family=3, color="#64748B", frame_id=frame_id)
        
        # Relations (Crow's foot connectors)
        scene.add_arrow(x + 340, y + 105, x + 440, y + 135, stroke="#D93829", stroke_w=1.5, frame_id=frame_id)
        scene.add_arrow(x + 720, y + 105, x + 840, y + 135, stroke="#D93829", stroke_w=1.5, frame_id=frame_id)
        scene.add_arrow(x + 1120, y + 105, x + 1200, y + 105, stroke="#94A3B8", stroke_w=1.2, dashed=True, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 06. TIMELINE (Events on an Axis)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_timeline(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        axis_y = y + (h * 0.5)
        # Eje principal continuo
        scene.add_line(x + 60, axis_y, x + w - 60, axis_y, stroke="#0F172A", stroke_w=2.0, frame_id=frame_id)
        
        events = [
            ("Q1 2025", "Arquitectura & Prototipo", "Validación Core y Benchmarks", x + 120, True),
            ("Q2 2025", "MVP Multi-Tenant", "Primeros 10 clientes piloto", x + 420, False),
            ("Q3 2025", "Escala Global (Hero Release)", "Lanzamiento GA & Zero-Downtime", x + 740, True),
            ("Q4 2025", "Expansión Enterprise", "Certificación SOC2 & HIPAA", x + 1060, False),
            ("Q1 2026", "IA Copilot Integrado", "Generación 100% Autónoma", x + 1340, False)
        ]
        
        for date, title, desc, ex, is_hero in events:
            top_align = (ex % 2 == 0)
            box_y = axis_y - 120 if top_align else axis_y + 40
            
            # Punto en eje
            scene.add_ellipse(ex - 8, axis_y - 8, 16, 16, bg="#D93829" if is_hero else "#0F172A", stroke="#FFFFFF", stroke_w=2.0, frame_id=frame_id)
            # Guía vertical
            scene.add_line(ex, axis_y, ex, box_y + (60 if top_align else 0), stroke="#CBD5E1", stroke_w=1.0, dashed=True, frame_id=frame_id)
            
            # Tarjeta de evento
            bg = "#FFF5F2" if is_hero else "#FFFFFF"
            strk = "#D93829" if is_hero else "#CBD5E1"
            scene.add_rect(ex - 100, box_y, 220, 75, bg=bg, stroke=strk, stroke_w=1.5, roundness_type=3, frame_id=frame_id)
            scene.add_text(ex - 85, box_y + 10, date, font_size=11, font_family=3, color="#D93829" if is_hero else "#64748B", frame_id=frame_id)
            scene.add_text(ex - 85, box_y + 28, title, font_size=12, font_family=2, color="#0F172A", frame_id=frame_id)
            scene.add_text(ex - 85, box_y + 48, desc, font_size=10, font_family=2, color="#64748B", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 07. SWIMLANE (Cross-Functional Flow)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_swimlane(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        lanes = ["CLIENT / USER", "SALES & OPS", "ENGINEERING", "FINANCE & BILLING"]
        lane_h = (h - 60) / len(lanes)
        
        for idx, lane in enumerate(lanes):
            ly = y + 30 + idx * lane_h
            # Lane background
            scene.add_rect(x + 40, ly, w - 80, lane_h, bg="#FFFFFF" if idx % 2 == 0 else "#F8FAFC", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id)
            # Header column
            scene.add_rect(x + 40, ly, 180, lane_h, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id)
            scene.add_text(x + 55, ly + (lane_h * 0.5) - 8, lane, font_size=11, font_family=3, color="#475569", frame_id=frame_id)
        
        # Steps inside lanes
        scene.add_quad_card(x + 260, y + 45, 180, 55, "Solicita Cotización", "Formulario Web", badge="STEP 1", icon="user", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 480, y + 130, 200, 55, "Revisión Comercial", "Scoring de Crédito", badge="STEP 2", icon="card", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 720, y + 215, 220, 60, "Aprovisiona Tenant", "K8s Namespace", badge="HERO CORE", icon="server", is_hero=True, frame_id=frame_id)
        scene.add_quad_card(x + 980, y + 300, 200, 55, "Factura Emitida", "Stripe Invoice", badge="STEP 4", icon="card", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 1220, y + 45, 180, 55, "Acceso Concedido", "Notificación Email", badge="DONE", icon="laptop", is_hero=False, frame_id=frame_id)
        
        # Cross-lane Arrows
        scene.add_arrow(x + 440, y + 72, x + 480, y + 155, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 680, y + 155, x + 720, y + 245, stroke="#D93829", stroke_w=1.8, frame_id=frame_id)
        scene.add_arrow(x + 940, y + 245, x + 980, y + 325, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 1180, y + 325, x + 1220, y + 72, stroke="#16A34A", stroke_w=1.8, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 08. QUADRANT (Two-Axis Positioning)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_quadrant(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        cx = x + (w * 0.5)
        cy = y + (h * 0.5)
        
        # 4 Quadrants Background
        scene.add_rect(x + 40, y + 40, (w - 80) * 0.5, (h - 80) * 0.5, bg="#FFF5F2", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id) # Top-Left DO FIRST (Hero)
        scene.add_rect(cx, y + 40, (w - 80) * 0.5, (h - 80) * 0.5, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id) # Top-Right MAJOR
        scene.add_rect(x + 40, cy, (w - 80) * 0.5, (h - 80) * 0.5, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id) # Bottom-Left QUICK
        scene.add_rect(cx, cy, (w - 80) * 0.5, (h - 80) * 0.5, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id) # Bottom-Right THANKLESS
        
        # Main Axes
        scene.add_line(x + 40, cy, x + w - 40, cy, stroke="#0F172A", stroke_w=2.0, frame_id=frame_id)
        scene.add_line(cx, y + 40, cx, y + h - 40, stroke="#0F172A", stroke_w=2.0, frame_id=frame_id)
        
        # Quadrant Labels
        scene.add_text(x + 60, y + 60, "DO FIRST (HIGH IMPACT · LOW EFFORT)", font_size=11, font_family=3, color="#D93829", frame_id=frame_id)
        scene.add_text(cx + 20, y + 60, "MAJOR PROJECTS (HIGH IMPACT · HIGH EFFORT)", font_size=11, font_family=3, color="#475569", frame_id=frame_id)
        scene.add_text(x + 60, cy + 20, "QUICK WINS (LOW IMPACT · LOW EFFORT)", font_size=11, font_family=3, color="#475569", frame_id=frame_id)
        scene.add_text(cx + 20, cy + 20, "THANKLESS TASKS (LOW IMPACT · HIGH EFFORT)", font_size=11, font_family=3, color="#94A3B8", frame_id=frame_id)
        
        # Plotted Data Points
        points = [
            ("Auto-Repair Engine", x + 160, y + 140, True),
            ("SVG High-Fidelity Export", x + 340, y + 180, True),
            ("Kafka Pipeline Migration", cx + 220, y + 130, False),
            ("CI Regression Suite", cx + 450, y + 200, False),
            ("Fix Footer Padding", x + 200, cy + 120, False),
            ("Legacy Script Refactor", cx + 320, cy + 140, False)
        ]
        for label, px, py, is_hero in points:
            col = "#D93829" if is_hero else "#2563EB"
            scene.add_ellipse(px - 6, py - 6, 12, 12, bg=col, stroke="#FFFFFF", stroke_w=1.5, frame_id=frame_id)
            scene.add_text(px + 12, py - 7, label, font_size=11, font_family=2, color="#0F172A", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 09. NESTED (Hierarchy by Containment)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_nested(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        # Nivel 1: Workspace
        scene.add_rect(x + 40, y + 30, w - 80, h - 60, bg="#F8FAFC", stroke="#64748B", stroke_w=1.5, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 60, y + 45, "WORKSPACE ROOT (/Users/sketion-engine)", font_size=12, font_family=3, color="#0F172A", frame_id=frame_id)
        
        # Nivel 2: .agents/ Directory
        scene.add_rect(x + 80, y + 80, w - 160, h - 130, bg="#FFFFFF", stroke="#94A3B8", stroke_w=1.2, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 100, y + 95, "CUSTOMIZATION ROOT (.agents/)", font_size=11, font_family=3, color="#475569", frame_id=frame_id)
        
        # Nivel 3: skills/ Directory
        scene.add_rect(x + 120, y + 130, w - 240, h - 200, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 140, y + 145, "SKILLS BUNDLE (skills/sketion-diagram-design/)", font_size=11, font_family=3, color="#475569", frame_id=frame_id)
        
        # Nivel 4: SKILL.md (Hero Content)
        scene.add_rect(x + 160, y + 180, w - 320, h - 270, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 180, y + 198, "CORE MANIFEST (SKILL.md) — 100% ZERO EMOJIS & STRICT VERTICAL ZONING", font_size=12, font_family=3, color="#D93829", frame_id=frame_id)
        scene.add_text(x + 180, y + 230, "• Composition Core (Frozen) · IA Ranking · Adaptive Rendering · Visual Consistency VCS 97.7", font_size=11, font_family=2, color="#334155", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 10. TREE (Parent -> Children Branching)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_tree(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        cx = x + (w * 0.5)
        # Root Node
        scene.add_quad_card(cx - 150, y + 30, 300, 65, "Sketion Skill Taxonomy", "Root Customization", badge="ROOT", icon="server", is_hero=True, frame_id=frame_id)
        
        # Level 1 Categories
        cats = [
            ("Visual Intelligence", cx - 460),
            ("Layout & Matrix", cx - 50),
            ("Quality & Exporters", cx + 360)
        ]
        for cname, cpx in cats:
            scene.add_rect(cpx - 110, y + 150, 220, 50, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=frame_id)
            scene.add_text(cpx - 90, y + 166, cname, font_size=12, font_family=2, color="#0F172A", frame_id=frame_id)
            # Orthogonal connector from root
            scene.add_line(cx, y + 95, cx, y + 120, stroke="#94A3B8", frame_id=frame_id)
            scene.add_line(cx, y + 120, cpx, y + 120, stroke="#94A3B8", frame_id=frame_id)
            scene.add_arrow(cpx, y + 120, cpx, y + 150, stroke="#94A3B8", frame_id=frame_id)
            
            # Level 2 Leaves
            leaves = ["Module A", "Module B"]
            for l_idx, lf in enumerate(leaves):
                lpx = cpx - 80 + l_idx * 90
                scene.add_rect(lpx - 35, y + 250, 70, 35, bg="#FFFFFF", stroke="#E2E8F0", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
                scene.add_text(lpx - 28, y + 260, lf, font_size=10, font_family=3, color="#64748B", frame_id=frame_id)
                scene.add_arrow(cpx, y + 200, lpx, y + 250, stroke="#CBD5E1", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 11. ORG CHART (Ownership + Routing)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_org_chart(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        cx = x + (w * 0.5)
        # Top Exec
        scene.add_actor_node(cx - 130, y + 30, 260, 65, "Alex Vance", role="VP OF PLATFORM ENGINEERING", icon="user", is_hero=True, frame_id=frame_id)
        
        # Leads
        leads = [
            ("Core Architecture", "LEAD ARCHITECT", cx - 420),
            ("Data Infrastructure", "DATA PLATFORM LEAD", cx),
            ("Security & SRE", "HEAD OF INFRASEC", cx + 420)
        ]
        for lname, lrole, lx in leads:
            scene.add_actor_node(lx - 120, y + 160, 240, 60, lname, role=lrole, icon="user", is_hero=False, frame_id=frame_id)
            scene.add_line(cx, y + 95, cx, y + 130, stroke="#94A3B8", frame_id=frame_id)
            scene.add_line(cx, y + 130, lx, y + 130, stroke="#94A3B8", frame_id=frame_id)
            scene.add_arrow(lx, y + 130, lx, y + 160, stroke="#94A3B8", frame_id=frame_id)
            
            # Pod members
            scene.add_rect(lx - 100, y + 260, 200, 45, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            scene.add_text(lx - 80, y + 274, "Squad Pod (4 Engineers)", font_size=11, font_family=2, color="#475569", frame_id=frame_id)
            scene.add_arrow(lx, y + 220, lx, y + 260, stroke="#CBD5E1", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 12. VENN (Set Overlap)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_venn(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        cx = x + (w * 0.5)
        cy = y + (h * 0.5)
        r = 160.0
        
        # Circle 1: Top (Desirability)
        scene.add_ellipse(cx - r, cy - 140, r * 2, r * 2, bg="transparent", stroke="#0F172A", stroke_w=1.8, frame_id=frame_id)
        scene.add_text(cx - 50, cy - 110, "DESIRABLE\n(People Want It)", font_size=11, font_family=2, color="#0F172A", align="center", frame_id=frame_id)

        # Circle 2: Bottom-Left (Feasibility)
        scene.add_ellipse(cx - r - 80, cy - 30, r * 2, r * 2, bg="transparent", stroke="#0F172A", stroke_w=1.8, frame_id=frame_id)
        scene.add_text(cx - r - 60, cy + 70, "FEASIBLE\n(We Can Build It)", font_size=11, font_family=2, color="#0F172A", align="center", frame_id=frame_id)

        # Circle 3: Bottom-Right (Viability)
        scene.add_ellipse(cx - r + 80, cy - 30, r * 2, r * 2, bg="transparent", stroke="#0F172A", stroke_w=1.8, frame_id=frame_id)
        scene.add_text(cx + 70, cy + 70, "VIABLE\n(Business Succeeds)", font_size=11, font_family=2, color="#0F172A", align="center", frame_id=frame_id)

        # Center Overlap Box (Hero)
        scene.add_rect(cx - 65, cy - 15, 130, 45, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, roundness_type=3, frame_id=frame_id)
        scene.add_text(cx - 50, cy - 2, "SHIPPABLE PRODUCT", font_size=10, font_family=3, color="#D93829", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 13. LAYER STACK (Stacked Abstraction Layers)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_layer_stack(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        layers = [
            ("L5", "UI Surface & Visual Shell", "React 19 · WebGL Canvas · DOM Shaders", False),
            ("L4", "Agent Harness & Reasoning Core", "Intent Parser · Constraint Solver · Tree-of-Thought", True), # Hero
            ("L3", "Prompt Layer & Context Window", "Token Budgeter · Prompt Cache · Embedding Index", False),
            ("L2", "SDK & Client Driver", "Python 3.12 SDK · TypeScript Bridge · REST Proxy", False),
            ("L1", "Model Weights & GPU Backend", "vLLM Cluster · FP8 Quantization · TensorRT-LLM", False)
        ]
        layer_h = (h - 70) / len(layers)
        
        for idx, (tier, title, sub, is_hero) in enumerate(layers):
            ly = y + 35 + idx * layer_h
            bg = "#FFF5F2" if is_hero else "#FFFFFF"
            strk = "#D93829" if is_hero else "#CBD5E1"
            scene.add_rect(x + 60, ly, w - 120, layer_h - 10, bg=bg, stroke=strk, stroke_w=2.0 if is_hero else 1.2, roundness_type=3, frame_id=frame_id)
            
            # Tier Badge
            scene.add_rect(x + 75, ly + 8, 40, 24, bg="#FEE2E2" if is_hero else "#F1F5F9", stroke=strk, stroke_w=1.0, roundness_type=3, frame_id=frame_id)
            scene.add_text(x + 85, ly + 13, tier, font_size=11, font_family=3, color="#D93829" if is_hero else "#475569", frame_id=frame_id)
            
            scene.add_text(x + 130, ly + 12, title.upper(), font_size=13, font_family=2, color="#0F172A", frame_id=frame_id)
            scene.add_text(x + w - 460, ly + 14, sub, font_size=11, font_family=3, color="#64748B", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 14. PYRAMID / FUNNEL (Ranked Hierarchy Slices)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_pyramid_funnel(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        cx = x + (w * 0.5)
        slices = [
            ("4. FLAGSHIP ASSET", "1 Producto de Alto Impacto (Apex)", 280, True),
            ("3. LONG-FORM GUIDES", "12 Guías Técnicas de Arquitectura", 460, False),
            ("2. DEEP-DIVE ESSAYS", "85 Ensayos de Ingeniería", 680, False),
            ("1. SHORT POSTS & SNIPPETS", "1,200 Micro-Publicaciones (Base)", 920, False)
        ]
        slice_h = (h - 70) / len(slices)
        
        for idx, (tier, desc, sw, is_hero) in enumerate(slices):
            sy = y + 35 + idx * slice_h
            bg = "#FFF5F2" if is_hero else "#FFFFFF"
            strk = "#D93829" if is_hero else "#CBD5E1"
            scene.add_rect(cx - (sw * 0.5), sy, sw, slice_h - 10, bg=bg, stroke=strk, stroke_w=2.0 if is_hero else 1.2, roundness_type=3, frame_id=frame_id)
            scene.add_text(cx - (sw * 0.5) + 20, sy + 12, tier, font_size=12, font_family=3, color="#D93829" if is_hero else "#0F172A", frame_id=frame_id)
            scene.add_text(cx + (sw * 0.5) - 240, sy + 14, desc, font_size=11, font_family=2, color="#64748B", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 15. CONSULTANT 2X2 (Scenario Matrix · Named Cells)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_consultant_2x2(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        cell_w = (w - 120) * 0.5
        cell_h = (h - 90) * 0.5
        
        cells = [
            ("DISTRIBUTED HUMANS", "Async-first, global hiring.\nSaaS-heavy, human-centric workflows.\nLow automation leverage.", x + 50, y + 40, False),
            ("AGENT TEAMS (HERO TARGET)", "Autonomous AI agents execute.\nHumans steer and audit outcomes.\nUltra-high leverage per seat.", x + 70 + cell_w, y + 40, True),
            ("OFFICE CLASSIC", "Co-located physical desks.\nManual paper and sync meetings.\nLegacy operations baseline.", x + 50, y + 55 + cell_h, False),
            ("IN-PERSON + AI ASSISTANTS", "Smart offices with edge compute.\nHybrid workforce model.\nHigh tooling cost.", x + 70 + cell_w, y + 55 + cell_h, False)
        ]
        for title, body, cx, cy, is_hero in cells:
            bg = "#FFF5F2" if is_hero else "#FFFFFF"
            strk = "#D93829" if is_hero else "#CBD5E1"
            scene.add_rect(cx, cy, cell_w, cell_h, bg=bg, stroke=strk, stroke_w=2.0 if is_hero else 1.2, roundness_type=3, frame_id=frame_id)
            scene.add_text(cx + 20, cy + 18, title, font_size=13, font_family=3, color="#D93829" if is_hero else "#0F172A", frame_id=frame_id)
            scene.add_text(cx + 20, cy + 50, body, font_size=11, font_family=2, color="#475569", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 16. RADAR / SPIDER (Multi-Axis Comparison)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_radar_spider(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        cx = x + (w * 0.5)
        cy = y + (h * 0.5)
        axes = ["LATENCY", "THROUGHPUT", "RESILIENCE", "SECURITY", "SIMPLICITY"]
        rad = 140.0
        
        # Draw 3 Concentric Polygons
        for r_factor in [0.33, 0.66, 1.0]:
            poly_rad = rad * r_factor
            for i in range(len(axes)):
                a1 = (i * 2 * math.pi / len(axes)) - (math.pi / 2)
                a2 = ((i + 1) * 2 * math.pi / len(axes)) - (math.pi / 2)
                x1, y1 = cx + poly_rad * math.cos(a1), cy + poly_rad * math.sin(a1)
                x2, y2 = cx + poly_rad * math.cos(a2), cy + poly_rad * math.sin(a2)
                scene.add_line(x1, y1, x2, y2, stroke="#CBD5E1", stroke_w=1.0, dashed=True, frame_id=frame_id)
        
        # Radial Spoke Lines & Labels
        for i, ax_name in enumerate(axes):
            angle = (i * 2 * math.pi / len(axes)) - (math.pi / 2)
            spoke_x = cx + rad * math.cos(angle)
            spoke_y = cy + rad * math.sin(angle)
            scene.add_line(cx, cy, spoke_x, spoke_y, stroke="#94A3B8", stroke_w=1.2, frame_id=frame_id)
            lx = cx + (rad + 30) * math.cos(angle) - 30
            ly = cy + (rad + 20) * math.sin(angle) - 8
            scene.add_text(lx, ly, ax_name, font_size=11, font_family=3, color="#0F172A", frame_id=frame_id)
            
        # Target System Overlay Polygon (Hero)
        scores = [0.95, 0.90, 0.85, 0.98, 0.80]
        poly_pts = []
        for i, sc in enumerate(scores):
            angle = (i * 2 * math.pi / len(axes)) - (math.pi / 2)
            poly_pts.append((cx + (rad * sc) * math.cos(angle), cy + (rad * sc) * math.sin(angle)))
        for i in range(len(poly_pts)):
            p1 = poly_pts[i]
            p2 = poly_pts[(i + 1) % len(poly_pts)]
            scene.add_line(p1[0], p1[1], p2[0], p2[1], stroke="#D93829", stroke_w=2.2, frame_id=frame_id)
            scene.add_ellipse(p1[0] - 4, p1[1] - 4, 8, 8, bg="#D93829", stroke="#FFFFFF", stroke_w=1.5, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 17. LOOP / FLYWHEEL (Stations Around a Hub)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_loop_flywheel(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        cx = x + (w * 0.5)
        cy = y + (h * 0.5)
        
        # Center Hub
        scene.add_quad_card(cx - 120, cy - 50, 240, 100, "Core Flywheel Engine", "Self-Reinforcing Growth", badge="ENGINE", icon="server", is_hero=True, frame_id=frame_id)
        
        stations = [
            ("1. Freemium Inbound", "Viral Organic Acquisition", cx, cy - 170),
            ("2. Fast Time-to-Value", "Interactive Onboarding", cx + 360, cy),
            ("3. Paid Expansion", "Stripe Self-Serve Upgrades", cx, cy + 170),
            ("4. Multi-Seat Advocacy", "Word-of-Mouth Referral", cx - 360, cy)
        ]
        for name, sub, sx, sy in stations:
            scene.add_quad_card(sx - 110, sy - 40, 220, 80, name, sub, badge="STATION", icon="laptop", is_hero=False, frame_id=frame_id)
        
        # Circular Perimeter Connectors
        scene.add_arrow(cx + 120, cy - 140, cx + 240, cy - 50, stroke="#D93829", stroke_w=1.8, frame_id=frame_id)
        scene.add_arrow(cx + 240, cy + 50, cx + 120, cy + 140, stroke="#D93829", stroke_w=1.8, frame_id=frame_id)
        scene.add_arrow(cx - 120, cy + 140, cx - 240, cy + 50, stroke="#D93829", stroke_w=1.8, frame_id=frame_id)
        scene.add_arrow(cx - 240, cy - 50, cx - 120, cy - 140, stroke="#D93829", stroke_w=1.8, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 18. IT CURRENT-STATE (Legacy vs Target Modernization)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_it_current_state(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        half_w = (w - 120) * 0.5
        # Legacy Landscape Box
        scene.add_rect(x + 40, y + 40, half_w, h - 80, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 60, y + 60, "LEGACY AS-IS LANDSCAPE (2020)", font_size=13, font_family=3, color="#991B1B", frame_id=frame_id)
        scene.add_quad_card(x + 60, y + 100, 220, 75, "PHP Monolith (v5.6)", "Spaghetti Codebase", badge="LEGACY", icon="server", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 60, y + 190, 220, 75, "Single MySQL Instance", "Table Locks in High Concurrency", badge="SPOF", icon="database", is_hero=False, frame_id=frame_id)
        
        # Target Modernization Box
        rx = x + 80 + half_w
        scene.add_rect(rx, y + 40, half_w, h - 80, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, roundness_type=3, frame_id=frame_id)
        scene.add_text(rx + 20, y + 60, "TARGET TO-BE CLOUD-NATIVE (2026)", font_size=13, font_family=3, color="#D93829", frame_id=frame_id)
        scene.add_quad_card(rx + 20, y + 100, 260, 75, "Kubernetes EKS Cluster", "Autonomous Microservices", badge="CLOUD-NATIVE", icon="server", is_hero=True, frame_id=frame_id)
        scene.add_database_cylinder(rx + 20, y + 190, 260, 110, "Aurora Multi-AZ DB", "ACID Replication & Auto-Failover", badge="ACID DB", is_hero=False, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 19. GANTT (Tasks and Phases on a Timeline)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_gantt(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        months = ["APRIL (W1-W4)", "MAY (W5-W8)", "JUNE (W9-W12)"]
        col_w = (w - 300) / 3.0
        
        # Header Months
        for m_idx, m_name in enumerate(months):
            mx = x + 240 + m_idx * col_w
            scene.add_rect(mx, y + 30, col_w, 35, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id)
            scene.add_text(mx + 20, y + 42, m_name, font_size=11, font_family=3, color="#475569", frame_id=frame_id)
            # Grid vertical lines
            scene.add_line(mx, y + 65, mx, y + h - 30, stroke="#E2E8F0", stroke_w=1.0, dashed=True, frame_id=frame_id)
        
        tasks = [
            ("Discovery & Spec", 0.0, 1.2, False),
            ("Core Engine Build", 0.8, 2.0, True), # Hero task
            ("Regression & CI", 1.8, 2.6, False),
            ("General Availability (GA)", 2.4, 3.0, True)
        ]
        row_h = (h - 100) / len(tasks)
        for idx, (tname, start_u, end_u, is_hero) in enumerate(tasks):
            ty = y + 80 + idx * row_h
            scene.add_text(x + 40, ty + 8, tname, font_size=12, font_family=2, color="#0F172A", frame_id=frame_id)
            
            # Bar span
            bx = x + 240 + start_u * col_w
            bw = (end_u - start_u) * col_w
            bg = "#FFF5F2" if is_hero else "#EFF6FF"
            strk = "#D93829" if is_hero else "#2563EB"
            scene.add_rect(bx, ty, bw, 28, bg=bg, stroke=strk, stroke_w=1.5, roundness_type=3, frame_id=frame_id)
            scene.add_text(bx + 10, ty + 6, f"{int((end_u-start_u)*4)} Semanas", font_size=10, font_family=3, color=strk, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 20. SCATTER PLOT (Distribution and Correlation)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_scatter_plot(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        ox = x + 80
        oy = y + h - 60
        plot_w = w - 160
        plot_h = h - 120
        
        # Axes
        scene.add_line(ox, oy, ox + plot_w, oy, stroke="#0F172A", stroke_w=1.8, frame_id=frame_id) # X Axis
        scene.add_line(ox, oy, ox, oy - plot_h, stroke="#0F172A", stroke_w=1.8, frame_id=frame_id) # Y Axis
        scene.add_text(ox + (plot_w * 0.5) - 60, oy + 20, "THROUGHPUT (REQS / SEC)", font_size=11, font_family=3, color="#475569", frame_id=frame_id)
        scene.add_text(ox - 60, oy - (plot_h * 0.5), "P99 LATENCY", font_size=11, font_family=3, color="#475569", frame_id=frame_id)
        
        # Dotted Trendline
        scene.add_line(ox + 40, oy - plot_h + 30, ox + plot_w - 40, oy - 40, stroke="#94A3B8", stroke_w=1.5, dashed=True, frame_id=frame_id)
        
        # Points
        data = [
            (ox + 60, oy - plot_h + 50, "Node 1", False),
            (ox + 160, oy - plot_h + 120, "Node 2", False),
            (ox + 300, oy - plot_h + 180, "Node 3", False),
            (ox + 460, oy - plot_h + 230, "Optimized Core (Hero)", True),
            (ox + 620, oy - plot_h + 290, "Node 5", False),
            (ox + 780, oy - plot_h + 330, "Edge Target", True)
        ]
        for px, py, label, is_hero in data:
            col = "#D93829" if is_hero else "#2563EB"
            scene.add_ellipse(px - 6, py - 6, 12, 12, bg=col, stroke="#FFFFFF", stroke_w=1.5, frame_id=frame_id)
            scene.add_text(px + 10, py - 8, label, font_size=10, font_family=3, color="#0F172A", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 21. PROCESS (Multi-Actor Sequential Workflow)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_process(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        steps = [
            ("1. RECEIVE ORDER", "Webhook Ingest", x + 50),
            ("2. VERIFY FRAUD", "Risk Engine", x + 340),
            ("3. SAGA LOCK", "ACID Hold", x + 630),
            ("4. CAPTURE FUNDS", "Stripe API", x + 920),
            ("5. DISPATCH", "Warehouse Event", x + 1210)
        ]
        for idx, (title, sub, sx) in enumerate(steps):
            is_hero = idx == 2
            scene.add_quad_card(sx, y + 140, 220, 95, title, sub, badge=f"STAGE {idx+1}", icon="server", is_hero=is_hero, frame_id=frame_id)
            if idx < len(steps) - 1:
                scene.add_arrow(sx + 220, y + 187, steps[idx+1][2], y + 187, stroke="#D93829" if is_hero else "#94A3B8", stroke_w=2.0 if is_hero else 1.5, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 22. MEDALLION (Multi-Tier Data Storage)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_medallion(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        tiers = [
            ("1. RAW LANDING", "Bronze S3 Bucket", "Raw Unstructured Logs", x + 50),
            ("2. CLEAN & MASK", "Silver Delta Table", "De-Identified Records", x + 340),
            ("3. STAGING", "Silver Parquet", "Aggregated Dimensions", x + 630),
            ("4. AGGREGATED", "Gold ClickHouse OLAP", "Business Marts & KPIs", x + 920),
            ("5. ARCHIVE", "Cold WORM Store", "7-Year Retention Policy", x + 1210)
        ]
        for idx, (tname, tengine, tdesc, tx) in enumerate(tiers):
            is_hero = idx == 3
            scene.add_database_cylinder(tx, y + 140, 240, 125, tengine, tdesc, badge=f"MEDALLION {idx+1}", is_hero=is_hero, frame_id=frame_id)
            if idx < len(tiers) - 1:
                # Arched connector on top
                scene.add_arrow(tx + 240, y + 180, tiers[idx+1][3], y + 180, stroke="#D93829" if is_hero else "#94A3B8", stroke_w=1.8, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 23. DATA FLOW (Role-Scoped Pipeline Steps)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_data_flow(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        # Role 1: Data Engineer
        scene.add_rect(x + 40, y + 40, w - 80, 110, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id)
        scene.add_text(x + 55, y + 55, "ROLE: DATA ENGINEER", font_size=11, font_family=3, color="#475569", frame_id=frame_id)
        scene.add_quad_card(x + 220, y + 50, 220, 80, "Capture Events", "Kafka Ingest", badge="INGEST", icon="stream", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 500, y + 50, 220, 80, "Land Records", "S3 Storage", badge="RAW STORE", icon="database", is_hero=False, frame_id=frame_id)
        
        # Role 2: Data Scientist (Hero)
        scene.add_rect(x + 40, y + 170, w - 80, 110, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, frame_id=frame_id)
        scene.add_text(x + 55, y + 185, "ROLE: DATA SCIENTIST", font_size=11, font_family=3, color="#D93829", frame_id=frame_id)
        scene.add_quad_card(x + 500, y + 180, 260, 85, "Clean & Feature Engineering", "Feature Store & PySpark", badge="HERO CORE", icon="server", is_hero=True, frame_id=frame_id)
        scene.add_quad_card(x + 820, y + 180, 220, 85, "Train Model", "vLLM Checkpoint", badge="MODEL", icon="server", is_hero=False, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 24. DP INTEGRATION (Sources -> Core -> Consumers)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_dp_integration(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        # 1. Sources
        scene.add_quad_card(x + 50, y + 80, 200, 75, "CRM & ERP Feeds", "Daily Batch Sync", badge="SOURCE", icon="server", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 50, y + 180, 200, 75, "POS Transactions", "Real-time MQTT", badge="SOURCE", icon="card", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 50, y + 280, 200, 75, "Event Stream", "Kafka Backbone", badge="SOURCE", icon="stream", is_hero=False, frame_id=frame_id)
        
        # 2. Core Platform Box (Hero)
        scene.add_rect(x + 330, y + 40, 520, h - 80, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 350, y + 58, "CENTRAL DATA PLATFORM CORE", font_size=12, font_family=3, color="#D93829", frame_id=frame_id)
        scene.add_database_cylinder(x + 360, y + 95, 200, 110, "Object Lakehouse", "Parquet Store", badge="LAKE", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 600, y + 95, 220, 110, "Query Engine", "Trino / Presto SQL", badge="QUERY CORE", icon="server", is_hero=True, frame_id=frame_id)
        
        # 3. Consumers
        scene.add_quad_card(x + 940, y + 80, 220, 75, "BI Executive Dashboards", "Superset & Tableau", badge="CONSUMER", icon="laptop", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 940, y + 180, 220, 75, "Realtime Fraud AI", "Inference Microservice", badge="CONSUMER", icon="server", is_hero=False, frame_id=frame_id)
        scene.add_quad_card(x + 940, y + 280, 220, 75, "Partner APIs", "REST / GraphQL Gateway", badge="CONSUMER", icon="gateway", is_hero=False, frame_id=frame_id)
        
        # Connectors
        scene.add_arrow(x + 250, y + 117, x + 360, y + 145, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 250, y + 217, x + 360, y + 145, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 820, y + 150, x + 940, y + 117, stroke="#D93829", stroke_w=1.8, frame_id=frame_id)
        scene.add_arrow(x + 820, y + 150, x + 940, y + 217, stroke="#D93829", stroke_w=1.8, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 25. DP SECURITY MATRIX (Per-Role Access Permissions)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_dp_security_matrix(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        headers = ["COMPONENTS", "DATA ENGINEER", "DATA SCIENTIST", "ANALYST", "ADMINISTRATOR", "EXTERNAL PARTNER"]
        rows = [
            ("Object Storage (S3)", ["Write", "Read", "None", "Admin", "None"]),
            ("Query Engine (Trino)", ["Write", "Write", "Read", "Admin", "Read"]),
            ("Notebooks (Jupyter)", ["Read", "Write", "None", "Admin", "None"]),
            ("BI Tool (Superset)", ["Read", "Write", "Write", "Admin", "Read"]),
            ("Orchestrator (Airflow)", ["Admin", "None", "None", "Admin", "None"])
        ]
        
        col_w = (w - 80) / len(headers)
        row_h = (h - 70) / (len(rows) + 1)
        
        # Header Row
        for c_idx, head in enumerate(headers):
            cx = x + 40 + c_idx * col_w
            scene.add_rect(cx, y + 30, col_w, row_h, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id)
            scene.add_text(cx + 10, y + 42, head, font_size=10, font_family=3, color="#0F172A", frame_id=frame_id)
        
        # Matrix Rows
        for r_idx, (comp_name, perms) in enumerate(rows):
            ry = y + 30 + (r_idx + 1) * row_h
            # Component Name
            scene.add_rect(x + 40, ry, col_w, row_h, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.0, frame_id=frame_id)
            scene.add_text(x + 50, ry + 12, comp_name, font_size=11, font_family=2, color="#0F172A", frame_id=frame_id)
            
            # Permission Chips
            for p_idx, perm in enumerate(perms):
                px = x + 40 + (p_idx + 1) * col_w
                is_admin = perm == "Admin"
                is_write = perm == "Write"
                is_read = perm == "Read"
                
                chip_bg = "#FEE2E2" if is_admin else ("#EFF6FF" if is_write else ("#F0FDF4" if is_read else "#F8FAFC"))
                chip_col = "#991B1B" if is_admin else ("#1D4ED8" if is_write else ("#166534" if is_read else "#94A3B8"))
                
                scene.add_rect(px, ry, col_w, row_h, bg="#FFFFFF", stroke="#E2E8F0", stroke_w=1.0, frame_id=frame_id)
                scene.add_rect(px + 14, ry + 8, col_w - 28, row_h - 16, bg=chip_bg, stroke=chip_bg, roundness_type=3, frame_id=frame_id)
                scene.add_text(px + 28, ry + 12, perm, font_size=10, font_family=3, color=chip_col, frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 26. VALUE CHAIN (Porter Enterprise Flow)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_value_chain(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        stages = [
            ("1. INBOUND", "Sourcing & Raw Logistics", x + 50),
            ("2. OPERATIONS", "Automated Assembly Core", x + 300),
            ("3. OUTBOUND", "Fleet Realtime Dispatch", x + 550),
            ("4. MARKETING", "Omnichannel Growth", x + 800),
            ("5. SERVICE", "24/7 SLA Resolution", x + 1050)
        ]
        for idx, (title, sub, sx) in enumerate(stages):
            is_hero = idx == 1
            scene.add_quad_card(sx, y + 120, 220, 110, title, sub, badge="VALUE TIER", icon="server", is_hero=is_hero, frame_id=frame_id)
            if idx < len(stages) - 1:
                scene.add_arrow(sx + 220, y + 175, stages[idx+1][2], y + 175, stroke="#D93829" if is_hero else "#94A3B8", stroke_w=1.8, frame_id=frame_id)
        
        # Final Chevron Margin Box
        scene.add_rect(x + 1300, y + 90, 140, 170, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 1325, y + 160, "MARGIN (PROFIT)", font_size=11, font_family=3, color="#D93829", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # 27. HIGH-LEVEL (End-to-End Stack on a Cluster)
    # -----------------------------------------------------------------------------------------------
    @staticmethod
    def render_high_level(scene: ExcalidrawScene, x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        # Ingress
        scene.add_quad_card(x + 50, y + 120, 220, 110, "Global Ingress Gateway", "Edge TLS & WAF Shield", badge="INGRESS", icon="gateway", is_hero=False, frame_id=frame_id)
        
        # Central Kubernetes Cluster (Hero)
        scene.add_rect(x + 330, y + 40, 680, h - 80, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, stroke_style="dashed", roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 350, y + 60, "KUBERNETES CONTAINER CLUSTER (EKS MULTI-AZ)", font_size=12, font_family=3, color="#D93829", frame_id=frame_id)
        scene.add_quad_card(x + 360, y + 100, 280, 120, "Saga Payment Orchestrator", "Distributed State Machine", badge="HERO CORE", icon="server", is_hero=True, frame_id=frame_id)
        scene.add_quad_card(x + 680, y + 100, 280, 120, "Risk Scoring Worker", "Machine Learning Scoring", badge="WORKER", icon="server", is_hero=False, frame_id=frame_id)
        
        # External Integrations
        scene.add_database_cylinder(x + 1070, y + 100, 240, 120, "Aurora PostgreSQL", "Primary ACID Storage", badge="DATABASE", is_hero=False, frame_id=frame_id)
        scene.add_arrow(x + 270, y + 175, x + 360, y + 160, stroke="#94A3B8", frame_id=frame_id)
        scene.add_arrow(x + 640, y + 160, x + 680, y + 160, stroke="#D93829", stroke_w=1.8, frame_id=frame_id)
        scene.add_arrow(x + 960, y + 160, x + 1070, y + 160, stroke="#94A3B8", frame_id=frame_id)

    # -----------------------------------------------------------------------------------------------
    # DISPATCHER & CLASSIFIER UNIFICADO DE LOS 27 TIPOS
    # -----------------------------------------------------------------------------------------------
    @classmethod
    def classify_intent(cls, text: str) -> VisualType27:
        """Clasifica el texto / prompt de entrada en uno de los 27 tipos canónicos."""
        t = text.lower()
        if any(w in t for w in ["sequence", "messages", "lifeline", "interacción"]):
            return VisualType27.SEQUENCE
        elif any(w in t for w in ["state machine", "transición", "states", "finitos", "transiciones"]):
            return VisualType27.STATE_MACHINE
        elif any(w in t for w in ["er", "entity", "relational", "schema", "tablas", "data model"]):
            return VisualType27.ER_DATA_MODEL
        elif any(w in t for w in ["timeline", "hitos", "events on axis", "cronología"]):
            return VisualType27.TIMELINE
        elif any(w in t for w in ["swimlane", "carriles", "cross-functional", "handoff"]):
            return VisualType27.SWIMLANE
        elif any(w in t for w in ["quadrant", "2x2", "cuadrantes", "impact vs effort"]):
            return VisualType27.QUADRANT
        elif any(w in t for w in ["nested", "containment", "claude.md", "anidado"]):
            return VisualType27.NESTED
        elif any(w in t for w in ["tree", "taxonomy", "árbol", "parent", "children"]):
            return VisualType27.TREE
        elif any(w in t for w in ["org chart", "organigrama", "ownership", "routing tree"]):
            return VisualType27.ORG_CHART
        elif any(w in t for w in ["venn", "intersección", "overlap", "conjuntos"]):
            return VisualType27.VENN
        elif any(w in t for w in ["layer stack", "pila", "abstraction layers", "stack"]):
            return VisualType27.LAYER_STACK
        elif any(w in t for w in ["pyramid", "funnel", "pirámide", "embudo", "drop-off"]):
            return VisualType27.PYRAMID_FUNNEL
        elif any(w in t for w in ["consultant", "scenario matrix", "named cells"]):
            return VisualType27.CONSULTANT_2X2
        elif any(w in t for w in ["radar", "spider", "polar", "multiaxial"]):
            return VisualType27.RADAR_SPIDER
        elif any(w in t for w in ["loop", "flywheel", "growth loop", "estaciones"]):
            return VisualType27.LOOP_FLYWHEEL
        elif any(w in t for w in ["it current", "legacy", "modernization", "as-is", "to-be"]):
            return VisualType27.IT_CURRENT_STATE
        elif any(w in t for w in ["gantt", "schedule", "cronograma", "semanas", "tareas"]):
            return VisualType27.GANTT
        elif any(w in t for w in ["scatter", "dispersión", "correlation", "distribución"]):
            return VisualType27.SCATTER_PLOT
        elif any(w in t for w in ["medallion", "lakehouse", "bronze", "silver", "gold"]):
            return VisualType27.MEDALLION
        elif any(w in t for w in ["data flow", "role-scoped", "pipeline steps"]):
            return VisualType27.DATA_FLOW
        elif any(w in t for w in ["dp integration", "sources", "consumers"]):
            return VisualType27.DP_INTEGRATION
        elif any(w in t for w in ["security matrix", "permissions", "rbac", "access matrix"]):
            return VisualType27.DP_SECURITY_MATRIX
        elif any(w in t for w in ["value chain", "porter", "cadena de valor", "margin"]):
            return VisualType27.VALUE_CHAIN
        elif any(w in t for w in ["flowchart", "decision", "bifurcación", "if else"]):
            return VisualType27.FLOWCHART
        elif any(w in t for w in ["process", "workflow", "proceso"]):
            return VisualType27.PROCESS
        elif any(w in t for w in ["high-level", "high level", "cluster", "platform"]):
            return VisualType27.HIGH_LEVEL
        else:
            return VisualType27.ARCHITECTURE

    @classmethod
    def render_by_type(cls, scene: ExcalidrawScene, visual_type: Union[str, VisualType27],
                       x: float, y: float, w: float, h: float, frame_id: Optional[str] = None):
        """Despacha la ejecución al renderizador geométrico correspondiente de los 27 tipos."""
        vt = visual_type if isinstance(visual_type, VisualType27) else VisualType27(visual_type.lower())
        
        dispatch_map = {
            VisualType27.ARCHITECTURE: cls.render_architecture,
            VisualType27.FLOWCHART: cls.render_flowchart,
            VisualType27.SEQUENCE: cls.render_sequence,
            VisualType27.STATE_MACHINE: cls.render_state_machine,
            VisualType27.ER_DATA_MODEL: cls.render_er_model,
            VisualType27.TIMELINE: cls.render_timeline,
            VisualType27.SWIMLANE: cls.render_swimlane,
            VisualType27.QUADRANT: cls.render_quadrant,
            VisualType27.NESTED: cls.render_nested,
            VisualType27.TREE: cls.render_tree,
            VisualType27.ORG_CHART: cls.render_org_chart,
            VisualType27.VENN: cls.render_venn,
            VisualType27.LAYER_STACK: cls.render_layer_stack,
            VisualType27.PYRAMID_FUNNEL: cls.render_pyramid_funnel,
            VisualType27.CONSULTANT_2X2: cls.render_consultant_2x2,
            VisualType27.RADAR_SPIDER: cls.render_radar_spider,
            VisualType27.LOOP_FLYWHEEL: cls.render_loop_flywheel,
            VisualType27.IT_CURRENT_STATE: cls.render_it_current_state,
            VisualType27.HIGH_LEVEL: cls.render_high_level,
            VisualType27.GANTT: cls.render_gantt,
            VisualType27.SCATTER_PLOT: cls.render_scatter_plot,
            VisualType27.PROCESS: cls.render_process,
            VisualType27.MEDALLION: cls.render_medallion,
            VisualType27.DATA_FLOW: cls.render_data_flow,
            VisualType27.DP_INTEGRATION: cls.render_dp_integration,
            VisualType27.DP_SECURITY_MATRIX: cls.render_dp_security_matrix,
            VisualType27.VALUE_CHAIN: cls.render_value_chain
        }
        fn = dispatch_map.get(vt, cls.render_architecture)
        fn(scene, x, y, w, h, frame_id=frame_id)

