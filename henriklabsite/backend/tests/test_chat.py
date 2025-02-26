import pytest
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocketDisconnect


def test_get_chat_history(client):
    """Test the chat history endpoint returns a placeholder message for now"""
    response = client.get("/chat")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Chat history endpoint"


def test_send_message(client):
    """Test sending a message returns a placeholder response"""
    test_message = {"content": "Hello, how are you?", "user_id": "test_user"}
    response = client.post("/chat/message", json=test_message)
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "response" in data
    assert data["message"] == "Message received"
    assert data["response"] == "This is a placeholder response from the AI"


def test_websocket_echo(client):
    """Test the websocket endpoint echoes messages back"""
    with client.websocket_connect("/chat/ws") as websocket:
        test_message = "Hello websocket"
        websocket.send_text(test_message)
        response = websocket.receive_text()
        assert response == f"Echo: {test_message}"
        
        # Test another message
        test_message_2 = "Testing websocket communication"
        websocket.send_text(test_message_2)
        response = websocket.receive_text()
        assert response == f"Echo: {test_message_2}"