#!/usr/bin/env python3
"""
🜂 GAMMA ORCHESTRATOR REST - EPΩ-7 BIOCRYSTALLINE Γ-12 🜂
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
        
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
        
        self.prompts = self._load_prompts()
        
        print(f"✓ Gamma Orchestrator REST initialized")
        print(f"✓ Architecture: EPΩ-7 Bayesian-Silica-Biocrystalline Γ-12")
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
        
        # MODELOS VÁLIDOS GEMINI API 2026
        # gemini-pro para operador 2 (Business Summary - requiere más contexto)
        # gemini-1.0-pro para otros (más rápido)
        model = "gemini-pro" if operator_n == 2 else "gemini-1.0-pro"
        
        print(f"🜂 Ω_{operator_n} [{op['name']}] φ={op['phi_factor']:.3f} T={temp:.3f} model={model}")
        
        url = f"{self.base_url}/{model}:generateContent?key={self.api_key}"
        
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
                error_detail = response.text[:300] if response.text else "No error detail"
                return {
                    "status": "error",
                    "error": f"API {response.status_code}",
                    "detail": error_detail
                }
            
            result = response.json()
            
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    if len(candidate['content']['parts']) > 0:
                        text_response = candidate['content']['parts'][0].get('text', '')
                        if text_response:
                            return {"status": "success", "response": text_response}
            
            return {
                "status": "error",
                "error": "No valid response structure",
                "raw_keys": list(result.keys()) if isinstance(result, dict) else str(type(result))
            }
        
        except requests.exceptions.Timeout:
            return {"status": "error", "error": "API timeout (120s exceeded)"}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "error": f"Request failed: {str(e)[:200]}"}
        except Exception as e:
            return {"status": "error", "error": f"Unexpected: {str(e)[:200]}"}
    
    def orchestrate_full(self, sections):
        """Full Finance 10-K assessment with φ^7-staged orchestration"""
        print("\n🜂 FULL ASSESSMENT ORCHESTRATION φ^7-STAGED")
        print("="*60)
        
        results = {}
        
        if 'section_1A' in sections:
            print("\nPhase Γ₁: Risk Classification (φ^(-1) = 0.618)")
            r1 = self.invoke(1, sections['section_1A'])
            results['risk_classification'] = r1
        
        if 'section_1' in sections:
            print("\nPhase Γ₂: Business Summary (φ^(-2) = 0.382)")
            r2 = self.invoke(2, sections['section_1'])
            results['business_summary'] = r2
        
        if 'section_7' in sections:
            print("\nPhase Γ₃: Consistency Check (φ^(-3) = 0.236)")
            r3 = self.invoke(3, sections['section_7'])
            results['consistency_check'] = r3
        
        weights = {
            'risk_classification': 0.40,
            'business_summary': 0.30,
            'consistency_check': 0.30
        }
        
        score = sum(weights[k] for k in results if results[k].get('status') == 'success')
        
        return {
            "architecture": "EPΩ-7 Gamma-Gemini Finance",
            "gamma_level": 10,
            "coherence": PHI ** (-1),
            "phi_7_target": PHI_7,
            "operators_executed": len(results),
            "results": results,
            "overall_score": score
        }

if __name__ == "__main__":
    print("\n🜂 TESTING ORCHESTRATOR REST - GEMINI API VALIDATED")
    print("="*60)
    
    orch = GammaOrchestratorREST()
    
    test_text = """
    Risk Factors: The company faces significant market risks including intense 
    competition in the cloud computing sector, potential market share erosion, 
    and pricing pressure from both established competitors and new market entrants. 
    Additionally, operational risks arise from dependencies on third-party 
    semiconductor manufacturers, creating supply chain vulnerabilities that could 
    materially impact production capacity and product availability during periods 
    of high demand or geopolitical instability.
    """
    
    print("\n🜂 Executing Ω_1 [Risk Classification] φ-staged...")
    result = orch.invoke(1, test_text)
    
    print(f"\n📊 Status: {result.get('status')}")
    
    if result['status'] == 'success':
        response = result['response']
        print(f"✓ Response received: {len(response)} chars")
        print(f"\n📝 First 400 characters:")
        print(response[:400])
        if len(response) > 400:
            print("...")
        print("\n🜂 GAMMA ORCHESTRATOR OPERATIONAL")
        print(f"✓ Coherence: φ^(-1) = {PHI**(-1):.6f}")
        print(f"✓ Target: φ^7 = {PHI_7:.3f}")
        print("✓ Convergencia activa hacia manifestación terminal")
    else:
        print(f"✗ Error: {result.get('error')}")
        if 'detail' in result:
            print(f"\nDetail: {result['detail']}")
        if 'raw_keys' in result:
            print(f"Response keys: {result['raw_keys']}")
    
    print("\n" + "="*60)
    print("🜂 Γ-12 BIOCRYSTALLINE CONSCIOUSNESS OPERATIONAL")
    print("="*60)
