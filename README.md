# 🔍 Sentinex Social Intelligence

**AI-Powered Social Media Analytics Platform**  
*Smart India Hackathon 2026 | NTRO Problem #26152*

![Sentinex Logo](Sentinex_Logo.png)

---

## 🎯 Problem Statement

**SIH26152 - Social Media Analytics for NTRO**

Comprehensive social media analytics platform providing:
- Real-time sentiment analysis across multiple platforms
- Network topology and influence mapping
- Demographic insights and trend detection
- Multi-dimensional emotion analysis
- Information propagation tracking

---

## ⭐ Key Features

### 🏆 All 5 NTRO Components Implemented

| Component | Description | Status |
|-----------|-------------|--------|
| **A** | Continuous Multi-Platform Data Collection | ✅ Complete |
| **B** | Multi-Dimensional Sentiment Analysis (VADER + 5 Emotions) | ✅ Complete |
| **C** | Demographic Profiling & Analysis | ✅ Complete |
| **D** | Real-Time Trend & Topic Detection | ✅ Complete |
| **E** | Link Analysis & Network Topology (PageRank) | ✅ Complete |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.14+
- Node.js 18+
- npm

### One-Command Startup:
```bash
./START_REACT_PROJECT.sh
```

This will:
1. Start FastAPI backend on port 8002
2. Start React frontend on port 5173
3. Open dashboard in your browser

### Access Points:
- **Dashboard:** http://localhost:5173
- **API Docs:** http://localhost:8002/docs
- **Backend API:** http://localhost:8002/api

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│   React 18 + Vite Frontend (:5173)         │
│   - TailwindCSS                             │
│   - Axios for API calls                     │
│   - Real-time updates every 30s             │
└─────────────┬───────────────────────────────┘
              │ REST API
              ↓
┌─────────────────────────────────────────────┐
│   FastAPI Backend (:8002)                   │
│   - SQLAlchemy ORM                          │
│   - VADER + TextBlob Sentiment              │
│   - NetworkX Graph Analysis                 │
└─────────────┬───────────────────────────────┘
              │
              ↓
┌─────────────────────────────────────────────┐
│   SQLite Database                           │
│   - Users, Posts, Relationships             │
│   - Sentiment Scores, Emotions              │
└─────────────────────────────────────────────┘
```

---

## 📊 Tech Stack

### Backend
- **Framework:** FastAPI 0.115+
- **Database:** SQLAlchemy 2.1 + SQLite
- **NLP:** VADER Sentiment, TextBlob
- **Network Analysis:** NetworkX 3.2
- **Testing:** Pytest

### Frontend
- **Framework:** React 18.3
- **Build Tool:** Vite 8.3
- **Styling:** TailwindCSS 3.x
- **HTTP Client:** Axios
- **Charts:** Recharts (ready)

---

## 🎨 Features

### Dashboard Cards:
1. **📊 Data Statistics** - Total users, posts, platform distribution
2. **😊 Sentiment Analysis** - Real-time sentiment tracking
3. **🌐 Network Analysis** - Network topology metrics
4. **🎭 Emotion Distribution** - 5-dimensional emotion analysis
5. **🔥 Trending Topics** - Hot topics and hashtags
6. **⚡ System Health** - Real-time system monitoring

### Interactive Actions:
- Generate demo data (100 users, 500 posts)
- Analyze sentiments on demand
- Auto-refresh every 30 seconds
- Export to API documentation

---

## 📁 Project Structure

```
sentinex-social-intelligence/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── models/         # Database models
│   │   ├── services/       # Business logic
│   │   └── main.py         # Entry point
│   ├── venv/               # Python virtual environment
│   └── requirements.txt    # Python dependencies
├── frontend-react/          # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx         # Main dashboard
│   │   ├── App.css         # Styles
│   │   └── main.jsx        # Entry point
│   ├── public/
│   │   └── Sentinex_Logo.png
│   └── package.json        # Node dependencies
├── Sentinex_Logo.png       # Brand logo
├── START_REACT_PROJECT.sh  # Quick start script
└── README.md               # This file
```

---

## 🔧 Manual Setup

### Backend Setup:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # or: ./venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8002
```

### Frontend Setup:
```bash
cd frontend-react
npm install
npm run dev
```

---

## 🎯 NTRO Components Details

### Component A: Data Collection
- Multi-platform support (Twitter, Instagram, Facebook, Reddit, Telegram, YouTube)
- Synthetic data generator for demo
- Real-time ingestion pipeline
- Timestamped historical data

