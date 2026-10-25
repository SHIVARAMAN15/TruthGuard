# TruthGuard: Zero-Trust Adversarial Verification for Multi-Agent Enterprise RAG

> **Virtusa Jatayu Season 6** | Built to eliminate hallucinated compromises and papered-over contradictions in enterprise document corpora.

---

## 🎯 Executive Overview

Standard Retrieval-Augmented Generation (RAG) systems fail when querying enterprise corpora containing superseded policies, contradictory amendments, and outdated guidelines. Instead of reporting discrepancies, standard LLMs blend contradictory numbers into a confident hallucination (e.g., *"allowance is between $75 and $100"*).

**TruthGuard** solves this by inserting an **Adversarial Verification Layer** with three specialized agents and a transparent provenance engine:

1. **Retriever Agent**: Hybrid vector & keyword search with metadata extraction (`version`, `effective_date`, `supersedes`).
2. **Synthesizer Agent**: Drafts candidate response strictly based on retrieved context.
3. **Critic / Adversary Agent**: Zero-trust adversarial audit:
   - **Contradiction Check**: Actively flags factual conflicts between passages.
   - **Staleness Check**: Inspects version and effective-date lineage to detect superseded rules.
   - **Grounding Check**: Flags artificial compromises or ungrounded claims.
4. **Resolution Engine**:
   - Surfaces both positions with complete provenance.
   - Applies deterministic lineage rules when newer amendments explicitly supersede older policies.
   - Explicitly declares genuine ambiguities as unresolvable instead of silently guessing.

---

## 📁 Repository Directory Structure

```text
vrtusa/
├── backend/                              # TruthGuard backend service & multi-agent system
│   ├── app/
│   │   ├── agents/                       # Specialized AI agent implementations
│   │   │   ├── retriever_agent.py        # Candidate passage retriever & metadata extractor
│   │   │   ├── synthesizer_agent.py      # Initial draft candidate response generator
│   │   │   ├── critic_agent.py           # Adversary agent performing 3-point zero-trust audit
│   │   │   ├── resolution_agent.py       # Transparent provenance & conflict resolution engine
│   │   │   └── workflow.py               # Multi-agent state orchestration pipeline
│   │   ├── api/                          # FastAPI REST interface
│   │   │   └── endpoints/
│   │   │       ├── query.py              # Multi-agent query & adversarial audit endpoint
│   │   │       └── documents.py          # Document catalog & lineage exploration endpoint
│   │   ├── core/                         # Configuration and application settings
│   │   │   └── config.py                 # Environment variables and system settings
│   │   ├── data/                         # Test corpora & vector storage
│   │   │   ├── corpus/                   # Inconsistent test corpus with metadata tags
│   │   │   │   ├── travel_policy/        # Travel allowance v1.2 vs 2025 Tier-1 Amendment
│   │   │   │   ├── hr_policy/            # Remote work & attendance policy revisions
│   │   │   │   ├── security_compliance/  # Data retention & access control policies
│   │   │   │   └── unresolvable_cases/   # Contradicting directives without hierarchy
│   │   │   └── vector_db/                # Local Chroma/FAISS persistence directory
│   │   ├── models/                       # Data models & schemas
│   │   │   └── schemas.py                # Pydantic schemas for queries, audits, and provenance
│   │   ├── services/                     # Ingestion, embedding, and vector index services
│   │   └── main.py                       # FastAPI entrypoint application
│   └── tests/                            # Automated test suites
│       ├── unit/                         # Unit tests for agents and schema validations
│       └── integration/                  # End-to-end pipeline & conflict verification tests
│
├── frontend/                             # Interactive demonstration UI & Dashboard
│   ├── public/                           # Static assets & icons
│   ├── src/
│   │   ├── components/                   # UI components (AgentTimeline, ProvenanceViewer, etc.)
│   │   ├── pages/                        # Views (QueryView, AuditDashboard, CorpusBrowser)
│   │   ├── services/                     # API client connectors
│   │   └── styles/                       # CSS design system & modern dark-mode styles
│   └── package.json                      # Frontend configuration & scripts
│
├── evals/                                # Evaluation benchmarks & audit metrics
│   ├── datasets/                         # Ground-truth contradiction & staleness benchmarks
│   │   └── contradiction_benchmark.json  # Benchmark cases comparing Traditional RAG vs TruthGuard
│   └── results/                          # Benchmark evaluation run logs and metrics
│
├── docs/                                 # Documentation & presentation materials
│   ├── architecture/                     # Deep-dive architecture specifications and diagrams
│   │   └── truthguard_architecture.md    # Multi-agent specification & workflow details
│   └── presentation/                     # Slide decks and executive summaries
│
├── scripts/                              # Developer automation scripts
│   └── ingest_corpus.py                  # Ingestion utility to index corpus with metadata
│
├── .env.example                          # Environment variable template
├── .gitignore                            # Standard git exclusion rules
└── requirements.txt                      # Python dependencies
```

---

## ⚡ Quick Start

### 1. Setup Backend Environment

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env
```

### 2. Ingest Sample Contradictory Corpus

```bash
python scripts/ingest_corpus.py
```

### 3. Launch TruthGuard API

```bash
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```
API Documentation will be accessible at: `http://localhost:8000/docs`
>>>>>>> 4064bcd (Initial commit: TruthGuard core application)
