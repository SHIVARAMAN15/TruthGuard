import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "TruthGuard"
    PROJECT_DESCRIPTION: str = "Adversarial Verification for Multi-Agent Document Q&A"
    API_V1_STR: str = "/api/v1"
    
    # Environment & Host
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # Storage & Corpus
    CORPUS_DIR: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "corpus")
    VECTOR_DB_DIR: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "vector_db")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
