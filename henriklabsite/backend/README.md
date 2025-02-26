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

For development, install additional dependencies:

```bash
pip install -r requirements-dev.txt
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

### Testing

Run the test suite:

```bash
pytest
```

Or use the test script with code formatting and linting:

```bash
./scripts/run_tests.sh --format --lint
```

## API Endpoints

- `/api` - API root
- `/api/chat` - Chat endpoints
- `/api/auth` - Authentication endpoints
- `/api/files` - File management
- `/api/vector` - Vector search capabilities

## Project Structure

```
henriklabsite/
  ├── henriklabs/          # Current Astro frontend
  └── backend/             # New Python backend
      ├── app/             # Main application code
      │   ├── api/         # API endpoints
      │   ├── auth/        # Authentication handlers
      │   ├── chat/        # Chat functionality
      │   ├── storage/     # File storage logic
      │   ├── vector/      # Vector database integration
      │   └── models/      # Data models
      ├── config/          # Configuration files
      ├── tests/           # Test suite
      └── scripts/         # Utility scripts
```

## Implementation Plan

1. **FastAPI Framework**
   - RESTful API with async support
   - OpenAPI documentation
   - WebSocket support for real-time chat

2. **Authentication**
   - Google OAuth integration using `authlib`
   - JWT token management with `python-jose`
   - User session handling

3. **Database**
   - PostgreSQL for relational data (users, chat histories)
   - SQLAlchemy ORM for database interactions
   - Alembic for migrations

4. **File Storage**
   - CSV validation and processing with pandas
   - Local storage with path to S3-compatible storage
   - Access control tied to user authentication

5. **Vector Database**
   - Qdrant (self-hosted) for vector storage
   - Embedding generation with sentence-transformers
   - API for similarity search

6. **LLM Integration**
   - Anthropic Claude API integration
   - Abstraction layer for easy model switching
   - Context management for chat history

7. **Deployment**
   - Docker containerization
   - Docker Compose for development
   - Kubernetes manifests for production

8. **API Endpoints**
   - `/auth/*` - Authentication routes
   - `/chat/*` - Chat management
   - `/files/*` - File upload and management
   - `/vector/*` - Vector search capabilities