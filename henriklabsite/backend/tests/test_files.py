import pytest
import os
import json
from fastapi import status


def test_list_files_endpoint(client):
    """Test the file listing endpoint returns a placeholder message for now"""
    response = client.get("/files")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "File listing endpoint"


def test_upload_csv_file(client, csv_file):
    """Test uploading a valid CSV file"""
    with open(csv_file, "rb") as f:
        filename = os.path.basename(csv_file)
        response = client.post(
            "/files/upload",
            files={"file": (filename, f, "text/csv")}
        )
    
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "File uploaded successfully"
    assert data["filename"] == filename
    assert data["rows"] == 2  # Our test CSV has 2 data rows
    assert data["columns"] == ["name", "age", "city"]


def test_reject_non_csv_file(client, tmp_path):
    """Test that non-CSV files are rejected"""
    # Create a temporary text file
    text_file = tmp_path / "test.txt"
    text_file.write_text("This is not a CSV file")
    
    with open(text_file, "rb") as f:
        response = client.post(
            "/files/upload",
            files={"file": ("test.txt", f, "text/plain")}
        )
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Only CSV files are allowed" in response.json()["detail"]


def test_reject_invalid_csv(client, tmp_path):
    """Test that invalid CSV files are rejected"""
    # Create a malformed CSV file
    invalid_csv = tmp_path / "invalid.csv"
    invalid_csv.write_text("name,age,city\nJohn,thirty,New York\nincomplete_row\n")
    
    with open(invalid_csv, "rb") as f:
        response = client.post(
            "/files/upload",
            files={"file": ("invalid.csv", f, "text/csv")}
        )
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Invalid CSV file" in response.json()["detail"]