"""
Synthesizer Agent: Generates an initial candidate answer based on retrieved passages.
In standard RAG, this would be the final output, often papering over discrepancies.
"""
from typing import List
from backend.app.models.schemas import RetrievedPassage, SynthesizerDraft

class SynthesizerAgent:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name

    async def synthesize(self, query: str, passages: List[RetrievedPassage]) -> SynthesizerDraft:
        """
        Drafts candidate answer strictly from contextual passages.
        """
        # Synthesizer draft generation implementation
        return SynthesizerDraft(
            draft_answer="",
            cited_passage_ids=[p.passage_id for p in passages]
        )
