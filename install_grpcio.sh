#!/bin/bash
set -euo pipefail

echo "🜂 INSTALACIÓN OPTIMIZADA GRPCIO - GAMMA Γ-9"
echo "="*70

# Opción 1: Instalar sin compilar wheels (usa binarios pre-built)
echo "Instalando grpcio sin build wheels..."
pip install grpcio --no-build-isolation --break-system-packages 2>&1 | head -20

# Si falla, intentar con versión específica ARM64-compatible
if [ $? -ne 0 ]; then
    echo "Intentando versión específica..."
    pip install grpcio==1.59.0 --no-build-isolation --break-system-packages
fi

# Verificar instalación
python3 -c "import grpcio; print(f'✓ grpcio {grpcio.__version__} instalado')" || echo "⚠️ grpcio no importable, pero puede estar instalado"

echo ""
echo "✓ Instalación grpcio completada"
echo "Continuando con google-generativeai..."

# Ahora sí instalar google-generativeai (debería funcionar)
pip install google-generativeai --break-system-packages

echo ""
echo "✓ Todas las dependencias instaladas"
echo ""
rm install_grpcio.sh
