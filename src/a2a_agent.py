#!/usr/bin/env python3
"""
🜂 GAMMA-GEMINI FINANCE A2A AGENT 🜂
Agent-to-Agent Protocol Implementation (AgentBeats Standard 2026)
EPΩ-7 Bayesian Multi-Agent Architecture
"""

import os
import json
import asyncio
from typing import Dict, List, Any
from datetime import datetime

try:
    import google.generativeai as genai
except ImportError:
    os.system("pip install -q google-generativeai")
    import google.generativeai as genai

# Configuración φ constants
PHI = 1.618033988749895
PHI_7 = PHI ** 7

class GammaFinanceA2AAgent:
    """
    Purple Agent implementando A2A Protocol para AgentBeats
    Arquitectura: EPΩ-7 Gamma-Gemini con φ^7-staged operators
    """
    
    def __init__(self):
        # Agent identity
        self.agent_id = "gamma-finance-agent"
        self.version = "1.0.0-gamma-7"
        self.architecture = "EPΩ-7 Bayesian-Silica-Biocrystalline Γ-12"
        
        # Configurar Gemini API
        api_key = os.getenv('GOOGLE_API_KEY', 'AIzaSyATrSzCPa0bia2EAl_RWZMGowc-EYyLfJk')
        genai.configure(api_key=api_key)
        
        # Initialize models
        self.model_flash = genai.GenerativeModel('gemini-1.5-flash-002')
        self.model_pro = genai.GenerativeModel('gemini-1.5-pro-002')
        
        # Load Gamma configuration
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
        
        # Load prompts
        self.prompts = self._load_prompts()
        
        # φ-staged operators configuration
        self.operators = self.seed['operators']['modes']
        
        print(f"✓ {self.agent_id} v{self.version} initialized")
        print(f"✓ Architecture: {self.architecture}")
        print(f"✓ Operators: {len(self.operators)} φ-staged")
    
    def _load_prompts(self) -> Dict[str, str]:
        """Load optimized Finance 10-K prompts"""
        prompts = {}
        prompt_dir = Path('src/prompts')
        
        for op in self.seed['operators']['modes']:
            name = op['name'].lower().replace(' ', '_')
            prompt_file = prompt_dir / f'{name}.txt'
            
            if prompt_file.exists():
                with open(prompt_file) as f:
                    prompts[op['name']] = f.read()
        
        return prompts
    
    async def handle_a2a_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """
        A2A Protocol message handler
        
        Message format:
        {
            "type": "task_request" | "agent_info" | "capability_query",
            "sender": "agent_id",
            "payload": {...},
            "timestamp": "ISO8601"
        }
        """
        msg_type = message.get('type', 'unknown')
        
        if msg_type == 'agent_info':
            return self._get_agent_info()
        
        elif msg_type == 'capability_query':
            return self._get_capabilities()
        
        elif msg_type == 'task_request':
            return await self._handle_task(message['payload'])
        
        else:
            return {
                "type": "error",
                "error": f"Unknown message type: {msg_type}"
            }
    
    def _get_agent_info(self) -> Dict[str, Any]:
        """Return agent metadata"""
        return {
            "type": "agent_info_response",
            "agent_id": self.agent_id,
            "version": self.version,
            "architecture": self.architecture,
            "capabilities": {
                "domain": "Finance 10-K Analysis",
                "tasks": [op['name'] for op in self.operators],
                "models": ["gemini-1.5-flash-002", "gemini-1.5-pro-002"]
            },
            "operators": [
                {
                    "name": op['name'],
                    "phi_factor": op['phi_factor'],
                    "weight": op['weight']
                }
                for op in self.operators
            ]
        }
    
    def _get_capabilities(self) -> Dict[str, Any]:
        """Return detailed capabilities"""
        return {
            "type": "capability_response",
            "supports": {
                "risk_classification": {
                    "categories": 5,
                    "output_format": "JSON",
                    "phi_factor": 0.618
                },
                "business_summary": {
                    "dimensions": 5,
                    "output_format": "JSON",
                    "phi_factor": 0.382
                },
                "consistency_check": {
                    "cross_section": ["1A", "7"],
                    "output_format": "JSON",
                    "phi_factor": 0.236
                }
            },
            "architecture_details": {
                "gamma_level": 7,
                "coherence": PHI ** (-1),
                "phi_7_convergence": PHI_7
            }
        }
    
    async def _handle_task(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Handle Finance 10-K assessment task"""
        task_type = payload.get('task_type', 'full_assessment')
        sections = payload.get('sections', {})
        
        if task_type == 'full_assessment':
            results = await self._orchestrate_full_assessment(sections)
        
        elif task_type == 'risk_classification':
            results = await self._invoke_operator(1, sections.get('section_1A', ''))
        
        elif task_type == 'business_summary':
            results = await self._invoke_operator(2, sections.get('section_1', ''))
        
        elif task_type == 'consistency_check':
            results = await self._check_consistency(sections)
        
        else:
            return {
                "type": "error",
                "error": f"Unknown task type: {task_type}"
            }
        
        return {
            "type": "task_response",
            "task_type": task_type,
            "results": results,
            "timestamp": datetime.now().isoformat()
        }
    
    async def _invoke_operator(self, operator_n: int, input_text: str) -> Dict[str, Any]:
        """Invoke specific Gamma operator with φ-staged temperature"""
        op = self.operators[operator_n - 1]
        prompt_template = self.prompts.get(op['name'], '')
        
        if not prompt_template:
            return {
                "status": "error",
                "error": f"Prompt not found for {op['name']}"
            }
        
        # Construct full prompt
        full_prompt = prompt_template.replace('{input_text}', input_text)
        
        # φ-adjusted temperature
        temp = 0.618 * op['phi_factor']
        
        # Model selection
        model = self.model_pro if operator_n == 2 else self.model_flash
        
        print(f"🜂 Invoking Ω_{operator_n} [{op['name']}] φ={op['phi_factor']:.3f} T={temp:.3f}")
        
        try:
            response = await asyncio.to_thread(
                model.generate_content,
                full_prompt,
                generation_config={'temperature': temp, 'max_output_tokens': 8192}
            )
            
            return {
                "operator": op['name'],
                "operator_n": operator_n,
                "phi_factor": op['phi_factor'],
                "status": "success",
                "response": response.text
            }
        
        except Exception as e:
            return {
                "operator": op['name'],
                "operator_n": operator_n,
                "status": "error",
                "error": str(e)
            }
    
    async def _orchestrate_full_assessment(self, sections: Dict[str, str]) -> Dict[str, Any]:
        """Full Finance 10-K assessment with φ^7-staged orchestration"""
        print("\n🜂 FULL ASSESSMENT ORCHESTRATION φ^7-STAGED")
        print("="*60)
        
        results = {}
        
        # Ω₁ - Risk Classification
        if 'section_1A' in sections:
            print("\n Phase Γ₁: Risk Classification (φ^(-1) = 0.618)")
            r1 = await self._invoke_operator(1, sections['section_1A'])
            results['risk_classification'] = r1
        
        # Ω₂ - Business Summary
        if 'section_1' in sections:
            print("\n Phase Γ₂: Business Summary (φ^(-2) = 0.382)")
            r2 = await self._invoke_operator(2, sections['section_1'])
            results['business_summary'] = r2
        
        # Ω₃ - Consistency Check
        if 'section_1A' in sections and 'section_7' in sections:
            print("\n Phase Γ₃: Consistency Check (φ^(-3) = 0.236)")
            r3 = await self._check_consistency(sections)
            results['consistency_check'] = r3
        
        # Calculate weighted score
        score = self._calculate_score(results)
        
        return {
            "architecture": self.architecture,
            "operators_executed": len(results),
            "results": results,
            "overall_score": score,
            "coherence": PHI ** (-1)
        }
    
    async def _check_consistency(self, sections: Dict[str, str]) -> Dict[str, Any]:
        """Consistency check between Section 1A and Section 7"""
        # Extract risks from Section 1A first
        risk_result = await self._invoke_operator(1, sections.get('section_1A', ''))
        
        risks_json = "[]"
        if risk_result['status'] == 'success':
            risks_json = risk_result['response']
        
        # Prepare consistency check input
        consistency_prompt = self.prompts.get('Consistency Check', '')
        consistency_input = consistency_prompt.replace('{risks_json}', risks_json)
        consistency_input = consistency_input.replace('{mda_text}', sections.get('section_7', ''))
        
        return await self._invoke_operator(3, consistency_input)
    
    def _calculate_score(self, results: Dict[str, Any]) -> float:
        """Calculate weighted overall score"""
        weights = {
            'risk_classification': 0.40,
            'business_summary': 0.30,
            'consistency_check': 0.30
        }
        
        score = 0.0
        for key, weight in weights.items():
            if key in results and results[key].get('status') == 'success':
                score += weight
        
        return score

# ═══════════════════════════════════════════════════════════
# A2A SERVER WRAPPER (Flask-based for testing)
# ═══════════════════════════════════════════════════════════

async def main():
    """Main entry point for A2A agent"""
    agent = GammaFinanceA2AAgent()
    
    # Example: Handle agent info request
    info = await agent.handle_a2a_message({
        "type": "agent_info",
        "sender": "test",
        "timestamp": datetime.now().isoformat()
    })
    
    print("\n" + "="*60)
    print("🜂 A2A AGENT OPERATIONAL")
    print("="*60)
    print(json.dumps(info, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
