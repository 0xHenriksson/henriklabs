from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any

# Create the API router
api_router = APIRouter(prefix="/api")

@api_router.get("/")
async def api_root():
    return {
        "message": "Henrik Labs API",
        "endpoints": [
            {"path": "/auth", "description": "Authentication endpoints"},
            {"path": "/chat", "description": "Chat functionality"},
            {"path": "/files", "description": "File upload and management"},
            {"path": "/vector", "description": "Vector search capabilities"}
        ]
    }