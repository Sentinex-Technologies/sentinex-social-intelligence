# Sentinex Social Intelligence - Backend

Backend API for the Sentinex Social Intelligence platform (SIH26152 - Social Media Analytics).

---

## 📊 Current Status

**Phase 1: Backend Foundation** ✅

This is a minimal FastAPI backend skeleton with basic health check functionality. Core analytics features are **not yet implemented**.

**What's Working:**
- ✅ FastAPI application structure
- ✅ Health check endpoint (`/api/health`)
- ✅ API documentation (Swagger UI)
- ✅ CORS configuration
- ✅ Basic test suite

**Not Implemented Yet:**
- ❌ Social media data ingestion
- ❌ Sentiment analysis
- ❌ Trend detection
- ❌ Demographic analysis
- ❌ Network analysis
- ❌ Database integration
- ❌ Authentication
- ❌ ML models

These features will be added in subsequent phases through feature branches.

---

## 🏗️ Architecture

```
Client
  ↓
FastAPI (app/main.py)
  ↓
API Routes (app/api/)
  ↓
Services (app/services/) → Analytics (app/analytics/)
  ↓
Models (app/models/)
```

---

## 📁 Project Structure

```
backend/
├── app/
│   ├── __init__.py          # Application package
│   ├── main.py              # FastAPI application entry point
│   ├── api/                 # API endpoints
│   │   ├── __init__.py
│   │   └── health.py        # Health check endpoint
│   ├── analytics/           # Analytics modules (future)
│   │   └── __init__.py
│   ├── models/              # Data models (future)
│   │   └── __init__.py
│   ├── services/            # Business logic (future)
│   │   └── __init__.py
│   └── utils/               # Utility functions (future)
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_health.py       # Health endpoint tests
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### 1. Create Virtual Environment

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Run the Server

```bash
# Start FastAPI development server with auto-reload
uvicorn app.main:app --reload

# Server will start at http://localhost:8000
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 4. Access API Documentation

Once the server is running:

- **Swagger UI:** http://localhost:8000/api/docs
- **ReDoc:** http://localhost:8000/api/redoc
- **Root endpoint:** http://localhost:8000/

---

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_health.py

# Run with coverage
pytest --cov=app tests/
```

**Expected output:**
```
============================= test session starts ==============================
collected 2 items

tests/test_health.py ..                                                  [100%]

============================== 2 passed in 0.5s ================================
```

---

## 📡 Available Endpoints

### Root Endpoint
```
GET /
```

Returns API information and status.

**Response:**
```json
{
  "message": "Sentinex Social Intelligence API",
  "version": "0.1.0",
  "status": "operational",
  "docs": "/api/docs"
}
```

### Health Check
```
GET /api/health
```

Simple health check to verify service availability.

**Response:**
```json
{
  "status": "ok"
}
```

---

## 🛠️ Development

### Code Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions small and focused

### Adding New Endpoints

1. Create a new router file in `app/api/`
2. Define your endpoints using FastAPI decorators
3. Import and include the router in `app/main.py`

Example:
```python
# app/api/example.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
async def example_endpoint():
    return {"message": "Example"}

# app/main.py
from app.api.example import router as example_router
app.include_router(example_router, prefix="/api", tags=["Example"])
```

### Running Development Server with Custom Port

```bash
uvicorn app.main:app --reload --port 8080
```

---

## 🔧 Configuration

### CORS Settings

CORS is configured in `app/main.py` to allow requests from:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (React dev server)

To modify CORS settings, edit the `CORSMiddleware` configuration in `main.py`.

---

## 🧩 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Framework | FastAPI | High-performance async web framework |
| Server | Uvicorn | ASGI server |
| Testing | pytest | Test framework |
| HTTP Client | httpx | HTTP testing for FastAPI |

---

## 📝 Environment Variables (Future)

When `.env` configuration is added in later phases, it will include:

- `DATABASE_URL` - Database connection string
- `API_HOST` - API host address
- `API_PORT` - API port number
- `LOG_LEVEL` - Logging level

Currently, the application runs with default settings.

---

## 🚦 Next Steps (Future Phases)

1. **Phase 2:** Data models and database setup
2. **Phase 3:** Demo dataset and data ingestion
3. **Phase 4:** Sentiment analysis module
4. **Phase 5:** Trend detection module
5. **Phase 6:** Demographic analysis module
6. **Phase 7:** Network analysis module
7. **Phase 8:** Frontend dashboard integration

---

## 🤝 Contributing

This backend follows the project's Git workflow:

1. Create feature branch from `develop`
2. Implement changes
3. Write tests
4. Run test suite
5. Create Pull Request to `develop`

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

MIT License - See [LICENSE](../LICENSE) for details.

---

## 🏢 Organization

**Sentinex Technologies**  
**Project:** SIH26152 - Social Media Analytics  
**Phase:** 1 - Backend Foundation

---

**Built with Python and FastAPI** 🚀
