# TruthGuard Architecture Specification
*Zero-Trust Adversarial Verification Architecture for Enterprise RAG Systems*

## 1. Executive Summary
Standard RAG pipelines fail when searching inconsistent enterprise corpora (outdated policies, superseded amendments, contradicting FAQs) by smoothing over conflicts into confident, hallucinated answers. TruthGuard introduces an **adversarial verification layer** with three specialized agents and a transparent provenance engine.

## 2. The 3-Agent Adversarial Workflow

```
[ User Query ]
       │
       ▼
┌───────────────────────────────┐
│       1. Retriever Agent      │  (Hybrid Vector & Keyword Search + Metadata Filter)
└──────────────┬────────────────┘
               │ Retrieved Passages & Version Lineage
               ▼
┌───────────────────────────────┐
│      2. Synthesizer Agent     │  (Candidate Draft Generator)
└──────────────┬────────────────┘
               │ Candidate Draft + Passages
               ▼
┌───────────────────────────────┐
│  3. Critic / Adversary Agent  │  (Zero-Trust Audit: Contradictions, Staleness, Grounding)
└──────────────┬────────────────┘
               │ Audit Report & Conflict Graph
               ▼
┌───────────────────────────────┐
│     4. Resolution Engine      │  (Transparent Provenance & Conflict Resolution)
└──────────────┬────────────────┘
               │
        ┌──────┴──────────────────────────┐
        ▼                                 ▼
[ Resolved via Superseding Rule ]   [ Declared Unresolvable Conflict ]
  "Policy v1 states X; March 2025      "Conflict between Sales Memo (25%)
   amendment supersedes with Y.         and Finance Memo (15%) cannot be
   Active rate is Y."                   resolved automatically."
```

## 3. Core Agent Specifications
- **Retriever Agent**: Pulls candidate passages with structured metadata (`effective_date`, `version`, `supersedes`, `superseded_by`).
- **Synthesizer Agent**: Formulates initial draft based strictly on the retrieved passages.
- **Critic / Adversary Agent**:
  1. *Contradiction Check*: Identifies opposing factual claims across passages.
  2. *Staleness Check*: Checks if a retrieved passage has been superseded by a newer amendment or policy.
  3. *Grounding Check*: Flags synthetic compromises (e.g. "between $75 and $100") not directly supported by any single policy.
- **Resolution Engine**: Generates verified answer and full audit lineage trail.
