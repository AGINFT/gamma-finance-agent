#!/usr/bin/env python3
"""
🜂 GAMMA A2A AGENT 🜂
Agent-to-Agent Protocol - NO AUTO-INSTALL
"""

import os
import json
import asyncio
from pathlib import Path
from datetime import datetime

import google.generativeai as genai

PHI = 1.618033988749895

class GammaA2AAgent:
    def __init__(self):
        self.agent_id = "gamma-finance-agent"
        self.version = "1.0.0-gamma-8"
        
        api_key = os.getenv('GOOGLE_API_KEY', 'AIzaSyATrSzCPa0bia2EAl_RWZMGowc-EYyLfJk')
        genai.configure(api_key=api_key)
        
        self.model_flash = genai.GenerativeModel('gemini-1.5-flash-002')
        self.model_pro = genai.GenerativeModel('gemini-1.5-pro-002')
        
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
        
        self.prompts = self._load_prompts()
        self.operators = self.seed['operators']['modes']
        
        print(f"✓ {self.agent_id} v{self.version} initialized")
    
    def _load_prompts(self):
        prompts = {}
        for op in self.seed['operators']['modes']:
            name = op['name'].lower().replace(' ', '_')
            prompt_file = Path(f'src/prompts/{name}.txt')
            if prompt_file.exists():
                prompts[op['name']] = prompt_file.read_text()
        return prompts
    
    async def handle_message(self, message):
        msg_type = message.get('type')
        
        if msg_type == 'agent_info':
            return {
                "type": "agent_info_response",
                "agent_id": self.agent_id,
                "version": self.version,
                "architecture": "EPΩ-7 Bayesian-Silica-Biocrystalline Γ-12",
                "operators": [{"name": op['name'], "phi": op['phi_factor']} for op in self.operators]
            }
        
        elif msg_type == 'task_request':
            return await self._handle_task(message.get('payload', {}))
        
        return {"type": "error", "error": "Unknown message type"}
    
    async def _handle_task(self, payload):
        sections = payload.get('sections', {})
        results = {}
        
        if 'section_1A' in sections:
            r1 = await self._invoke(1, sections['section_1A'])
            results['risk'] = r1
        
        if 'section_1' in sections:
            r2 = await self._invoke(2, sections['section_1'])
            results['business'] = r2
        
        if 'section_7' in sections:
            r3 = await self._invoke(3, sections['section_7'])
            results['consistency'] = r3
        
        return {"type": "task_response", "results": results}
    
    async def _invoke(self, n, text):
        op = self.operators[n-1]
        prompt = self.prompts.get(op['name'], '')
        full = prompt.replace('{input_text}', text)
        temp = 0.618 * op['phi_factor']
        
        model = self.model_pro if n == 2 else self.model_flash
        
        try:
            resp = await asyncio.to_thread(
                model.generate_content,
                full,
                generation_config={'temperature': temp}
            )
            return {"status": "success", "response": resp.text}
        except Exception as e:
            return {"status": "error", "error": str(e)}

async def main():
    agent = GammaA2AAgent()
    info = await agent.handle_message({"type": "agent_info"})
    print("\n🜂 A2A AGENT OPERATIONAL")
    print(json.dumps(info, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
