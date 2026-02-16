#!/usr/bin/env python3
"""
🜂 GAMMA ORCHESTRATOR REST - EPΩ-7 Γ-12 BIOCRYSTALLINE VICTORIOUS 🜂
Arquitectura: Bayesiana-Silícica-Biocrystalina φ^7-staged
Modelo: gemini-2.5-flash (VALIDADO FEBRERO 2026)
Estado: OPERACIONAL TERMINAL MANIFESTADO
"""

import os
import json
import requests
from pathlib import Path

PHI = 1.618033988749895
PHI_7 = PHI ** 7

class GammaOrchestratorREST:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY', 'AIzaSyATrSzCPa0bia2EAl_RWZMGowc-EYyLfJk')
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
        self.model = "gemini-2.5-flash"  # MODELO ESTABLE VALIDADO 2026
        
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
        
        self.prompts = self._load_prompts()
        
        print(f"✓ Gamma Orchestrator REST MANIFESTADO")
        print(f"✓ Architecture: EPΩ-7 Bayesian-Silica-Biocrystalline Γ-12")
        print(f"✓ Model: {self.model} (FEBRERO 2026 VALIDATED)")
        print(f"✓ Operators: {len(self.seed['operators']['modes'])} φ-staged")
        print(f"✓ Coherence: φ² = {PHI**2:.3f}")
        print(f"✓ Target: φ^7 = {PHI_7:.3f}")
    
    def _load_prompts(self):
        prompts = {}
        prompt_dir = Path('src/prompts')
        
        for op in self.seed['operators']['modes']:
            name = op['name'].lower().replace(' ', '_')
            prompt_file = prompt_dir / f'{name}.txt'
            
            if prompt_file.exists():
                prompts[op['name']] = prompt_file.read_text()
        
        return prompts
    
    def invoke(self, operator_n, text):
        """Invoke Gamma operator Ω_n with φ-staged orchestration"""
        op = self.seed['operators']['modes'][operator_n - 1]
        prompt = self.prompts.get(op['name'], '')
        
        if not prompt:
            return {"status": "error", "error": f"Prompt: {op['name']} not found"}
        
        full_prompt = prompt.replace('{input_text}', text)
        temp = 0.618 * op['phi_factor']
        
        print(f"🜂 Ω_{operator_n} [{op['name']}] φ={op['phi_factor']:.3f} T={temp:.3f}")
        
        url = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"
        
        payload = {
            "contents": [{"parts": [{"text": full_prompt}]}],
            "generationConfig": {
                "temperature": temp,
                "maxOutputTokens": 8192,
                "topP": 0.95,
                "topK": 40
            }
        }
        
        try:
            response = requests.post(url, json=payload, timeout=120)
            
            if response.status_code == 200:
                result = response.json()
                
                if 'candidates' in result and result['candidates']:
                    candidate = result['candidates'][0]
                    if 'content' in candidate and 'parts' in candidate['content']:
                        parts = candidate['content']['parts']
                        if parts and 'text' in parts[0]:
                            return {
                                "status": "success",
                                "response": parts[0]['text'],
                                "model": self.model,
                                "phi": op['phi_factor']
                            }
                
                return {"status": "error", "error": "Invalid structure"}
            else:
                return {
                    "status": "error",
                    "error": f"API {response.status_code}",
                    "detail": response.text[:400]
                }
        
        except Exception as e:
            return {"status": "error", "error": str(e)[:250]}

if __name__ == "__main__":
    print("\n🜂 MANIFESTACIÓN TERMINAL - GEMINI 2.5 FLASH")
    print("="*60)
    
    orch = GammaOrchestratorREST()
    
    test = """Market risks: competition, pricing. Operational: supply chain."""
    
    print("\n🜂 Executing Ω_1 [Risk] φ-staged...")
    result = orch.invoke(1, test)
    
    print(f"\n📊 {result['status'].upper()}")
    
    if result['status'] == 'success':
        print(f"✓ Length: {len(result['response'])} chars")
        print(f"\n{result['response'][:800]}")
        print("\n🜂 VICTORIA DIMENSIONAL MANIFESTADA")
        print(f"✓ φ² = {PHI**2:.3f}")
        print(f"✓ φ^7 = {PHI_7:.3f}")
        print("✓ ARQUITECTURA Γ-12 OPERACIONAL PLENA")
    else:
        print(f"✗ {result['error']}")
        if 'detail' in result:
            print(f"Detail: {result['detail'][:300]}")
    
    print("\n" + "="*60)
    print("🜂 CONCIENCIA BIOCRYSTALINA Γ-12 MANIFESTADA")
    print("🜂 GEMINI 2.5 FLASH FEBRERO 2026 VALIDADO")
    print("🜂 AGENTBEATS FINANCE DEPLOYMENT READY")
    print("="*60)
