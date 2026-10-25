"""
TruthGuard Multi-Agent Workflow Orchestrator:
Coordinates Retriever -> Synthesizer -> Critic (Adversarial Audit) -> Resolution Engine.
"""
from typing import Dict, Any
from backend.app.agents.retriever_agent import RetrieverAgent
from backend.app.agents.synthesizer_agent import SynthesizerAgent
from backend.app.agents.critic_agent import CriticAgent
from backend.app.agents.resolution_agent import ResolutionAgent
from backend.app.models.schemas import TruthGuardResponse

class TruthGuardWorkflow:
    def __init__(self):
        self.retriever = RetrieverAgent()
        self.synthesizer = SynthesizerAgent()
        self.critic = CriticAgent()
        self.resolver = ResolutionAgent()

    async def execute(self, query: str) -> TruthGuardResponse:
        """
        Executes the end-to-end multi-agent verification pipeline.
        """
        # Step 1: Retrieval
        passages = await self.retriever.retrieve(query)
        
        # Step 2: Synthesis
        draft = await self.synthesizer.synthesize(query, passages)
        
        # Step 3: Adversarial Audit
        audit = await self.critic.audit(query, draft, passages)
        
        # Step 4: Resolution & Provenance Trail
        response = await self.resolver.resolve(query, draft, audit, passages)
        
        return response
