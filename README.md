# Sentinex Social Intelligence

AI-powered social media analytics platform for sentiment analysis, trend detection, demographic insights, and network intelligence.

---

## 🎯 Problem Statement

This project addresses **SIH26152 - Social Media Analytics**, providing comprehensive tools for analyzing social media data to understand public sentiment, emerging narratives, and community dynamics across multiple platforms.

---

## 🚀 Objective

Sentinex Social Intelligence aims to analyze social media data from platforms like X (Twitter), Instagram, LinkedIn, Telegram, and Facebook to provide:

- **Sentiment & Emotion Analysis** - Understanding public mood and emotional trends through advanced NLP
- **Trending Topics & Narratives** - Identifying emerging themes, viral discussions, and narrative patterns
- **Aggregate Demographic Insights** - Privacy-preserving demographic patterns and engagement analysis
- **Network & Link Analysis** - Mapping connections, information flow, and community structures
- **Influence & Community Detection** - Identifying key influencers, opinion leaders, and community clusters
- **Temporal Analysis** - Tracking trends, sentiment, and engagement patterns over time
- **Explainable AI Insights** - Transparent, interpretable analytics with confidence scores

---

## 📊 Current Status

> 📄 **For detailed real-time project status, see [PROJECT_STATUS.md](PROJECT_STATUS.md)**

**🚀 Phase 2 Complete - 60% Overall Progress**

| Metric | Status |
|--------|--------|
| **Overall Completion** | **60%** (3/5 phases complete) |
| **NTRO Components** | **3/5 Complete** (A, C, E) |
| **Tests Passing** | **12/12 ✅** (100% success rate) |
| **API Endpoints** | **16 endpoints** |
| **Branch** | `feature/data-and-network-foundation` |

**✅ Completed:**
- ✅ Phase 0: Repository structure & documentation
- ✅ Phase 1: FastAPI backend foundation
- ✅ Phase 2: Data collection & network analysis
  - Database schema (SQLAlchemy + SQLite)
  - Synthetic data generator (100% legal, no web scraping)
  - Network analysis engine (5 centrality measures, PageRank)
  - 15 API endpoints for data, network, and posts
  - Component A: Multi-platform data collection ✅
  - Component C: Demographic profiling ✅
  - Component E: Link analysis & network topology ✅

**🔄 In Development:**
- ⏳ Phase 3: Sentiment analysis & trend detection
  - Component B: Multi-dimensional sentiment (emotions, sarcasm)
  - Component D: Real-time trend & topic detection
- ⏳ Phase 4: Frontend dashboard
- ⏳ Phase 5: Production readiness

**📊 Track Progress:** See [PROJECT_STATUS.md](PROJECT_STATUS.md) for detailed tracking of all changes, features, and updates.

---

## 🏗️ Planned Architecture

```
Data Sources (X/Twitter, Instagram, LinkedIn, Telegram, Facebook)
                            ↓
                  Data Ingestion Layer
                            ↓
                  Data Processing Pipeline
                            ↓
                    Analytics Engine
        ┌──────────────┬────────────┬──────────────┐
        ↓              ↓            ↓              ↓
   Sentiment      Trend         Demographics   Network
   Analysis     Detection        Analysis      Analysis
        └──────────────┴────────────┴──────────────┘
                            ↓
                      REST API Layer
                            ↓
                  Visualization Dashboard
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed architecture documentation.

---

## 🧩 Planned Modules

### 1. **Data Ingestion**
- Multi-platform social media data collection (X, Instagram, LinkedIn, etc.)
- Rate limiting and API management
- Timestamped historical data storage
- Data validation and normalization

### 2. **Sentiment & Emotion Analysis**
- Multi-class sentiment classification (positive/negative/neutral)
- Emotion detection (joy, anger, sadness, fear, surprise, disgust)
- Confidence scoring and explainability
- Real-time and batch processing

### 3. **Trend Detection**
- Trending topics identification using TF-IDF and frequency analysis
- Emerging narrative tracking
- Hashtag and keyword trend analysis
- Topic clustering and categorization

### 4. **Demographic Analysis**
- Aggregate age/location insights (fully anonymized)
- Privacy-preserving demographic patterns
- Engagement patterns by demographic groups
- **No individual profiling or tracking**

### 5. **Network Analysis**
- Community detection using graph algorithms
- Influence scoring and ranking
- Information propagation tracking
- Connection and interaction mapping

### 6. **Visualization Dashboard**
- Interactive charts and graphs
- Real-time analytics display
- Multi-dimensional filtering
- Exportable reports and insights

---

## 🔄 Development Workflow

This project follows a structured Git workflow for team collaboration:

```
main (stable, presentation-ready)
  ↑
