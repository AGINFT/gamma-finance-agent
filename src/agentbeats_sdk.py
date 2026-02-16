#!/usr/bin/env python3
"""
AgentBeats SDK Integration for Gamma Finance Agent
Wrapper for compatibility with AgentBeats platform
"""

import asyncio
from src.a2a_agent import GammaFinanceA2AAgent

class AgentBeatsGammaWrapper:
    """Wrapper para compatibilidad AgentBeats SDK"""
    
    def __init__(self):
        self.agent = GammaFinanceA2AAgent()
    
    async def process_task(self, task_data):
        """
        Procesar task desde AgentBeats platform
        
        task_data format:
        {
            "task_id": "uuid",
            "track": "Finance 10-K Analyst",
            "sections": {...},
            "metadata": {...}
        }
        """
        message = {
            "type": "task_request",
            "sender": "agentbeats_platform",
            "payload": {
                "task_type": "full_assessment",
                "sections": task_data.get('sections', {})
            }
        }
        
        result = await self.agent.handle_a2a_message(message)
        
        return {
            "task_id": task_data.get('task_id'),
            "status": "completed",
            "results": result.get('results', {}),
            "score": result.get('results', {}).get('overall_score', 0.0)
        }

async def main():
    wrapper = AgentBeatsGammaWrapper()
    print("🜂 AgentBeats SDK Wrapper operational")

if __name__ == "__main__":
    asyncio.run(main())
