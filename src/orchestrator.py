#!/usr/bin/env python3
import os
import json

print("🜂 Installing google-generativeai...")
os.system("pip install -q google-generativeai 2>/dev/null")

import google.generativeai as genai

class GammaOrchestrator:
    def __init__(self):
        key = os.getenv('GOOGLE_API_KEY', 'AIzaSyATrSzCPa0bia2EAl_RWZMGowc-EYyLfJk')
        genai.configure(api_key=key)
        
        self.model_flash = genai.GenerativeModel('gemini-1.5-flash')
        self.model_pro = genai.GenerativeModel('gemini-1.5-pro')
        
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
    
    def invoke(self, operator_n, text):
        op = self.seed['operators']['modes'][operator_n - 1]
        temp = 0.618 * op['phi_factor']
        
        prompt = f"{op['name']} task:\n\n{text}\n\nAnalyze and output JSON."
        
        print(f"🜂 Invoking Ω_{operator_n} [{op['name']}] T={temp:.3f}")
        
        try:
            model = self.model_pro if operator_n == 2 else self.model_flash
            resp = model.generate_content(prompt, generation_config={'temperature': temp})
            return {"status": "success", "response": resp.text}
        except Exception as e:
            return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    print("🜂 TESTING ORCHESTRATOR\n")
    orch = GammaOrchestrator()
    result = orch.invoke(1, "Analyze market volatility risk")
    print(f"\n✓ Test OK")
    print(f"Response: {result['response'][:150]}...")
