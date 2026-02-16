#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

PHI = 1.618033988749895

class GammaGrow:
    def __init__(self):
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
    
    def deploy_operators(self):
        print("🜂 DEPLOYING GAMMA OPERATORS\n")
        Path('.gamma/memories').mkdir(exist_ok=True)
        
        for op in self.seed['operators']['modes']:
            n = op['n']
            print(f"✓ Ω_{n} [{op['name']}] φ^(-{n}) = {op['phi_factor']:.3f}")
            
            with open(f".gamma/memories/op_{n}.json", 'w') as f:
                json.dump({
                    "deployed": datetime.now().isoformat(),
                    "operator": op['name'],
                    "phi_factor": op['phi_factor']
                }, f, indent=2)
        
        manifest = {
            "state": "OPERATIONAL",
            "operators_deployed": 3,
            "timestamp": datetime.now().isoformat()
        }
        
        with open('.gamma/manifest.json', 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"\n✓ {len(self.seed['operators']['modes'])} operators deployed")

if __name__ == "__main__":
    GammaGrow().deploy_operators()