develop (integration branch)
  ↑
feature/* (individual features)
```

**Workflow Steps:**
1. Create feature branch from `develop`
2. Implement focused feature with tests
3. Commit with meaningful messages
4. Open Pull Request to `develop`
5. Code review and approval
6. Merge to `develop`
7. Periodic merges from `develop` → `main` after testing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/DEVELOPMENT_WORKFLOW.md](docs/DEVELOPMENT_WORKFLOW.md) for detailed guidelines.

---

## 👥 Team Development

This repository is structured for a **6-member development team** working collaboratively through feature branches. Each team member can work on independent features that are integrated through the `develop` branch.

**Suggested Team Roles:**
- **Developer 1:** Data Ingestion & API Integration
- **Developer 2:** Sentiment & Emotion Analysis
- **Developer 3:** Trend Detection & Topic Analysis
- **Developer 4:** Demographic Analysis (Aggregate)
- **Developer 5:** Network & Influence Analysis
- **Developer 6:** Dashboard & Visualization

**Feature Branch Strategy:**
- `feature/data-ingestion`
- `feature/sentiment-analysis`
- `feature/trend-detection`
- `feature/demographic-analysis`
- `feature/network-analysis`
- `feature/dashboard`

---

## 🔐 Responsible AI & Privacy

Sentinex Social Intelligence is committed to ethical AI and privacy-first design:

### Privacy Principles

✅ **Aggregate Analysis Only** - No unnecessary individual profiling  
✅ **Anonymized Insights** - Demographic data is aggregated and anonymous  
✅ **Synthetic Data for Development** - Using mock/demo data during prototype phase  
✅ **Responsible Data Handling** - Compliance with platform terms of service  
✅ **Transparent AI** - Explainable insights with confidence scores  
✅ **Privacy-First Design** - Minimal data retention, secure storage  
✅ **No Personal Tracking** - User behavior is not individually tracked  

### Data Collection Ethics

- Social media data collection follows platform terms of service
- Only publicly available data is analyzed
- Personal identifiers are anonymized
- Data is used for research and educational purposes only

---

## ⚠️ Disclaimer

### Prototype Status

- **This is a prototype/demonstration system** built for SIH26152 competition
- Mock and synthetic data are used during development and testing
- Features are in various stages of development
- Not all planned capabilities are currently implemented
- Real-world deployment requires proper API access, authentication, and compliance

### Data Sources

- **Demo data:** Synthetic/anonymized data for testing and demonstration
- **Production system:** Will use legitimately obtained platform data via official APIs
- **Privacy:** No personal data is stored beyond what's necessary for aggregate analysis
- **Compliance:** All data collection respects platform terms of service and privacy regulations

### Academic & Research Use

This project is developed for educational purposes as part of Smart India Hackathon 2026. Any insights or analytics are for demonstration and research purposes only.

---

## 🛠️ Technology Stack

### Backend
- **Python 3.9+** - Core programming language
- **FastAPI** - High-performance REST API framework
- **SQLite** - Initial prototype database (PostgreSQL for production)
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations

### NLP & Analytics
- **spaCy** - Advanced NLP processing
- **TextBlob** - Sentiment analysis
- **VADER** - Social media-specific sentiment analysis
- **scikit-learn** - Machine learning algorithms
- **NetworkX** - Network and graph analysis

### Frontend
- **React 18+** - Modern UI framework
- **Vite** - Fast build tool and dev server
- **Recharts / D3.js** - Data visualization
- **TailwindCSS** - Utility-first CSS framework

### Development Tools
- **Git** - Version control
- **pytest** - Python testing
- **Jest** - JavaScript testing
- **ESLint / Prettier** - Code formatting

---

## 📁 Repository Structure

```
sentinex-social-intelligence/
├── .gitignore                   # Git ignore rules
├── .env.example                 # Environment variables template
├── LICENSE                      # MIT License
├── README.md                    # This file
├── CONTRIBUTING.md              # Contribution guidelines
├── Reference_Doc.pdf            # Scraper implementations reference
├── Sentinex_Logo.png           # Project branding
│
├── backend/                     # Python backend (FastAPI)
│   └── (to be implemented)
│
├── frontend/                    # React frontend (Vite)
│   └── (to be implemented)
│
├── docs/                        # Documentation
│   ├── ARCHITECTURE.md          # System architecture
│   └── DEVELOPMENT_WORKFLOW.md  # Git workflow guide
│
├── experiments/                 # Research & prototyping
│   └── (notebooks, prototypes)
│
└── tests/                       # Test suites
    └── (unit & integration tests)
```

---

## 🚦 Getting Started

### Prerequisites

- Python 3.9 or higher
- Node.js 16+ and npm
- Git

### Installation (Coming Soon)

```bash
# Clone repository
git clone <repository-url>
cd sentinex-social-intelligence

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Environment configuration
cp .env.example .env
# Edit .env with your configuration

# Run backend
cd backend
python app.py

# Run frontend (in another terminal)
cd frontend
npm run dev
```

**Note:** Full setup instructions will be provided as implementation progresses.

---

## 📚 Documentation

### Project Management
- **[PROJECT_STATUS.md](PROJECT_STATUS.md)** - 📊 **Living project tracker** (updated with every change)
- **[PHASE2_STATUS.md](PHASE2_STATUS.md)** - Phase 2 completion report

### Development Guides
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to this project
- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Detailed system architecture
- **[docs/DEVELOPMENT_WORKFLOW.md](docs/DEVELOPMENT_WORKFLOW.md)** - Git workflow and branching strategy

### Technical Documentation
- **[docs/PHASE2_SUMMARY.md](docs/PHASE2_SUMMARY.md)** - Phase 2 technical details (data & network analysis)
- **[backend/README.md](backend/README.md)** - Backend setup and API documentation
- **[Reference_Doc.pdf](Reference_Doc.pdf)** - Social media scraper implementations (reference only)

---

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest tests/

# Frontend tests
cd frontend
npm test

# Integration tests
npm run test:integration
```

---

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Development workflow
- Coding standards
- Commit message conventions
- Pull request process
- Testing guidelines

**Quick Start:**
```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
# Make changes, commit, push
# Open Pull Request to develop
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🏢 Organization

**Sentinex Technologies**  
Building intelligent social media analytics for better insights.

**Project:** Smart India Hackathon 2026  
**Problem Statement:** SIH26152 - Social Media Analytics

---

## 🔗 Links

- **Documentation:** [docs/](docs/)
- **Issues:** GitHub Issues (when repository is public)
- **Project Board:** (Coming soon)

---

## 📞 Contact

For questions, issues, or collaboration:
- Open a GitHub issue
- Check documentation in `docs/` folder
- Contact team lead through project channels

---

## 🙏 Acknowledgments

- Smart India Hackathon 2026 organizers
- Open-source NLP and data science communities
- All contributors and team members

---

**Built with ❤️ by Sentinex Technologies for SIH 2026**

---

*Last Updated: September 26, 2026*
