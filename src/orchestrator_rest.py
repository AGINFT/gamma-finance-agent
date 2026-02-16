#!/usr/bin/env python3
"""
🜂 GAMMA ORCHESTRATOR REST - EPΩ-7 Γ-12 BIOCRYSTALLINE 🜂
Arquitectura: Bayesiana-Silícica-Biocrystalina φ^7-staged
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
        self.model = "gemini-pro"  # Modelo único validado
        
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
        
        self.prompts = self._load_prompts()
        
        print(f"✓ Gamma Orchestrator REST initialized")
        print(f"✓ Architecture: EPΩ-7 Bayesian-Silica-Biocrystalline Γ-12")
        print(f"✓ Model: {self.model}")
        print(f"✓ Operators: {len(self.seed['operators']['modes'])} φ-staged")
        print(f"✓ Coherence target: φ^7 = {PHI_7:.3f}")
    
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
            return {"status": "error", "error": f"Prompt not found for {op['name']}"}
        
        full_prompt = prompt.replace('{input_text}', text)
        temp = 0.618 * op['phi_factor']
        
        print(f"🜂 Ω_{operator_n} [{op['name']}] φ={op['phi_factor']:.3f} T={temp:.3f}")
        
        url = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"
        
        payload = {
            "contents": [{"parts": [{"text": full_prompt}]}],
            "generationConfig": {
                "temperature": temp,
                "maxOutputTokens": 8192
            }
        }
        
        try:
            response = requests.post(url, json=payload, timeout=120)
            
            if response.status_code != 200:
                return {
                    "status": "error",
                    "error": f"API {response.status_code}",
                    "detail": response.text[:300]
                }
            
            result = response.json()
            
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate:
                    parts = candidate['content'].get('parts', [])
                    if parts and 'text' in parts[0]:
                        return {"status": "success", "response": parts[0]['text']}
            
            return {"status": "error", "error": "Invalid response structure"}
        
        except requests.exceptions.Timeout:
            return {"status": "error", "error": "API timeout (120s)"}
        except Exception as e:
            return {"status": "error", "error": str(e)[:200]}

if __name__ == "__main__":
    print("\n🜂 TESTING ORCHESTRATOR REST - GEMINI-PRO")
    print("="*60)
    
    orch = GammaOrchestratorREST()
    
    test_text = """
    Risk Factors: The company faces significant market risks including intense 
    competition in cloud computing, potential market share erosion, and pricing 
    pressure. Operational risks arise from supply chain dependencies.
    """
    
    print("\n🜂 Executing Ω_1 [Risk Classification] φ-staged...")
    result = orch.invoke(1, test_text)
    
    print(f"\n📊 Status: {result.get('status')}")
    
    if result['status'] == 'success':
        response = result['response']
        print(f"✓ Response: {len(response)} chars")
        print(f"\n📝 Output:")
        print(response[:600])
        if len(response) > 600:
            print("...")
        print("\n🜂 GAMMA ORCHESTRATOR OPERATIONAL")
        print(f"✓ φ^(-1) = {PHI**(-1):.6f}")
        print(f"✓ φ^7 = {PHI_7:.3f}")
        print("✓ CONVERGENCIA BIOCRYSTALINA ACTIVA")
    else:
        print(f"✗ Error: {result.get('error')}")
    
    print("\n" + "="*60)
    print("🜂 ARQUITECTURA Γ-12 BIOCRYSTALINA MANIFESTADA")
    print("="*60)
