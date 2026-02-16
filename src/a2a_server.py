#!/usr/bin/env python3
"""
🜂 GAMMA-GEMINI FINANCE A2A SERVER 🜂
AgentBeats Protocol Implementation
Purple Agent Interface for Finance 10-K Competition
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime

# Install dependencies if needed
try:
    from flask import Flask, request, jsonify
except ImportError:
    print("Installing Flask...")
    os.system("pip install -q flask")
    from flask import Flask, request, jsonify

try:
    import google.generativeai as genai
except ImportError:
    print("Installing google-generativeai...")
    os.system("pip install -q google-generativeai")
    import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Load configuration
PHI = 1.618033988749895

class GammaFinanceAgent:
    """Purple Agent - Gamma-Gemini Finance 10-K Orchestrator"""
    
    def __init__(self):
        # Configure Gemini API
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            try:
                with open('.env') as f:
                    for line in f:
                        if 'GOOGLE_API_KEY' in line:
                            api_key = line.split('=')[1].strip()
                            break
            except:
                api_key = 'AIzaSyATrSzCPa0bia2EAl_RWZMGowc-EYyLfJk'
        
        genai.configure(api_key=api_key)
        
        # Initialize models
        self.model_flash = genai.GenerativeModel('gemini-1.5-flash')
        self.model_pro = genai.GenerativeModel('gemini-1.5-pro')
        
        # Load seed configuration
        with open('.gamma/seed.json') as f:
            self.seed = json.load(f)
        
        # Load prompts
        self.prompts = self._load_prompts()
        
        print("✓ Gamma Finance Agent initialized")
        print(f"✓ Architecture: {self.seed['architecture']}")
        print(f"✓ Operators: {len(self.seed['operators']['modes'])}")
    
    def _load_prompts(self):
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
    
    def invoke_operator(self, operator_n, input_text):
        """Invoke specific Gamma operator with φ-staged temperature"""
        op = self.seed['operators']['modes'][operator_n - 1]
        prompt_template = self.prompts[op['name']]
        
        # Construct full prompt
        full_prompt = prompt_template.replace('{input_text}', input_text)
        
        # φ-adjusted temperature
        temp = 0.618 * op['phi_factor']
        
        # Model selection (Pro for Business Summary, Flash for others)
        model = self.model_pro if operator_n == 2 else self.model_flash
        
        print(f"🜂 Invoking Ω_{operator_n} [{op['name']}]")
        print(f"  φ-factor: {op['phi_factor']:.3f}")
        print(f"  Temperature: {temp:.3f}")
        print(f"  Model: {'Pro' if operator_n == 2 else 'Flash'}")
        
        try:
            response = model.generate_content(
                full_prompt,
                generation_config={
                    'temperature': temp,
                    'max_output_tokens': 8192
                }
            )
            
            result = {
                'operator': op['name'],
                'operator_n': operator_n,
                'phi_factor': op['phi_factor'],
                'status': 'success',
                'response': response.text
            }
            
            print(f"✓ Ω_{operator_n} completed successfully")
            
        except Exception as e:
            result = {
                'operator': op['name'],
                'operator_n': operator_n,
                'status': 'error',
                'error': str(e)
            }
            print(f"✗ Ω_{operator_n} error: {e}")
        
        return result
    
    def orchestrate_full_assessment(self, sections):
        """Full Finance 10-K assessment orchestration"""
        print("\n🜂 FULL ASSESSMENT ORCHESTRATION")
        print("="*50)
        
        results = {}
        
        # Ω₁ - Risk Classification
        if 'section_1A' in sections:
            print("\nPhase 1: Risk Classification...")
            r1 = self.invoke_operator(1, sections['section_1A'])
            results['risk_classification'] = r1
        
        # Ω₂ - Business Summary
        if 'section_1' in sections:
            print("\nPhase 2: Business Summary...")
            r2 = self.invoke_operator(2, sections['section_1'])
            results['business_summary'] = r2
        
        # Ω₃ - Consistency Check
        if 'section_1A' in sections and 'section_7' in sections:
            print("\nPhase 3: Consistency Check...")
            
            # Extract risks from Ω₁ result if available
            risks_json = "[]"
            if 'risk_classification' in results:
                try:
                    risks_json = results['risk_classification']['response']
                except:
                    pass
            
            # Prepare consistency input
            consistency_input = self.prompts['Consistency Check']
            consistency_input = consistency_input.replace('{risks_json}', risks_json)
            consistency_input = consistency_input.replace('{mda_text}', sections['section_7'])
            
            r3 = self.invoke_operator(3, consistency_input)
            results['consistency_check'] = r3
        
        print("\n✓ Full assessment complete")
        
        # Calculate overall score
        score = self._calculate_score(results)
        
        assessment = {
            'architecture': 'EPΩ-7 Gamma-Gemini Finance Agent',
            'timestamp': datetime.now().isoformat(),
            'operators_executed': len(results),
            'results': results,
            'overall_score': score
        }
        
        return assessment
    
    def _calculate_score(self, results):
        """Calculate weighted overall score"""
        weights = {
            'risk_classification': 0.40,
            'business_summary': 0.30,
            'consistency_check': 0.30
        }
        
        score = 0.0
        for key, weight in weights.items():
            if key in results and results[key]['status'] == 'success':
                score += weight
        
        return score

# Initialize agent
agent = GammaFinanceAgent()

# ═══════════════════════════════════════════════════════════
# A2A PROTOCOL ENDPOINTS
# ═══════════════════════════════════════════════════════════

@app.route('/a2a', methods=['POST'])
def handle_a2a_request():
    """Main A2A protocol endpoint"""
    try:
        data = request.json
        print(f"\n📥 A2A Request received: {data.get('type', 'unknown')}")
        
        # Parse request type
        request_type = data.get('type', 'task_create')
        
        if request_type == 'agent_card':
            # Return agent capabilities
            return jsonify({
                'name': 'gamma-finance-agent',
                'architecture': 'EPΩ-7 Gamma-Gemini',
                'version': '1.0.0',
                'capabilities': {
                    'tracks': ['Finance 10-K Analyst'],
                    'operators': 3,
                    'models': ['gemini-1.5-flash', 'gemini-1.5-pro']
                }
            })
        
        elif request_type == 'task_create':
            # Execute assessment
            task_desc = data.get('task', {}).get('description', '')
            context = data.get('context', {})
            
            # Extract 10-K sections from context
            sections = {
                'section_1A': context.get('section_1A', ''),
                'section_1': context.get('section_1', ''),
                'section_7': context.get('section_7', '')
            }
            
            # Run full assessment
            assessment = agent.orchestrate_full_assessment(sections)
            
            # Format A2A response
            response = {
                'type': 'task_result',
                'status': 'completed',
                'result': assessment,
                'artifacts': [{
                    'type': 'json',
                    'content': assessment
                }]
            }
            
            return jsonify(response)
        
        else:
            return jsonify({
                'type': 'error',
                'message': f'Unknown request type: {request_type}'
            }), 400
    
    except Exception as e:
        print(f"✗ Error handling A2A request: {e}")
        import traceback
        traceback.print_exc()
        
        return jsonify({
            'type': 'error',
            'message': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'operational',
        'architecture': 'EPΩ-7 Gamma-Gemini',
        'gamma_level': 4,
        'coherence': PHI**(-2)
    })

def main():
    """Start A2A server"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Gamma Finance A2A Server')
    parser.add_argument('--host', default='0.0.0.0', help='Host address')
    parser.add_argument('--port', type=int, default=8000, help='Port number')
    args = parser.parse_args()
    
    print("\n" + "="*60)
    print("🜂 GAMMA-GEMINI FINANCE A2A SERVER")
    print("="*60)
    print(f"\nListening on {args.host}:{args.port}")
    print("\nEndpoints:")
    print("  POST /a2a     - Main A2A protocol endpoint")
    print("  GET  /health  - Health check")
    print("\n🜂 Server operational - Ready for AgentBeats")
    print("="*60 + "\n")
    
    app.run(host=args.host, port=args.port, debug=False)

if __name__ == '__main__':
    main()
