"""
Doctor Module Router (SignSetu).
Handles doctor note submission, simplification requests, and final doctor approval.
"""

from fastapi import APIRouter
from app.models.schemas import SimplificationRequest, SimplificationDraftResponse, DoctorApprovalRequest

router = APIRouter(prefix="/api/doctor", tags=["Doctor Dashboard"])

@router.post("/simplify", response_model=SimplificationDraftResponse)
async def request_simplification(payload: SimplificationRequest):
    """Generates simplified draft for doctor review. Logic to be implemented."""
    pass

@router.post("/approve-and-send")
async def approve_and_send(payload: DoctorApprovalRequest):
    """Doctor explicitly reviews, approves, and dispatches message to patient. Logic to be implemented."""
    pass
