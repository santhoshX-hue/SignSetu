import os

class Settings:
    """Offline-first settings for SignSetu backend."""
    APP_NAME: str = "SignSetu Backend"
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    CORS_ORIGINS: list = [os.getenv("CORS_ORIGINS", "http://localhost:5173")]

settings = Settings()
