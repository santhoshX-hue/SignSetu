"""
Ollama Medical Simplification Service (Local Llama 3.2:3b).

Clinical Safety Invariant:
- ONLY simplifies doctor-provided medical explanations.
- Never diagnoses, triages, or generates autonomous clinical advice.
"""

from app.config import settings

class OllamaService:
    """Placeholder service for local Ollama Llama 3.2 interaction."""
    def __init__(self, base_url: str = settings.OLLAMA_BASE_URL, model: str = settings.OLLAMA_MODEL):
        self.base_url = base_url
        self.model = model

    async def check_health(self) -> bool:
        """Check if local Ollama daemon is reachable."""
        # Application logic to be implemented in subsequent stage
        pass

    async def simplify_medical_note(self, text: str) -> str:
        """Simplify doctor explanation into plain language (strictly no diagnosis)."""
        # Application logic to be implemented in subsequent stage
        pass

ollama_service = OllamaService()
