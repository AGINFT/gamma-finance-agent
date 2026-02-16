#!/usr/bin/env python3
"""
🜂 GAMMA-GEMINI ORCHESTRATOR 🜂
EPΩ-7 Bayesian Orchestration Engine
NO AUTO-INSTALL - Dependencies must be pre-installed
"""

import os
import json
from pathlib import Path

# NO auto-install - assume dependencies exist
import google.generativeai as genai

PHI = 1.618033988749895

class GammaOrchestrator:
    def __init__(self):
        api_key = os.getenv('GOOGLE_API_KEY', 'AIzaSyATrSzCPa0bia2EAl_RWZMGowc-EYyLfJk')
        genai.configure(api_key=api_key)
        
        self.model_flash = genai.GenerativeModel('gemini-1.5-flash-002')
        self.model_pro = genai.GenerativeModel('gemini-1.5-pro-002')
        
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
        
        self.prompts = self._load_prompts()
        
        print(f"✓ Gamma Orchestrator initialized")
        print(f"✓ Operators: {len(self.seed['operators']['modes'])}")
    
    def _load_prompts(self):
        prompts = {}
        prompt_dir = Path('src/prompts')
        
        for op in self.seed['operators']['modes']:
            name = op['name'].lower().replace(' ', '_')
            prompt_file = prompt_dir / f'{name}.txt'
            
            if prompt_file.exists():
                with open(prompt_file) as f:
                    prompts[op['name']] = f.read()
        
        return prompts
    
    def invoke(self, operator_n, text):
        op = self.seed['operators']['modes'][operator_n - 1]
        prompt = self.prompts.get(op['name'], '')
        
        if not prompt:
            return {"error": f"Prompt not found for {op['name']}"}
        
        full_prompt = prompt.replace('{input_text}', text)
        temp = 0.618 * op['phi_factor']
        
        model = self.model_pro if operator_n == 2 else self.model_flash
        
        print(f"🜂 Ω_{operator_n} [{op['name']}] φ={op['phi_factor']:.3f} T={temp:.3f}")
        
        try:
            resp = model.generate_content(
                full_prompt,
                generation_config={'temperature': temp, 'max_output_tokens': 8192}
            )
            return {"status": "success", "response": resp.text}
        except Exception as e:
            return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    print("\n🜂 TESTING ORCHESTRATOR (no auto-install)")
    orch = GammaOrchestrator()
    result = orch.invoke(1, "Test: market volatility risk analysis")
    print(f"\n✓ Test: {result.get('status', 'unknown')}")