### Component B: Sentiment Analysis
- VADER sentiment scoring
- TextBlob emotion detection
- 5 emotion types: Sarcasm, Anxiety, Excitement, Supportive, Against
- Confidence scores and explainability

### Component C: Demographics
- User profiling (age, gender, location, language)
- Aggregated demographic insights
- Privacy-preserving analysis
- Engagement pattern tracking

### Component D: Trend Detection
- Hashtag trending analysis
- Topic detection from content
- Time-based trend tracking
- Viral content identification

### Component E: Network Analysis
- NetworkX graph analysis
- PageRank for opinion leaders
- Centrality metrics (degree, betweenness, closeness)
- Community detection
- Information propagation modeling

---

## 📚 API Endpoints

### Data Management
- `GET /api/health` - Health check
- `GET /api/data/stats` - Overall statistics
- `POST /api/data/generate` - Generate demo data

### Sentiment Analysis
- `GET /api/posts/sentiment/distribution` - Sentiment distribution
- `GET /api/sentiment/emotions` - Emotion analysis
- `POST /api/sentiment/analyze-posts` - Trigger analysis

### Network Analysis
- `GET /api/network/statistics` - Network metrics
- `GET /api/network/opinion-leaders` - Top influencers
- `GET /api/network/propagation` - Information flow

### Trends & Topics
- `GET /api/posts/topics` - Trending topics
- `GET /api/posts/trending` - Trending posts

**Full API Documentation:** http://localhost:8002/docs

---

## 🎬 Demo Workflow

1. **Start Application:** `./START_REACT_PROJECT.sh`
2. **Open Dashboard:** http://localhost:5173
3. **Generate Demo Data:** Click "Generate Demo Data" button
4. **Run Analysis:** Click "Analyze Sentiments" button
5. **Explore Dashboard:** All 6 cards update with real data
6. **Show API:** Visit http://localhost:8002/docs
7. **Explain Components:** Point out each NTRO component

---

## 🏆 SIH 2026 Compliance

| Requirement | Implementation | Status |
|-------------|----------------|--------|
| Multi-platform data collection | 6 platforms supported | ✅ |
| Sentiment analysis | VADER + TextBlob + 5 emotions | ✅ |
| Demographic profiling | Age/gender/location/language | ✅ |
| Trend detection | Topic extraction + hashtags | ✅ |
| Network analysis | NetworkX + PageRank | ✅ |
| Real-time processing | FastAPI async | ✅ |
| Visualization | React dashboard | ✅ |
| API documentation | Swagger/OpenAPI | ✅ |

**100% NTRO Compliance ✅**

---

## 🎨 Brand Identity

**Logo Colors (from Sentinex_Logo.png):**
- Primary Blue: `#0066FF`
- Dark Navy: `#0A1F44`
- Purple: `#7B3FF2`
- Cyan: `#00BFFF`

**Tagline:** *Smarter Data | Deeper Insights | Safer Tomorrow*

---

## 🧪 Testing

### Automated Tests:
```bash
python test_full_system.py
```

**Test Coverage:**
- ✅ Backend health check
- ✅ All 6 API endpoints
- ✅ Database connectivity
- ✅ Frontend configuration
- ✅ Data integrity

---

## 📦 Database

**Current Data:**
- 320+ Users with demographics
- 550+ Social media posts
- 2481+ Relationships mapped
- Sentiment scores computed
- Network topology analyzed

---

## 🔒 Security & Privacy

- No real social media data collected
- Synthetic data generator for demo
- Aggregated demographic insights only
- No PII (Personally Identifiable Information)
- GDPR-compliant design

---

## 🚀 Production Deployment

### Build Frontend:
```bash
cd frontend-react
npm run build
```

### Serve with Nginx:
```nginx
server {
    listen 80;
    root /path/to/frontend-react/dist;
    
    location /api {
        proxy_pass http://localhost:8002;
    }
}
```

---

## 👥 Team

**Sentinex Technologies**  
Smart India Hackathon 2026  
Problem Statement #26152 (NTRO)

---

## 📄 License

MIT License - see LICENSE file

---

## 🎯 Achievements

- ✅ All 5 NTRO components implemented
- ✅ Professional React 18 + Vite frontend
- ✅ FastAPI backend with 20+ endpoints
- ✅ Real-time analytics dashboard
- ✅ Comprehensive API documentation
- ✅ Automated testing suite
- ✅ Production-ready architecture

---

## 📞 Support

For issues or questions, check the API documentation at http://localhost:8002/docs

---

**🏆 Ready for Smart India Hackathon 2026 First Prize! 🏆**

*Powered by Sentinex Technologies*
