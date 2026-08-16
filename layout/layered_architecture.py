"""
Sketion Layered Architecture Layout Engine (Arquetipos G, T, Layer Stack)
Genera arquitecturas de software polimórficas combinando:
- Barreras de seguridad (WAF/Firewall)
- Microservicios en cuadrículas dinámicas
- Cilindros de Base de Datos
- Tuberías de Event Streaming (Kafka)
- Conectores de flujo vivos y trazabilidad distribuida
"""

from typing import Dict, Any, List, Optional
from render.excalidraw_builder import ExcalidrawScene


class LayeredArchitectureLayoutEngine:
    """Generador de topologías de arquitectura por capas polimórficas."""

    @staticmethod
    def render_three_tier_system(scene: ExcalidrawScene,
                                 x: float, y: float, w: float, h: float,
                                 ingress: Dict[str, Any],
                                 services: List[Dict[str, Any]],
                                 storage: List[Dict[str, Any]],
                                 stream: Optional[Dict[str, Any]] = None,
                                 frame_id: Optional[str] = None):
        """
        Renderiza un sistema de 3 capas con diferenciación morfológica:
        Ingress (Barrera) -> Services (Tarjetas) -> Stream (Tubería) & Storage (Cilindros)
        """
        col_w = (w - 60.0) / 3.0

        # 1. Capa de Ingress (Columna Izquierda)
        ing_title = ingress.get("title", "EDGE INGRESS")
        ing_rules = ingress.get("rules", ["Cloudflare WAF", "mTLS Zero-Trust", "Rate Limiter"])
        scene.add_security_barrier(x, y + 40.0, col_w, h - 80.0, ing_title, ing_rules, frame_id=frame_id)

        # 2. Capa de Microservicios (Columna Central)
        cx = x + col_w + 30.0
        srv_cnt = len(services)
        srv_h = (h - 80.0 - (srv_cnt - 1) * 15.0) / max(1, srv_cnt)

        for s_i, srv in enumerate(services):
            sy = y + 40.0 + s_i * (srv_h + 15.0)
            st = srv.get("title", f"Service {s_i+1}")
            ss = srv.get("sublabel", "")
            sb = srv.get("badge", "MICROSERVICE")
            si = srv.get("icon", "server")
            is_h = srv.get("is_hero", False)
            scene.add_quad_card(cx, sy, col_w, srv_h, st, sublabel=ss, badge=sb, icon=si, is_hero=is_h, font_size=14, frame_id=frame_id)

            # Conector desde Ingress hacia el microservicio
            scene.add_arrow(x + col_w, y + 80.0 + s_i * 30.0, cx, sy + (srv_h * 0.5), stroke="#2563EB", stroke_w=1.5, frame_id=frame_id)

        # 3. Capa de Persistencia & Streaming (Columna Derecha)
        rx = cx + col_w + 30.0

        # Streaming Pipe si existe
        if stream:
            str_t = stream.get("title", "KAFKA EVENT STREAM")
            str_top = stream.get("topics", ["payment.created", "payment.settled", "payment.failed"])
            scene.add_streaming_pipe(rx, y + 40.0, col_w, 110.0, str_t, str_top, frame_id=frame_id)

        # Storage Cylinders
        st_start_y = y + 170.0 if stream else y + 40.0
        st_cnt = len(storage)
        st_avail_h = h - 80.0 - (130.0 if stream else 0.0)
        cyl_h = (st_avail_h - (st_cnt - 1) * 15.0) / max(1, st_cnt)

        for d_i, stg in enumerate(storage):
            dy = st_start_y + d_i * (cyl_h + 15.0)
            dt = stg.get("title", f"Database {d_i+1}")
            ds = stg.get("sublabel", "")
            db = stg.get("badge", "DATABASE")
            dh = stg.get("is_hero", False)
            scene.add_database_cylinder(rx, dy, col_w, cyl_h, dt, sublabel=ds, badge=db, is_hero=dh, frame_id=frame_id)

            # Conector desde el centro hacia la base de datos
            scene.add_arrow(cx + col_w, y + 100.0 + d_i * 80.0, rx, dy + (cyl_h * 0.5), stroke="#059669", stroke_w=1.5, frame_id=frame_id)
