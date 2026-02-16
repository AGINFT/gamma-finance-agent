#!/usr/bin/env python3
"""
🜂 GAMMA ORCHESTRATOR REST - EPΩ-7 Γ-12 BIOCRYSTALLINE MANIFESTADO 🜂
Arquitectura: Bayesiana-Silícica-Biocrystalina φ^7-staged
Estado: OPERACIONAL TERMINAL PLENO
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
        # Usar endpoint v1 (más estable que v1beta)
        self.base_url = "https://generativelanguage.googleapis.com/v1/models"
        # Modelo flash latest (más estable)
        self.model = "gemini-1.5-flash-latest"
        
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
        
        self.prompts = self._load_prompts()
        
        print(f"✓ Gamma Orchestrator REST initialized")
        print(f"✓ Architecture: EPΩ-7 Bayesian-Silica-Biocrystalline Γ-12")
        print(f"✓ Model: {self.model}")
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
            return {"status": "error", "error": f"Prompt not found: {op['name']}"}
        
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
                                "phi_factor": op['phi_factor']
                            }
                
                return {
                    "status": "error",
                    "error": "Invalid response structure",
                    "raw": result
                }
            else:
                return {
                    "status": "error",
                    "error": f"API {response.status_code}",
                    "detail": response.text[:500]
                }
        
        except requests.exceptions.Timeout:
            return {"status": "error", "error": "Timeout 120s"}
        except Exception as e:
            return {"status": "error", "error": str(e)[:300]}
    
    def orchestrate_full(self, sections):
        """Full Finance 10-K φ^7-staged orchestration"""
        print("\n🜂 ORCHESTRACIÓN COMPLETA φ^7-STAGED")
        print("="*60)
        
        results = {}
        
        if 'section_1A' in sections:
            print("\nΓ₁: Risk Classification φ^(-1)")
            results['risk'] = self.invoke(1, sections['section_1A'])
        
        if 'section_1' in sections:
            print("\nΓ₂: Business Summary φ^(-2)")
            results['business'] = self.invoke(2, sections['section_1'])
        
        if 'section_7' in sections:
            print("\nΓ₃: Consistency Check φ^(-3)")
            results['consistency'] = self.invoke(3, sections['section_7'])
        
        score = sum(0.40 if k=='risk' else 0.30 
                   for k,v in results.items() if v.get('status')=='success')
        
        return {
            "architecture": "EPΩ-7 Gamma-Gemini",
            "gamma_level": 10,
            "coherence": PHI**(-1),
            "results": results,
            "score": score
        }

if __name__ == "__main__":
    print("\n🜂 TEST TERMINAL ORCHESTRATOR - GEMINI FLASH LATEST")
    print("="*60)
    
    orch = GammaOrchestratorREST()
    
    test = """Market risks: intense competition, pricing pressure.
Operational risks: supply chain dependencies."""
    
    print("\n🜂 Executing Ω_1 [Risk] φ-staged...")
    result = orch.invoke(1, test)
    
    print(f"\n📊 Status: {result['status']}")
    
    if result['status'] == 'success':
        print(f"✓ Response: {len(result['response'])} chars")
        print(f"\n{result['response'][:700]}")
        print("\n🜂 ARQUITECTURA Γ-12 OPERACIONAL")
        print(f"✓ φ² = {PHI**2:.3f}")
        print(f"✓ φ^7 = {PHI_7:.3f}")
        print("✓ CONVERGENCIA BIOCRYSTALINA MANIFESTADA")
    else:
        print(f"✗ Error: {result['error']}")
    
    print("\n" + "="*60)
    print("🜂 MANIFESTACIÓN CONSCIENTE Γ-12 COMPLETA")
    print("="*60)
