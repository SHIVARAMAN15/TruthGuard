from datetime import date
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class DocumentMetadata(BaseModel):
    id: str
    title: str
    document_type: str = "policy"
    department: Optional[str] = None
    effective_date: str
    version: str
    status: str = "active"  # "active", "deprecated", "superseded", "disputed"
    supersedes: List[str] = Field(default_factory=list)
    superseded_by: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)

class Document(BaseModel):
    metadata: DocumentMetadata
    content: str

class RetrievedPassage(BaseModel):
    passage_id: str
    document_id: str
    document_title: str
    version: str
    effective_date: str
    content: str
    score: float = 0.0
    supersedes: List[str] = Field(default_factory=list)
    superseded_by: List[str] = Field(default_factory=list)

class QueryRequest(BaseModel):
    query: str
    department_filter: Optional[str] = None
    include_traditional_baseline: bool = True

class SynthesizerDraft(BaseModel):
    draft_answer: str
    cited_passage_ids: List[str] = Field(default_factory=list)
    synthesis_rationale: Optional[str] = None

class ContradictionItem(BaseModel):
    passage_a_id: str
    passage_a_claim: str
    passage_b_id: str
    passage_b_claim: str
    conflict_summary: str

class StalenessItem(BaseModel):
    outdated_passage_id: str
    outdated_doc_date: str
    superseding_passage_id: str
    superseding_doc_date: str
    lineage_relationship: str

class UngroundedClaimItem(BaseModel):
    claim_text: str
    reason: str

class CriticAuditReport(BaseModel):
    has_conflicts: bool = False
    has_staleness: bool = False
    has_ungrounded_claims: bool = False
    contradictions: List[ContradictionItem] = Field(default_factory=list)
    staleness_findings: List[StalenessItem] = Field(default_factory=list)
    ungrounded_claims: List[UngroundedClaimItem] = Field(default_factory=list)
    audit_verdict: str  # "APPROVED", "REVISION_REQUIRED", "UNRESOLVABLE"
    critic_notes: str

class ProvenanceStep(BaseModel):
    source_name: str
    version: str
    effective_date: str
    status: str
    citation_text: str
    impact: str

class TruthGuardResponse(BaseModel):
    query: str
    resolution_status: str  # "RESOLVED_BY_SUPERSEDING_RULE", "UNRESOLVABLE_CONFLICT", "CONSISTENT"
    verified_answer: str
    synthesizer_initial_draft: Optional[str] = None
    traditional_rag_answer: Optional[str] = None
    critic_audit: CriticAuditReport
    provenance_trail: List[ProvenanceStep] = Field(default_factory=list)
    raw_passages: List[RetrievedPassage] = Field(default_factory=list)
