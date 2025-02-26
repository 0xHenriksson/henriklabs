import pytest


def test_vector_status_endpoint(client):
    """Test the vector database status endpoint returns the correct placeholder"""
    response = client.get("/vector")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Vector database status",
        "status": "not connected"
    }


def test_vector_search_endpoint(client):
    """Test the vector search endpoint returns an empty results array for now"""
    test_query = {
        "text": "Sample query text",
        "limit": 5
    }
    
    response = client.post("/vector/search", json=test_query)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Vector search endpoint"
    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) == 0  # Empty results for now