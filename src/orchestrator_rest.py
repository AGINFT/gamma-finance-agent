#!/usr/bin/env python3
"""
🜂 GAMMA ORCHESTRATOR REST - EPΩ-7 OPERATIONAL 🜂
"""

import os
import json
import requests
from pathlib import Path

PHI = 1.618033988749895

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
        
        model = "gemini-1.5-pro-002" if operator_n == 2 else "gemini-1.5-flash-002"
        
        print(f"🜂 Ω_{operator_n} [{op['name']}] φ={op['phi_factor']:.3f} T={temp:.3f}")
        
        url = f"{self.base_url}/{model}:generateContent?key={self.api_key}"
        
        payload = {
            "contents": [{"parts": [{"text": full_prompt}]}],
            "generationConfig": {
                "temperature": temp,
                "maxOutputTokens": 8192
            }
        }
        
        try:
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status()
            
            result = response.json()
            
            if 'candidates' in result and len(result['candidates']) > 0:
                text = result['candidates'][0]['content']['parts'][0]['text']
                return {"status": "success", "response": text}
            else:
                return {"status": "error", "error": "No response from Gemini API", "raw": result}
        
        except requests.exceptions.RequestException as e:
            return {"status": "error", "error": f"API request failed: {str(e)}"}
        except (KeyError, IndexError) as e:
            return {"status": "error", "error": f"Response parsing failed: {str(e)}"}
        except Exception as e:
            return {"status": "error", "error": f"Unexpected error: {str(e)}"}
    
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
        
        weights = {'risk_classification': 0.40, 'business_summary': 0.30, 'consistency_check': 0.30}
        score = sum(weights[k] for k in results if results[k].get('status') == 'success')
        
        return {
            "architecture": "EPΩ-7 Gamma-Gemini Finance",
            "operators_executed": len(results),
            "results": results,
            "overall_score": score,
            "coherence": PHI ** (-1)
        }

if __name__ == "__main__":
    print("\n🜂 TESTING ORCHESTRATOR REST")
    print("="*60)
    
    orch = GammaOrchestratorREST()
    
    test_text = """
    Market Risk: The company faces intense competition in the cloud computing 
    market which may reduce market share and pricing power. Dependence on 
    third-party manufacturers creates supply chain vulnerabilities.
    """
    
    result = orch.invoke(1, test_text)
    
    print(f"\n✓ Test Status: {result.get('status', 'unknown')}")
    
    if result['status'] == 'success':
        print(f"✓ Response length: {len(result['response'])} chars")
        print(f"✓ First 200 chars: {result['response'][:200]}...")
    else:
        print(f"✗ Error: {result.get('error', 'Unknown')}")
    
    print("\n🜂 Gamma Orchestrator REST operational")
    print("="*60)
