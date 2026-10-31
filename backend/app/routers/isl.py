"""
Text-to-ISL Module Router (Reserved for Teammate).
Maps doctor-approved simplified text to ISL gloss tokens / animation cues.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/isl", tags=["Text-to-ISL"])

# Teammate to implement text-to-ISL animation endpoints here
