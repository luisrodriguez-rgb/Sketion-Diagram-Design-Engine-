"""
Generador de Categoría 03: Software Architecture (20 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 03: Software Architecture (20 plantillas) ---")
    cat = "03_software_architecture"

    # 41. C4 System Context
    s, fid, tw, th = create_base_scene("C4 Model Level 1: System Context Diagram", "SOFTWARE")
    s.add_actor_node(40, 180, 180, 75, "Cliente de Banco", "Usuario Personal", frame_id=fid)
    s.add_arrow(220, 215, 340, 215, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_quad_card(340, 140, 360, 150, "SISTEMA BANCARIO DIGITAL", "Permite consultar saldos, realizar transferencias y pagos en linea.", badge="CORE SYSTEM", is_hero=True, frame_id=fid)
    s.add_arrow(700, 180, 840, 140, stroke="#94A3B8", stroke_w=1.5, frame_id=fid)
    s.add_arrow(700, 250, 840, 290, stroke="#94A3B8", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(840, 90, 280, 100, "Mainframe Bancario", "Sistema Legacy de Cuentas", badge="EXTERNAL", frame_id=fid)
    s.add_quad_card(840, 240, 280, 100, "Servicio de Notificaciones", "Amazon SES / Twilio SMS", badge="EXTERNAL", frame_id=fid)
    save_and_export(s, fid, cat, 41, "41_c4_system_context", "C4 System Context", "high", "c4_context", ["systems", "actors", "boundaries"])

    # 42. C4 Container Diagram
    s, fid, tw, th = create_base_scene("C4 Model Level 2: Container Diagram", "SOFTWARE")
    s.add_quad_card(40, 160, 220, 110, "Single Page App", "React 19 / TypeScript\nNavegador Web", badge="SPA", frame_id=fid)
    s.add_arrow(260, 215, 360, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(360, 140, 260, 150, "API Gateway / Backend", "FastAPI / Python 3.12\nJSON / HTTPS REST", badge="CONTAINER", is_hero=True, frame_id=fid)
    s.add_arrow(620, 215, 740, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_database_cylinder(740, 140, 240, 150, "PostgreSQL Database", "Almacena transacciones y saldos\nSQL / Puerto 5432", frame_id=fid)
    s.add_arrow(620, 270, 1080, 215, stroke="#94A3B8", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(1080, 160, 240, 110, "Redis Cache", "Sesiones y rate limiting", badge="IN-MEMORY", frame_id=fid)
    save_and_export(s, fid, cat, 42, "42_c4_container_diagram", "C4 Container Diagram", "high", "c4_container", ["containers", "dbs", "protocols"])

    # 43. C4 Component Diagram
    s, fid, tw, th = create_base_scene("C4 Model Level 3: Component Diagram (Order Service)", "SOFTWARE")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#0F172A", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "CONTENEDOR: ORDER SERVICE (FASTAPI RUNTIME)", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_quad_card(80, 160, 260, 120, "Order Controller", "Maneja endpoints HTTP REST\nValida payloads Pydantic", badge="CONTROLLER", frame_id=fid)
    s.add_arrow(340, 220, 440, 220, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(440, 140, 300, 160, "Order Core Service", "Aplica logica de negocio y estado\nCalcula impuestos y descuentos", badge="SERVICE", is_hero=True, frame_id=fid)
    s.add_arrow(740, 190, 860, 150, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(740, 250, 860, 290, stroke="#94A3B8", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(860, 100, 280, 110, "Payment Gateway Client", "Llama a Stripe API via HTTPS", badge="ADAPTER", frame_id=fid)
    s.add_quad_card(860, 240, 280, 110, "Order Repository", "Persistencia SQL en PostgreSQL", badge="REPOSITORY", frame_id=fid)
    save_and_export(s, fid, cat, 43, "43_c4_component_diagram", "C4 Component Diagram", "high", "c4_component", ["controllers", "services", "repos"])

    # 44. Deployment Diagram
    s, fid, tw, th = create_base_scene("UML Deployment Architecture & Nodes", "SOFTWARE")
    s.add_rect(40, 80, 320, 350, bg="#F8FAFC", stroke="#0F172A", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "NODO: CLIENTE (BROWSER)", font_size=11, font_family=3, color="#0F172A", frame_id=fid)
    s.add_rect(60, 150, 280, 80, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=fid)
    s.add_text(75, 175, "<<artifact>> WebApp.bundle.js", font_size=10, font_family=3, color="#334155", frame_id=fid)
    s.add_arrow(360, 220, 480, 220, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_rect(480, 80, 460, 350, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(500, 105, "NODO: AWS EC2 APPLICATION SERVER", font_size=11, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_rect(500, 150, 420, 100, bg="#FFFFFF", stroke="#3B82F6", stroke_w=1.2, roundness_type=3, frame_id=fid)
    s.add_text(515, 175, "<<execution environment>> Docker Daemon", font_size=10, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_text(515, 205, "Contenedor: api-server:v2.4 (Gunicorn)", font_size=9, font_family=3, color="#64748B", frame_id=fid)
    s.add_arrow(940, 220, 1040, 220, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_database_cylinder(1040, 140, 320, 180, "NODO: AWS RDS POSTGRESQL", "Multi-AZ Replication", frame_id=fid)
    save_and_export(s, fid, cat, 44, "44_deployment_diagram", "Deployment Diagram", "high", "deployment_nodes", ["client_node", "server_node", "db_node"])

    # 45. Component Architecture (Hexagonal Architecture)
    s, fid, tw, th = create_base_scene("Ports & Adapters (Hexagonal Component Architecture)", "SOFTWARE")
    s.add_quad_card(40, 160, 240, 110, "Inbound Adapter", "REST Controller / GraphQL", badge="ADAPTER", frame_id=fid)
    s.add_arrow(280, 215, 380, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_rect(380, 80, 560, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, roundness_type=3, frame_id=fid)
    s.add_text(400, 105, "CORE DE DOMINIO & PUERTOS (HEXAGONO)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_quad_card(410, 150, 240, 110, "Inbound Port", "OrderUseCaseInterface", badge="PORT", frame_id=fid)
    s.add_quad_card(680, 150, 240, 110, "Outbound Port", "OrderRepositoryPort", badge="PORT", frame_id=fid)
    s.add_arrow(650, 205, 680, 205, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(940, 215, 1040, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(1040, 160, 260, 110, "Outbound Adapter", "PostgreSQL Hibernate DAO", badge="ADAPTER", frame_id=fid)
    save_and_export(s, fid, cat, 45, "45_component_architecture", "Component Architecture", "high", "hexagonal", ["ports", "adapters", "domain_core"])

    # 46. Class Diagram (UML 3-Compartment Classes)
    s, fid, tw, th = create_base_scene("UML Class Diagram with Methods & Inheritance", "SOFTWARE")
    s.add_uml_class(40, 90, 320, 280, "UserAccount", "entity", ["id: UUID", "email: String", "hashedPassword: str", "isActive: bool"], ["validatePassword(pwd)", "changeEmail(newEmail)", "deactivate()"], is_hero=False, frame_id=fid)
    s.add_arrow(360, 210, 480, 210, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_uml_class(480, 90, 340, 280, "Order", "aggregate_root", ["orderId: UUID", "totalAmount: Decimal", "status: OrderStatus", "items: List[OrderItem]"], ["addItem(sku, qty)", "calculateTotal()", "markAsPaid()"], is_hero=True, frame_id=fid)
    s.add_arrow(820, 210, 940, 210, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_uml_class(940, 90, 340, 280, "PaymentTransaction", "entity", ["txId: UUID", "gatewayRef: str", "amount: Decimal", "processedAt: DateTime"], ["authorize()", "capture()", "refund(reason)"], is_hero=False, frame_id=fid)
    save_and_export(s, fid, cat, 46, "46_class_diagram", "Class Diagram", "high", "uml_classes", ["classes", "attributes", "associations"])

    # 47. Activity Diagram
    s, fid, tw, th = create_base_scene("UML Activity Diagram (Fork, Join & Decisions)", "SOFTWARE")
    s.add_ellipse(60, 210, 30, 30, bg="#0F172A", stroke="#0F172A", frame_id=fid)
    s.add_arrow(90, 225, 170, 225, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(170, 180, 200, 90, "Recibir Pedido", "Validar Payload", frame_id=fid)
    s.add_arrow(370, 225, 450, 225, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    # Fork Bar
    s.add_rect(450, 120, 16, 210, bg="#0F172A", stroke="#0F172A", frame_id=fid)
    s.add_arrow(466, 160, 560, 140, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(466, 280, 560, 290, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(560, 100, 240, 80, "Cobrar Tarjeta", "Stripe API Charge", is_hero=True, frame_id=fid)
    s.add_quad_card(560, 250, 240, 80, "Reservar Stock", "Inventory Service", frame_id=fid)
    # Join Bar
    s.add_arrow(800, 140, 900, 160, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(800, 290, 900, 280, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_rect(900, 120, 16, 210, bg="#0F172A", stroke="#0F172A", frame_id=fid)
    s.add_arrow(916, 225, 1000, 225, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(1000, 180, 220, 90, "Notificar Cliente", "Email de Confirmacion", frame_id=fid)
    save_and_export(s, fid, cat, 47, "47_activity_diagram", "Activity Diagram", "medium", "activity_flow", ["fork_join", "swimlanes"])

    # 48. State Machine Diagram
    s, fid, tw, th = create_base_scene("UML State Machine (States, Transitions & Guards)", "SOFTWARE")
    states = [("BORRADOR", 40, False), ("PENDIENTE PAGO", 320, False), ("PAGADO", 600, True), ("EN PREPARACION", 880, False), ("ENVIADO", 1160, False)]
    for s_name, sx, is_h in states:
        s.add_rect(sx, 170, 200, 90, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#0F172A", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(sx + 15, 205, s_name, font_size=11, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        if sx < 1160:
            s.add_arrow(sx + 200, 215, sx + 280, 215, stroke="#D93829" if is_h else "#94A3B8", stroke_w=1.5, frame_id=fid)
    save_and_export(s, fid, cat, 48, "48_state_machine_diagram", "State Machine Diagram", "high", "state_machine", ["states", "transitions", "events"])

    # 49. Use Case Diagram
    s, fid, tw, th = create_base_scene("UML Use Case Diagram (Actors & Boundaries)", "SOFTWARE")
    s.add_actor_node(60, 200, 160, 70, "Cliente Web", "Actor Principal", frame_id=fid)
    s.add_rect(300, 80, 800, 350, bg="#FFFFFF", stroke="#0F172A", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(320, 105, "SISTEMA DE PAGOS EN LINEA", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_quad_card(340, 140, 320, 65, "UC1: Iniciar Pago", "<<include>> Validar Stock", frame_id=fid)
    s.add_quad_card(340, 230, 320, 65, "UC2: Confirmar 3DS", "<<extend>> Notificar Fraude", is_hero=True, frame_id=fid)
    s.add_quad_card(340, 320, 320, 65, "UC3: Descargar Factura", "Generar PDF firmado", frame_id=fid)
    s.add_arrow(220, 235, 340, 170, stroke="#94A3B8", frame_id=fid)
    s.add_arrow(220, 235, 340, 260, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 49, "49_use_case_diagram", "Use Case Diagram", "medium", "use_cases", ["actors", "system_boundary"])

    # 50. Security Architecture
    s, fid, tw, th = create_base_scene("Defense-in-Depth Security & Zero-Trust Architecture", "SOFTWARE")
    s.add_actor_node(40, 180, 180, 70, "Usuario Final", "HTTPS / TLS 1.3", frame_id=fid)
    s.add_arrow(220, 215, 300, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_security_barrier(300, 140, 200, 150, "Cloudflare WAF", ["DDoS Mitigation", "Bot Defense", "IP Rate Limit"], badge="WAF", frame_id=fid)
    s.add_arrow(500, 215, 580, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(580, 150, 240, 130, "Envoy API Gateway", "JWT Verification\nmTLS Mesh Ingress", badge="GATEWAY", frame_id=fid)
    s.add_arrow(820, 215, 900, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(900, 150, 240, 130, "Core Service", "RBAC Policy Engine\nZero-Trust Runtime", badge="SERVICE", frame_id=fid)
    s.add_arrow(1140, 215, 1220, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_database_cylinder(1220, 150, 200, 130, "Encrypted DB", "AES-256 at Rest", frame_id=fid)
    save_and_export(s, fid, cat, 50, "50_security_architecture", "Security Architecture", "extreme", "pipeline_security", ["waf", "mtls", "zero_trust"])

    # 51. Network Architecture (DMZ + Subnets)
    s, fid, tw, th = create_base_scene("Multi-Tier Network Architecture (DMZ, Firewall & VPC)", "SOFTWARE")
    s.add_rect(40, 80, 420, 350, bg="#F8FAFC", stroke="#0F172A", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ZONA DMZ (PUBLICA)", font_size=11, font_family=3, color="#0F172A", frame_id=fid)
    s.add_quad_card(60, 140, 380, 90, "Bastion Host SSH", "MFA Access / Port 22", badge="BASTION", frame_id=fid)
    s.add_quad_card(60, 250, 380, 90, "Public NAT Gateway", "Salida a Internet Segura", badge="GATEWAY", frame_id=fid)
    s.add_arrow(460, 215, 540, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_rect(540, 80, 860, 350, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(560, 105, "VPC PRIVADA (SIN ACCESO DIRECTO DESDE INTERNET)", font_size=11, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_quad_card(560, 150, 380, 150, "Subred de Aplicacion", "Microservicios en EKS / ECS\nComunicacion mTLS interna", badge="APP SUB", is_hero=True, frame_id=fid)
    s.add_quad_card(980, 150, 380, 150, "Subred de Base de Datos", "Cluster Aurora PostgreSQL\nRestriccion estricta de Security Group", badge="DB SUB", frame_id=fid)
    save_and_export(s, fid, cat, 51, "51_network_architecture", "Network Architecture", "high", "network_tiers", ["dmz", "subnets", "firewall"])

    # 52. Package Diagram
    s, fid, tw, th = create_base_scene("Package Dependency & Modular Subsystems", "SOFTWARE")
    pkgs = [("Presentation", 40, 180), ("Application", 390, 180), ("Domain", 740, 180), ("Infrastructure", 1090, 180)]
    for pname, px, py in pkgs:
        s.add_rect(px, py - 25, 90, 25, bg="#E2E8F0", stroke="#0F172A", stroke_w=1.2, roundness_type=3, frame_id=fid)
        s.add_text(px + 10, py - 18, "package", font_size=8, font_family=3, color="#475569", frame_id=fid)
        s.add_rect(px, py, 260, 130, bg="#FFFFFF", stroke="#0F172A", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(px + 15, py + 20, pname, font_size=13, font_family=3, color="#0F172A", frame_id=fid)
        s.add_text(px + 15, py + 55, f"Clases y modulos de {pname.lower()}", font_size=10, font_family=3, color="#64748B", frame_id=fid)
        if px < 1090:
            s.add_arrow(px + 260, py + 65, px + 350, py + 65, stroke="#D93829" if pname=="Domain" else "#94A3B8", stroke_w=1.5, frame_id=fid)
    save_and_export(s, fid, cat, 52, "52_package_diagram", "Package Diagram", "medium", "package_tree", ["packages", "imports"])

    # 53. Infrastructure Architecture
    s, fid, tw, th = create_base_scene("Hybrid Cloud & On-Premises Infrastructure", "SOFTWARE")
    s.add_rect(40, 80, 600, 350, bg="#F8FAFC", stroke="#0F172A", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ON-PREMISES DATA CENTER (LEGACY)", font_size=11, font_family=3, color="#0F172A", frame_id=fid)
    s.add_quad_card(60, 150, 260, 120, "Servidor Bare-Metal", "VMware ESXi Cluster", badge="HARDWARE", frame_id=fid)
    s.add_quad_card(340, 150, 260, 120, "SAN Storage", "10Gbps iSCSI", badge="STORAGE", frame_id=fid)
    s.add_arrow(640, 220, 740, 220, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_text(650, 200, "VPN IPsec", font_size=10, font_family=3, color="#D93829", frame_id=fid)
    s.add_rect(740, 80, 660, 350, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "PUBLIC CLOUD (AWS US-EAST-1)", font_size=11, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_quad_card(760, 150, 300, 120, "EKS Kubernetes", "Auto-Scaling Fargate", badge="CLOUD COMPUTE", is_hero=True, frame_id=fid)
    s.add_database_cylinder(1080, 140, 280, 150, "Amazon Aurora RDS", "Global Database Replica", frame_id=fid)
    save_and_export(s, fid, cat, 53, "53_infrastructure_architecture", "Infrastructure Architecture", "high", "infrastructure", ["servers", "storage", "dc"])

    # 54. Cloud Architecture Multi-AZ
    s, fid, tw, th = create_base_scene("Cloud Native Multi-AZ High Availability Architecture", "SOFTWARE")
    s.add_quad_card(40, 160, 220, 110, "AWS Route 53", "DNS Failover & Latency Routing", badge="DNS", frame_id=fid)
    s.add_arrow(260, 215, 360, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(360, 140, 260, 150, "Application Load Balancer", "SSL Termination\nHealth Check Probes", badge="ALB", is_hero=True, frame_id=fid)
    s.add_arrow(620, 180, 720, 140, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(620, 250, 720, 290, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(720, 90, 340, 110, "Availability Zone A (us-east-1a)", "ECS Tasks (Active)", badge="AZ-A", frame_id=fid)
    s.add_quad_card(720, 240, 340, 110, "Availability Zone B (us-east-1b)", "ECS Tasks (Active)", badge="AZ-B", frame_id=fid)
    s.add_database_cylinder(1120, 140, 280, 160, "Aurora Multi-AZ DB", "Writer AZ-A / Reader AZ-B", frame_id=fid)
    save_and_export(s, fid, cat, 54, "54_cloud_architecture", "Cloud Architecture", "high", "cloud_multi_az", ["vpc", "az", "services"])

    # 55. AWS Architecture
    s, fid, tw, th = create_base_scene("AWS Enterprise Architecture (CloudFront, ALB, ECS, RDS)", "SOFTWARE")
    s.add_quad_card(40, 160, 220, 110, "Amazon CloudFront", "Edge CDN & DDoS Shield", badge="EDGE", frame_id=fid)
    s.add_arrow(260, 215, 340, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(340, 140, 240, 150, "AWS ALB", "Application Load Balancer", badge="ALB", frame_id=fid)
    s.add_arrow(580, 215, 660, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(660, 130, 300, 170, "Amazon ECS Fargate", "Microservicios sin servidor\nAuto-Scaling Group", badge="COMPUTE", is_hero=True, frame_id=fid)
    s.add_arrow(960, 215, 1040, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_database_cylinder(1040, 140, 320, 150, "Amazon Aurora RDS", "PostgreSQL Compatible Multi-AZ", frame_id=fid)
    save_and_export(s, fid, cat, 55, "55_aws_architecture", "AWS Architecture", "extreme", "aws_stack", ["aws_services", "vpc", "iam"])

    # 56. Azure Architecture
    s, fid, tw, th = create_base_scene("Microsoft Azure Architecture (App GW, AKS, Cosmos DB)", "SOFTWARE")
    s.add_quad_card(40, 160, 220, 110, "Azure Front Door", "Global CDN & WAF", badge="EDGE", frame_id=fid)
    s.add_arrow(260, 215, 340, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(340, 140, 260, 150, "Application Gateway", "URL-based routing & SSL", badge="GATEWAY", frame_id=fid)
    s.add_arrow(600, 215, 680, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(680, 130, 300, 170, "Azure Kubernetes (AKS)", "Cluster gestionado\nVirtual Nodes", badge="AKS", is_hero=True, frame_id=fid)
    s.add_arrow(980, 215, 1060, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_database_cylinder(1060, 140, 300, 150, "Azure Cosmos DB", "NoSQL Multi-Region Write", frame_id=fid)
    save_and_export(s, fid, cat, 56, "56_azure_architecture", "Azure Architecture", "extreme", "azure_stack", ["vnet", "aks", "cosmos"])

    # 57. GCP Architecture
    s, fid, tw, th = create_base_scene("Google Cloud Architecture (Cloud Armor, GKE, Spanner)", "SOFTWARE")
    s.add_quad_card(40, 160, 220, 110, "Google Cloud Armor", "DDoS Mitigation & WAF", badge="SECURITY", frame_id=fid)
    s.add_arrow(260, 215, 340, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(340, 140, 260, 150, "Cloud Load Balancing", "Anycast Global IP", badge="LB", frame_id=fid)
    s.add_arrow(600, 215, 680, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(680, 130, 300, 170, "Google Kubernetes (GKE)", "Autopilot Managed Cluster", badge="GKE", is_hero=True, frame_id=fid)
    s.add_arrow(980, 215, 1060, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_database_cylinder(1060, 140, 300, 150, "Cloud Spanner", "Consistencia estricta global", frame_id=fid)
    save_and_export(s, fid, cat, 57, "57_gcp_architecture", "GCP Architecture", "extreme", "gcp_stack", ["gke", "spanner", "pubsub"])

    # 58. CI/CD Pipeline
    s, fid, tw, th = create_base_scene("Automated CI/CD Pipeline (Build -> Test -> SecScan -> Deploy)", "SOFTWARE")
    p_stages = ["1. GitHub Commit", "2. GitHub Actions (Build)", "3. Trivy / Sonar (SecScan)", "4. ArgoCD (Deploy K8s)"]
    for i, pstage in enumerate(p_stages):
        px = 40 + i * 345
        s.add_quad_card(px, 140, 330, 150, pstage, f"Etapa #{i+1} de entrega continua", badge="CI/CD", is_hero=(i==2), frame_id=fid)
        if i < 3:
            s.add_arrow(px + 330, 215, px + 345, 215, stroke="#D93829" if i==2 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 58, "58_cicd_pipeline", "CI/CD Pipeline", "high", "pipeline", ["stages", "artifacts", "gates"])

    # 59. Kubernetes Architecture
    s, fid, tw, th = create_base_scene("Kubernetes Cluster Architecture (Control Plane & Worker Nodes)", "SOFTWARE")
    s.add_rect(40, 80, 380, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "CONTROL PLANE (MASTER NODE)", font_size=11, font_family=3, color="#D93829", frame_id=fid)
    s.add_quad_card(60, 140, 340, 70, "kube-apiserver", "REST API & Cluster State", badge="API", frame_id=fid)
    s.add_quad_card(60, 220, 340, 70, "kube-scheduler", "Asigna pods a nodos", badge="SCHED", frame_id=fid)
    s.add_database_cylinder(60, 300, 340, 100, "etcd cluster", "Almacen clave-valor de estado", frame_id=fid)
    s.add_arrow(420, 215, 480, 215, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_k8s_node(480, 80, 440, 350, "worker-01", "Worker Node", [{"name": "app-api", "image": "api:v2", "status": "Running"}, {"name": "worker-queue", "image": "worker:v1", "status": "Running"}], is_hero=True, frame_id=fid)
    s.add_k8s_node(940, 80, 460, 350, "worker-02", "Worker Node", [{"name": "frontend", "image": "ui:v1", "status": "Running"}, {"name": "cache-redis", "image": "redis:7", "status": "Running"}], is_hero=False, frame_id=fid)
    save_and_export(s, fid, cat, 59, "59_kubernetes_architecture", "Kubernetes Architecture", "extreme", "k8s_cluster", ["pods", "deployments", "ingress"])

    # 60. Docker Architecture
    s, fid, tw, th = create_base_scene("Docker Container Engine & Network Architecture", "SOFTWARE")
    s.add_quad_card(40, 160, 220, 110, "Docker Client", "CLI (docker build/run)\nREST API Calls", badge="CLIENT", frame_id=fid)
    s.add_arrow(260, 215, 360, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_rect(360, 80, 620, 350, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(380, 105, "DOCKER HOST (DAEMON: DOCKERD)", font_size=11, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_quad_card(380, 140, 280, 120, "Containers", "Contenedores en ejecucion\nNamespaces + cgroups", badge="RUNTIME", is_hero=True, frame_id=fid)
    s.add_quad_card(680, 140, 280, 120, "Images Cache", "Capas de imagenes cacheadas\nOverlayFS", badge="STORAGE", frame_id=fid)
    s.add_arrow(980, 215, 1080, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(1080, 160, 280, 110, "Docker Registry", "Docker Hub / AWS ECR", badge="REGISTRY", frame_id=fid)
    save_and_export(s, fid, cat, 60, "60_docker_architecture", "Docker Architecture", "medium", "docker_engine", ["containers", "daemon", "volumes"])
