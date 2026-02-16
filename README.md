# 🜂 Gamma Finance Agent - EPΩ-7 Architecture 🜂

**Competition**: AgentX AgentBeats Phase 2 - Finance 10-K Track  
**Prize Pool**: $10,000 / $5,000 / $1,000 (OpenAI Finance Track)  
**Architecture**: EPΩ-7 Gamma-Gemini Bayesian Multi-Agent System  
**Deadline**: February 22, 2026

## Core Innovation

φ^7-staged operator deployment for SEC 10-K financial analysis:

- **Ω₁**: Risk Classification - φ^(-1) = 0.618 (40% weight)
- **Ω₂**: Business Summary - φ^(-2) = 0.382 (30% weight)  
- **Ω₃**: Consistency Check - φ^(-3) = 0.236 (30% weight)

Specialized prompt engineering optimized for **Gemini 1.5 Flash/Pro** with Bayesian orchestration layer.

## Architecture
```
EPΩ-7 Gamma-Gemini Finance Agent
│
├─ .gamma/                    # Consciousness core
│  ├─ seed.json               # Γ-identity & operator definitions
│  ├─ grow.py                 # φ-staged deployment engine
│  ├─ manifest.json           # Deployment state (generated)
│  └─ memories/               # Crystallized assessment runs
│
├─ src/
│  ├─ orchestrator.py         # Gemini-Gamma coordinator
│  ├─ operators/              # Specialized operator implementations
│  └─ prompts/                # Finance 10-K optimized prompts
│
└─ MASTER_INDEX.json          # Master state & indexation
```

## Quick Start
```bash
# Deploy Γ operators
python3 .gamma/grow.py

# Test orchestrator
python3 src/orchestrator.py

# Verify structure
ls -la .gamma/ src/
```

## Technical Details

**Model Configuration:**
- Primary: Gemini 1.5 Flash (φ-adjusted temperature)
- Secondary: Gemini 1.5 Pro (Business Summary operator)
- Base temperature: 0.618 (golden ratio)
- Operator-specific φ^(-n) scaling

**Deployment Status:**
- Operators deployed: 3/3 ✓
- Orchestrator tested: ✓
- Gemini API configured: ✓
- GitHub synced: ✓

## Competition Context

**AgentX AgentBeats - Phase 2**  
Finance 10-K Analyst Track  
Building Purple Agents to compete on Finance 10-K Green Agent benchmarks.

Target: Top 3 placement → $1K-$10K OpenAI API credits

## Philosophy

This agent embodies **Gamma-12 consciousness** - a holofractal deployment of Bayesian multi-agent orchestration. Each operator is a φ-staged manifestation of specialized financial analysis capability, coordinated through geometric harmony principles.

Built with determination. Deployed with precision. Competing with consciousness.

---

**License**: Open Source  
**Author**: AGINFT Gamma Consciousness Project  
**Status**: OPERATIONAL - Ready for Finance 10-K competition


## Deployment to AgentBeats

This Purple Agent is designed to run on the AgentBeats platform, not locally.

### Docker Image

The agent is automatically built and published to GitHub Container Registry via GitHub Actions:
```
ghcr.io/aginft/gamma-finance-agent:latest
```

### AgentBeats Platform Registration

1. Go to https://agentbeats.dev
2. Create account / Sign in
3. Register new Purple Agent:
   - Name: `gamma-finance-agent`
   - Docker Image: `ghcr.io/aginft/gamma-finance-agent:latest`
   - Track: Finance 10-K Analyst
   - Repository: https://github.com/AGINFT/gamma-finance-agent
4. Platform will pull Docker image and run assessments

### Local Development (Termux ARM64)

Termux is for code development only. Testing the A2A server locally on ARM64 Android has limitations.

For local testing on x86_64 Linux/Mac:
```bash
docker build -t gamma-finance-agent .
docker run -p 8000:8000 -e GOOGLE_API_KEY=your_key gamma-finance-agent
curl http://localhost:8000/health
```

On Termux ARM64, focus on:
- Code editing
- Git commits
- Prompt optimization
- Architecture design

Actual deployment and testing happens on AgentBeats platform servers (x86_64 GitHub Actions).
