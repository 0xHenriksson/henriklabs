import pytest
import os
from pathlib import Path
from config.settings import Settings


def test_settings_defaults():
    """Test that settings have appropriate defaults"""
    settings = Settings()
    
    # Check API settings
    assert settings.API_V1_STR == "/api"
    assert settings.PROJECT_NAME == "Henrik Labs API"
    
    # Check CORS settings
    assert isinstance(settings.BACKEND_CORS_ORIGINS, list)
    
    # Check JWT settings
    assert settings.ALGORITHM == "HS256"
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES == 30
    
    # Check file storage settings
    assert isinstance(settings.UPLOAD_DIR, Path)


def test_settings_from_env(monkeypatch):
    """Test that settings can be overridden from environment variables"""
    # Set environment variables
    monkeypatch.setenv("SECRET_KEY", "test_secret_key")
    monkeypatch.setenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
    monkeypatch.setenv("GOOGLE_CLIENT_ID", "test_client_id")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test_api_key")
    
    # Create settings instance
    settings = Settings()
    
    # Check that values were loaded from environment
    assert settings.SECRET_KEY == "test_secret_key"
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES == 60
    assert settings.GOOGLE_CLIENT_ID == "test_client_id"
    assert settings.ANTHROPIC_API_KEY == "test_api_key"