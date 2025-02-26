# Henrik Labs Backend API

Backend API for Henrik Labs website with AI chat capabilities, authentication, file storage, and vector database integration.

## Features

- FastAPI-based REST API with WebSocket support
- Google OAuth authentication
- File upload and management (CSV files)
- Integration with Claude 3.7 (with path to custom model)
- Vector database for embeddings storage
- Containerized with Docker and Docker Compose

## Development Setup

### Prerequisites

- Python 3.11+
- Docker and Docker Compose

### Installation

1. Clone the repository
2. Navigate to the backend directory

```bash
cd henriklabsite/backend
```

3. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create `.env` file from example

```bash
cp .env.example .env
```

6. Update the `.env` file with your configuration

### Running with Docker

```bash
docker-compose up -d
```

Access the API documentation at: http://localhost:8000/docs

### Running Locally

```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `/api` - API root
- `/api/chat` - Chat endpoints
- `/api/auth` - Authentication endpoints
- `/api/files` - File management
- `/api/vector` - Vector search capabilities

## Architecture

- `app/` - Main application code
  - `api/` - API endpoints
  - `auth/` - Authentication handlers
  - `chat/` - Chat functionality
  - `storage/` - File storage logic
  - `vector/` - Vector database integration
  - `models/` - Data models
- `config/` - Configuration files
- `tests/` - Test suite
- `scripts/` - Utility scripts