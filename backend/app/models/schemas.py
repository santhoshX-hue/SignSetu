from typing import List, Optional
from pydantic import BaseModel, Field

# ============================================================================
# SHARED INTEGRATION FILE: Do not overwrite arbitrarily without team sync.
# ============================================================================

# --- Doctor & Ollama Simplification Schemas (Doctor Responsibility) ---
class SimplificationRequest(BaseModel):
    """Doctor's input notes to be simplified into plain language."""
    doctor_notes: str = Field(..., description="Original doctor explanation")
    simplification_level: str = Field(default="plain_language", description="Target complexity level")

class SimplificationDraftResponse(BaseModel):
    """AI simplified draft awaiting doctor verification."""
    original_text: str
    simplified_draft: str
    status: str = "pending_doctor_approval"

class DoctorApprovalRequest(BaseModel):
    """Doctor-approved final text payload before dispatching to patient/ISL."""
    session_id: str
    approved_text: str
    doctor_id: Optional[str] = "dr_default"
    approved: bool = True

# --- Reserved: Patient Module Schemas (Teammate Responsibility) ---
class PatientMessageResponse(BaseModel):
    session_id: str
    message: str
    timestamp: Optional[str] = None

# --- Reserved: Motion-to-Text Schemas (Teammate Responsibility) ---
class MotionRecognitionPayload(BaseModel):
    session_id: str
    detected_tokens: List[str] = []
    confidence: float = 0.0
    constructed_phrase: Optional[str] = None

# --- Reserved: Text-to-ISL Schemas (Teammate Responsibility) ---
class ISLGlossPayload(BaseModel):
    input_text: str
    isl_gloss_sequence: List[str] = []
    animation_cues: List[str] = []
