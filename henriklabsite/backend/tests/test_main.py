def test_root_endpoint(client):
    """Test the root endpoint returns the correct message"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Henrik Labs API"}


def test_health_check(client):
    """Test the health check endpoint returns a healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_api_root(client):
    """Test the API root endpoint returns the correct endpoints"""
    response = client.get("/api")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Henrik Labs API"
    assert "endpoints" in data
    
    # Check that all required endpoints are listed
    endpoints = [endpoint["path"] for endpoint in data["endpoints"]]
    required_endpoints = ["/auth", "/chat", "/files", "/vector"]
    for endpoint in required_endpoints:
        assert endpoint in endpoints