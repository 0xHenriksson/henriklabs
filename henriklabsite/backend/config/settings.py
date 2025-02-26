import os
from pathlib import Path
from pydantic_settings import BaseSettings
from typing import List, Dict, Any, Optional

class Settings(BaseSettings):
    """Application settings"""
    # API settings
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Henrik Labs API"
    
    # CORS settings
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "devsecretkey")  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Google OAuth settings
    GOOGLE_CLIENT_ID: Optional[str] = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: Optional[str] = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_REDIRECT_URI: Optional[str] = os.getenv("GOOGLE_REDIRECT_URI")
    
    # Claude API settings
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    
    # File storage settings
    UPLOAD_DIR: Path = Path("/tmp/henriklabs/uploads")  # Change in production
    
    # Vector database settings
    VECTOR_DB_URL: Optional[str] = os.getenv("VECTOR_DB_URL")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

# Create upload directory if it doesn't exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)