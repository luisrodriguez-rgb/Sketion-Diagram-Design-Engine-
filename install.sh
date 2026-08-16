#!/usr/bin/env bash
# ==============================================================================
# Sketion Diagram Design Skill — Instalador Rápido de 1 Comando
# Compatible con Antigravity IDE, Cursor, Windsurf, Claude Code y VSCode Agents
# ==============================================================================

set -e

REPO_URL="https://github.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-.git"
GLOBAL_SKILLS_DIR="$HOME/.gemini/config/skills/sketion"
LOCAL_SKILLS_DIR=".agents/skills/sketion"

echo "=================================================================="
echo "Instalando Sketion Diagram Design Skill (v3.4)..."
echo "=================================================================="

# 1. Detectar si estamos en un workspace o instalación global
if [ -d "$HOME/.gemini/config/skills" ]; then
    TARGET_DIR="$GLOBAL_SKILLS_DIR"
    echo "[*] Instalando como Skill Global en: $TARGET_DIR"
else
    TARGET_DIR="$LOCAL_SKILLS_DIR"
    echo "[*] Instalando como Skill Local en: $TARGET_DIR"
fi

# 2. Clonar o Actualizar Repositorio
if [ -d "$TARGET_DIR" ]; then
    echo "[*] Directorio existente detectado. Actualizando a la última versión..."
    cd "$TARGET_DIR"
    git pull origin main
else
    echo "[*] Clonando repositorio desde GitHub..."
    mkdir -p "$(dirname "$TARGET_DIR")"
    git clone "$REPO_URL" "$TARGET_DIR"
fi

# 3. Instalar dependencias Python si existen
if command -v pip3 &> /dev/null; then
    echo "[*] Instalando Sketion CLI globalmente vía pip..."
    pip3 install -e "$TARGET_DIR" --quiet || true
fi

echo "=================================================================="
echo "SKETION INSTALADO CON ÉXITO"
echo "=================================================================="
echo "Para usarlo en tu terminal:"
echo "  sketion generate \"Tu problema o arquitectura\" --audience ceo"
echo ""
echo "Para usarlo con cualquier Agente de IA:"
echo "  Pídele: 'Diseña un diagrama en Excalidraw para [tu caso] usando Sketion'"
echo "=================================================================="
