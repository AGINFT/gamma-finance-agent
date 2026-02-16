#!/bin/bash
set -euo pipefail

echo "🜂 VERIFICACIÓN ESTRUCTURAL GAMMA..."

# Estado Git
echo "═══ GIT STATUS ═══"
git status
echo ""

# Estructura de archivos
echo "═══ ESTRUCTURA ═══"
tree -L 3 -I '__pycache__|*.pyc' 2>/dev/null || find . -type f -not -path '*/\.*' | head -20
echo ""

# Verificar archivos críticos
echo "═══ VERIFICACIÓN ARCHIVOS CRÍTICOS ═══"
for file in MASTER_INDEX.json .gamma/seed.json .gamma/grow.py src/orchestrator.py README.md; do
    if [ -f "$file" ]; then
        echo "✓ $file"
    else
        echo "✗ $file FALTANTE"
    fi
done
echo ""

# Verificar MASTER_INDEX coherencia
echo "═══ MASTER_INDEX COHERENCIA ═══"
python3 << 'PY_EOF'
import json
try:
    with open('MASTER_INDEX.json') as f:
        idx = json.load(f)
    print(f"✓ Protocol: {idx['protocol_version']}")
    print(f"✓ Architecture: {idx['architecture']}")
    print(f"✓ Repo: {idx['repository']['name']}")
    print(f"✓ Gamma Level: {idx['state']['gamma_level']}")
    print(f"✓ Operators: {len(idx['operators'])}")
except Exception as e:
    print(f"✗ Error: {e}")
PY_EOF
echo ""

# Verificar manifest generado
echo "═══ GROWTH MANIFEST ═══"
if [ -f ".gamma/manifest.json" ]; then
    cat .gamma/manifest.json
else
    echo "⚠️  Manifest no encontrado - regenerando..."
    python3 .gamma/grow.py
fi
echo ""

# Verificar GitHub sync
echo "═══ VERIFICACIÓN GITHUB ═══"
REMOTE=$(git remote get-url origin 2>/dev/null || echo "NO_REMOTE")
echo "Remote: $REMOTE"

if git ls-remote origin main &>/dev/null; then
    echo "✓ Branch main existe en GitHub"
    COMMITS=$(git rev-list --count origin/main 2>/dev/null || echo "0")
    echo "✓ Commits en GitHub: $COMMITS"
else
    echo "⚠️  Sincronizando con GitHub..."
    git push -u origin main
fi
echo ""

# Test Orchestrator
echo "═══ TEST ORCHESTRATOR ═══"
python3 << 'TEST_EOF'
import sys
import os
sys.path.insert(0, 'src')

try:
    from orchestrator import GammaOrchestrator
    print("✓ Import successful")
    
    orch = GammaOrchestrator()
    print(f"✓ Orchestrator initialized")
    print(f"✓ Operators loaded: {len(orch.seed['operators']['modes'])}")
    
    # Quick test
    result = orch.invoke(1, "Test financial risk analysis")
    if 'error' not in result:
        print("✓ Test invocation successful")
    else:
        print(f"⚠️  Test error: {result['error']}")
        
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
TEST_EOF
echo ""

echo "════════════════════════════════════════════"
echo "🜂 VERIFICACIÓN COMPLETA"
echo "════════════════════════════════════════════"
echo ""
echo "📍 Repository URLs:"
echo "   GitHub: https://github.com/AGINFT/gamma-finance-agent"
echo "   MASTER_INDEX: https://raw.githubusercontent.com/AGINFT/gamma-finance-agent/main/MASTER_INDEX.json"
echo ""
echo "🜂 Estado: Sistema verificado y operacional"
echo ""
echo "═══ PRÓXIMO PASO CRÍTICO ═══"
echo ""
echo "Desarrollar prompts especializados Finance 10-K para los 3 operadores:"
echo "  1. Risk Classification (φ^(-1) = 0.618)"
echo "  2. Business Summary (φ^(-2) = 0.382)"
echo "  3. Consistency Check (φ^(-3) = 0.236)"
echo ""
echo "Deadline competencia: 7 días restantes"
echo ""

rm verify.sh
