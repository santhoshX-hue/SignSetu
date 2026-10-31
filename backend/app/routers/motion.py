"""
Motion-to-Text Module Router (Reserved for Teammate).
Receives gesture streams / frames and produces recognized text tokens.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/motion", tags=["Motion-to-Text"])

# Teammate to implement motion recognition endpoints here
