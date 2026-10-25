"""
Query endpoint: Dispatches user questions to TruthGuard Multi-Agent Workflow.
"""
from fastapi import APIRouter, HTTPException
from backend.app.models.schemas import QueryRequest, TruthGuardResponse
from backend.app.agents.workflow import TruthGuardWorkflow

router = APIRouter()
workflow = TruthGuardWorkflow()

@router.post("/", response_model=TruthGuardResponse)
async def execute_query(payload: QueryRequest):
    """
    Submits a query to the TruthGuard multi-agent pipeline.
    Runs Retriever -> Synthesizer -> Critic -> Resolution Engine.
    """
    try:
        response = await workflow.execute(payload.query)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
