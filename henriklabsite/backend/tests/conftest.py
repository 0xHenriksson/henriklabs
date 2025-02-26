import pytest
from fastapi.testclient import TestClient
from app.main import app
import os
import tempfile
from pathlib import Path


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def temp_upload_dir():
    """Create a temporary directory for file uploads during tests"""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_upload_dir = os.environ.get("UPLOAD_DIR")
        os.environ["UPLOAD_DIR"] = temp_dir
        yield Path(temp_dir)
        if original_upload_dir:
            os.environ["UPLOAD_DIR"] = original_upload_dir
        else:
            del os.environ["UPLOAD_DIR"]


@pytest.fixture
def csv_file():
    """Create a sample CSV file for testing"""
    content = "name,age,city\nJohn,30,New York\nJane,25,Los Angeles\n"
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as temp_file:
        temp_file.write(content.encode("utf-8"))
        temp_file_path = temp_file.name
    
    yield temp_file_path
    
    # Clean up the temporary file
    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)