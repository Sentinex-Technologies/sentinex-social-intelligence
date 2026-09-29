# 🚀 Deployment Guide - Sentinex Social Intelligence

## 📍 Live URLs

| Service | URL | Status |
|---------|-----|--------|
| **Frontend Dashboard** | [https://sentinex-technologies.github.io/sentinex-social-intelligence/](https://sentinex-technologies.github.io/sentinex-social-intelligence/) | ✅ **LIVE** |
| **Backend API** | [https://sentinex-api.onrender.com/](https://sentinex-api.onrender.com/) | ✅ **OPERATIONAL** |
| **API Documentation** | [https://sentinex-api.onrender.com/api/docs](https://sentinex-api.onrender.com/api/docs) | ✅ **AVAILABLE** |

---

## 🎯 Current Status

### ✅ Deployment Complete (Sep 29, 2026)

**Frontend:** GitHub Pages
- React + Vite production build
- Auto-deploys on push to `main`
- Base URL: `/sentinex-social-intelligence/`
- Connected to Render backend API

**Backend:** Render Free Tier
- FastAPI + SQLite
- Python 3.12
- Auto-deploys on push to `main`
- 100 users, 1000 posts, 58K+ engagements

---

## 📊 Database Status

**Current Data:**
- ✅ 100 synthetic users with demographics
- ✅ 1000 social media posts (across 6 platforms)
- ✅ 2127 network relationships
- ✅ 58,895 engagement events
- ✅ Sentiment analysis complete
- ✅ Network topology computed

**Platform Distribution:**
- Twitter: 195 posts
- YouTube: 199 posts
- Instagram: 168 posts
- Telegram: 159 posts
- Facebook: 156 posts
- Reddit: 123 posts

---

## 🔧 How to Generate/Regenerate Data

### Option 1: Using API Docs (GUI)
1. Visit: https://sentinex-api.onrender.com/api/docs
2. Find `POST /api/data/generate`
3. Click "Try it out"
4. Set parameters:
   - `num_users`: 100
   - `num_posts`: 1000
   - `days_back`: 30
   - `seed`: (optional, for reproducibility)
5. Click "Execute"
6. Wait ~45 seconds for completion

### Option 2: Using cURL
```bash
curl -X POST "https://sentinex-api.onrender.com/api/data/generate?num_users=100&num_posts=1000&days_back=30"
```

### Option 3: Using Python
```python
import requests

response = requests.post(
    "https://sentinex-api.onrender.com/api/data/generate",
    params={
        "num_users": 100,
        "num_posts": 1000,
        "days_back": 30
    }
)
print(response.json())
```

---

## 🧹 How to Clear Data

**⚠️ WARNING: This is destructive and cannot be undone!**

### Using API Docs:
1. Visit: https://sentinex-api.onrender.com/api/docs
2. Find `DELETE /api/data/clear`
3. Set `confirm` = `YES_DELETE_ALL`
4. Click "Execute"

### Using cURL:
```bash
curl -X DELETE "https://sentinex-api.onrender.com/api/data/clear?confirm=YES_DELETE_ALL"
```

---

## 🔄 CI/CD Workflows

### GitHub Actions - Frontend Deployment

**Workflow:** `.github/workflows/deploy-frontend.yml`
**Trigger:** Push to `main` branch or manual dispatch
**Steps:**
1. Checkout code
2. Setup Node.js 20
3. Install dependencies (`npm install`)
4. Build frontend (`npm run build`)
5. Upload build artifact
6. Deploy to GitHub Pages

**View Workflow:** [Actions Tab](https://github.com/Sentinex-Technologies/sentinex-social-intelligence/actions)

### Render - Backend Deployment

**Config:** `render.yaml`
**Trigger:** Push to `main` branch
**Steps:**
1. Detect Python 3.12
2. Install dependencies (`pip install -r requirements.txt`)
3. Start Uvicorn server (`uvicorn app.main:app --host 0.0.0.0 --port $PORT`)

**View Logs:** [Render Dashboard](https://dashboard.render.com/)

---

## 🐛 Troubleshooting

### Frontend Shows Empty Screen
**Problem:** Database has no data  
**Solution:** Generate synthetic data (see above)

### API Returns 500 Error
**Problem:** Render backend may be sleeping (free tier)  
**Solution:** Visit backend URL to wake it up, wait 30 seconds

### CORS Error in Browser Console
**Problem:** Frontend origin not allowed  
**Solution:** Backend already configured for GitHub Pages origin

### GitHub Actions Build Fails
**Problem:** CSS syntax errors or Node.js version mismatch  
**Solution:** Check workflow logs, verify Node.js 20+, validate CSS

### Render Build Fails
**Problem:** Python version incompatibility  
**Solution:** Ensure `PYTHON_VERSION=3.12.0` in render.yaml

---

## 📈 Performance Notes

### Render Free Tier Limitations:
- **Spin Down:** After 15 min of inactivity
- **Spin Up:** Takes ~30 seconds on first request
- **RAM:** 512 MB
- **Storage:** Ephemeral (SQLite resets on restart)

### Data Persistence:
- ⚠️ **Database resets** when Render service restarts
- 💡 **Solution:** Re-generate data using the API endpoint
- 🔮 **Future:** Migrate to PostgreSQL persistent storage

---

## 🎓 SIH 2026 Submission Details

**Problem Statement:** #26152 - Social Media Analytics for NTRO  
**Team:** Sentinex Technologies  
**Institution:** Vignan's Nirula Institute of Technology & Science for Women (VNITSW)  
**Department:** CSE - AI & ML  
**Mentor:** Dr. P. Silpa Chaitanya (HoD)

**Team Members:**
- 23NN1A4206 - Bhogireddy Reshma
- 23NN1A4227 - Konda Sai Nija
- 24NN1A4202 - Adduru Likhitha
- 24NN1A4227 - Kalluru Pranathi
- 24NN1A4255 - Konni Lakshmi Neha Sri
- 24NN1A4256 - Kotha Aparna

---

## 📚 Additional Resources

- **Architecture Diagrams:** [COMPLETE_ARCHITECTURE_DIAGRAMS.md](./COMPLETE_ARCHITECTURE_DIAGRAMS.md)
- **Main README:** [README.md](./README.md)
- **API Documentation:** https://sentinex-api.onrender.com/api/docs
- **Organization Profile:** https://github.com/Sentinex-Technologies/.github

---

## ✅ Deployment Checklist

- [x] Frontend deployed to GitHub Pages
- [x] Backend deployed to Render
- [x] CORS configured correctly
- [x] Environment variables set
- [x] Database schema created
- [x] Sample data generated
- [x] All 5 NTRO components operational
- [x] API documentation accessible
- [x] CI/CD workflows configured
- [x] Organization README updated

---

**🎉 Deployment completed successfully on September 29, 2026**

**Last Data Generation:** September 29, 2026 at 11:12 PM IST  
**Next Steps:** Monitor performance, gather feedback, optimize for production
