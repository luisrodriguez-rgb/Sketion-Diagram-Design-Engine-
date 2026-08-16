"""
Sketion 4.5 — Semantic Text Decomposer
Clasifica y descompone texto crudo antes del layout en entidades editoriales:
- Título conciso (<= 4 palabras clave)
- Subtítulo explicativo
- Metadata / Badges
- Puntos clave / Viñetas estructuradas
- Callout / Alertas de cuello de botella
- Sugerencia de Icono vectorial
"""

import re
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class DecomposedBlock:
    raw_text: str
    block_type: str  # 'card', 'callout', 'metric', 'bullet_list', 'sticky_note'
    title: str
    subtitle: str = ""
    badge: str = ""
    bullets: List[str] = field(default_factory=list)
    icon_suggestion: str = "file"
    is_hero: bool = False
    warning_note: str = ""


class SemanticTextDecomposer:
    """Analiza y estructura cualquier texto arbitrario antes de la fase de renderizado."""

    ICON_KEYWORD_MAP = {
        "whatsapp": "laptop",
        "pago": "lock",
        "caja": "lock",
        "cocina": "server",
        "kds": "server",
        "mesa": "container",
        "tiempo": "monitoring",
        "espera": "monitoring",
        "fila": "users",
        "cliente": "user",
        "error": "alert",
        "abandono": "alert",
        "rotacion": "sync",
        "entrega": "key",
        "comanda": "file",
        "qr": "laptop",
        "base de datos": "database",
        "supabase": "postgres",
        "auth": "lock"
    }

    @classmethod
    def suggest_icon(cls, text: str) -> str:
        t_low = text.lower()
        for kw, icon in cls.ICON_KEYWORD_MAP.items():
            if kw in t_low:
                return icon
        return "file"

    @classmethod
    def decompose(cls, raw_content: str, is_pain_or_hero: Optional[str] = None) -> DecomposedBlock:
        """Descompone texto libre en un bloque estructurado con jerarquía estricta."""
        lines = [line.strip() for line in raw_content.split("\n") if line.strip()]
        if not lines:
            return DecomposedBlock(raw_text="", block_type="card", title="Sin Título")

        first_line = lines[0]
        # Detectar viñetas o listas
        bullets = [l.lstrip("•-* ").strip() for l in lines[1:] if l.startswith(("•", "-", "*", "✔", "☑", "☐", "❌"))]
        other_lines = [l for l in lines[1:] if not l.startswith(("•", "-", "*", "✔", "☑", "☐", "❌"))]

        # Extraer badge si tiene prefijo entre corchetes o dos puntos
        badge = ""
        title = first_line
        if ":" in first_line and len(first_line.split(":")[0]) < 20:
            parts = first_line.split(":", 1)
            badge = parts[0].strip().upper()
            title = parts[1].strip()
        elif first_line.startswith("[") and "]" in first_line:
            parts = first_line.split("]", 1)
            badge = parts[0].lstrip("[").strip().upper()
            title = parts[1].strip()

        subtitle = " · ".join(other_lines) if other_lines else ""
        if len(subtitle) > 80:
            subtitle = subtitle[:77] + "..."

        icon = cls.suggest_icon(raw_content)
        is_hero = (is_pain_or_hero == "hero")

        # Detectar si es un callout o sticky de impacto
        block_type = "card"
        if len(lines) >= 4 and len(bullets) >= 2:
            block_type = "bullet_list"
        elif "alerta" in raw_content.lower() or "impacto" in raw_content.lower() or "diagnóstico" in raw_content.lower():
            block_type = "callout"

        return DecomposedBlock(
            raw_text=raw_content,
            block_type=block_type,
            title=title,
            subtitle=subtitle,
            badge=badge or "CORE",
            bullets=bullets,
            icon_suggestion=icon,
            is_hero=is_hero
        )
