# 🚀 DEPLOYMENT GUIDE - GitHub Pages + Render

**Project:** Sentinex Social Intelligence  
**Frontend:** GitHub Pages (Static)  
**Backend:** Render (Python/FastAPI)  
**Date:** September 29, 2026

---

## 📋 TABLE OF CONTENTS

1. [Architecture Overview](#architecture-overview)
2. [Prerequisites](#prerequisites)
3. [Backend Deployment (Render)](#backend-deployment-render)
4. [Frontend Deployment (GitHub Pages)](#frontend-deployment-github-pages)
5. [Verification & Testing](#verification--testing)
6. [Troubleshooting](#troubleshooting)
7. [Production URLs](#production-urls)

---

## 🏗️ ARCHITECTURE OVERVIEW

```
┌──────────────────────────────────────────┐
│   GitHub Pages (Frontend)                │
│   https://sentinex-technologies          │
│   .github.io/sentinex-social-intelligence│
│                                           │
│   - React 18 + Vite                      │
│   - Static HTML/CSS/JS                   │
│   - Auto-deploy on push to main          │
└────────────────┬─────────────────────────┘
                 │
                 │ HTTPS API Calls
                 ↓
┌──────────────────────────────────────────┐
│   Render (Backend)                       │
│   https://sentinex-api.onrender.com      │
│                                           │
│   - FastAPI (Python 3.14)                │
│   - SQLite Database                      │
│   - CORS enabled for GitHub Pages        │
│   - Auto-deploy from GitHub              │
└──────────────────────────────────────────┘
```

---

## ✅ PREREQUISITES

### 1. Accounts Required:
- ✅ GitHub account (you have this)
- ✅ Render account (free tier) - https://render.com

### 2. Repository Access:
- ✅ Admin access to `Sentinex-Technologies/sentinex-social-intelligence`

### 3. Tools Installed:
- ✅ Git
- ✅ Node.js 18+
- ✅ npm

---

## 🔧 BACKEND DEPLOYMENT (RENDER)

### Step 1: Login to Render

1. Go to https://dashboard.render.com
2. Login with GitHub (if not already)
3. You should see your dashboard

### Step 2: Create New Web Service

1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Build and deploy from a Git repository"**
4. Click **"Next"**

### Step 3: Connect Repository

1. If you haven't connected GitHub yet:
   - Click **"Connect GitHub"**
   - Authorize Render to access your repositories
   - Grant access to Sentinex-Technologies organization

2. Find and select: **`sentinex-social-intelligence`**
3. Click **"Connect"**

### Step 4: Configure Service

Fill in the following details:

**Basic Settings:**
- **Name:** `sentinex-api` (or any name you prefer)
- **Region:** Singapore (closest to India)
- **Branch:** `main`
- **Root Directory:** `backend`

**Build & Deploy:**
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

**Plan:**
- Select **"Free"** (perfect for demo)

**Advanced Settings (Click "Advanced"):**

Add these Environment Variables:
- **Key:** `PYTHON_VERSION` | **Value:** `3.14.0`
- **Key:** `DATABASE_URL` | **Value:** `sqlite:///./sentinex.db`
- **Key:** `ENVIRONMENT` | **Value:** `production`

**Health Check:**
- **Path:** `/api/health`

### Step 5: Deploy

1. Scroll down and click **"Create Web Service"**
2. ⏳ Wait 3-5 minutes for deployment
3. Watch the build logs for any errors
4. ✅ When you see "Your service is live 🎉", it's ready!

### Step 6: Get Your Backend URL

1. On the service page, you'll see your URL:
   - Example: `https://sentinex-api.onrender.com`
2. **Copy this URL** - you'll need it for the frontend!
3. Test it by visiting: `https://your-url.onrender.com/api/docs`
4. You should see the FastAPI Swagger documentation

---

## 🎨 FRONTEND DEPLOYMENT (GITHUB PAGES)

### Step 1: Update Frontend Environment

1. Open file: `frontend-react/.env.production`
2. Replace the URL with YOUR Render backend URL:

```env
VITE_API_BASE_URL=https://YOUR-RENDER-URL.onrender.com
```

**Example:**
```env
VITE_API_BASE_URL=https://sentinex-api.onrender.com
```

3. Save the file

### Step 2: Commit and Push Changes

```bash
# Check status
git status

# Add all changes
git add .

# Commit
git commit -m "feat: Add deployment configuration for GitHub Pages and Render

✅ Vite config updated for GitHub Pages
✅ GitHub Actions workflow added
✅ Render configuration added
✅ CORS updated for production
✅ API base URL configured

Deployment ready!"

# Push to main branch
git push origin feature/deployment-github-pages-render
```

### Step 3: Merge to Main

1. Go to GitHub repository
2. Create Pull Request from `feature/deployment-github-pages-render` to `main`
3. Review changes
4. Click **"Merge Pull Request"**
5. Click **"Confirm Merge"**

### Step 4: Enable GitHub Pages

1. Go to repository **Settings**
2. Scroll down to **"Pages"** section (left sidebar)
3. Under **"Build and deployment"**:
   - **Source:** Select **"GitHub Actions"**
4. Click **"Save"**

### Step 5: Trigger Deployment

GitHub Actions will automatically deploy when you push to main. To manually trigger:

1. Go to **"Actions"** tab in GitHub
2. Select **"Deploy Frontend to GitHub Pages"** workflow
3. Click **"Run workflow"** button
4. Select branch: `main`
5. Click **"Run workflow"**

### Step 6: Wait for Deployment

1. Watch the workflow run (takes 2-3 minutes)
2. ✅ When completed, you'll see a green checkmark
3. Your frontend URL will be:
   ```
   https://sentinex-technologies.github.io/sentinex-social-intelligence/
   ```

---

## ✅ VERIFICATION & TESTING

### 1. Test Backend (Render)

```bash
# Test health endpoint
curl https://your-backend-url.onrender.com/api/health

# Expected response:
{
  "status": "healthy",
  "database": "connected",
  "timestamp": "2026-09-29T..."
}
```

### 2. Test API Documentation

Visit: `https://your-backend-url.onrender.com/api/docs`

You should see:
- ✅ FastAPI Swagger UI
- ✅ All API endpoints listed
- ✅ Can test endpoints interactively

### 3. Test Frontend

Visit: `https://sentinex-technologies.github.io/sentinex-social-intelligence/`

You should see:
- ✅ Sentinex dashboard loads
- ✅ Logo and styling appear correctly
- ✅ Components load (may show empty data initially)

### 4. Generate Demo Data

1. On the frontend dashboard
2. Click **"Generate Demo Data"** button
3. ⏳ Wait 30-60 seconds (Render free tier cold start)
4. ✅ Data should populate all cards

### 5. End-to-End Test

Complete workflow test:

1. ✅ Generate demo data
2. ✅ Click "Analyze Sentiments"
3. ✅ All 6 cards show data
4. ✅ Charts render correctly
5. ✅ Refresh button works

---

## 🐛 TROUBLESHOOTING

### Issue 1: Backend is Slow (First Request)

**Symptom:** First API call takes 30-60 seconds

**Cause:** Render free tier "sleeps" after 15 minutes of inactivity

**Solution:**
- ✅ This is normal for free tier
- Wait for backend to "wake up"
- Subsequent requests will be fast (<200ms)

**For Judges:** Mention that this is free tier behavior, production would use paid tier

---

### Issue 2: CORS Error

**Symptom:** Browser console shows CORS error

**Cause:** Backend not allowing frontend origin

**Solution:**
```bash
# Check backend CORS settings in backend/app/main.py
# Should include:
allow_origins=[
    "https://sentinex-technologies.github.io",
    ...
]
```

---

### Issue 3: 404 on GitHub Pages

**Symptom:** Page shows 404 error

**Cause:** GitHub Pages not properly configured

**Solution:**
1. Go to repo Settings → Pages
2. Ensure Source is set to "GitHub Actions"
3. Re-run the workflow from Actions tab

---

### Issue 4: API Calls Failing

**Symptom:** Network errors in browser console

**Cause:** Wrong API base URL in frontend

**Solution:**
1. Check `.env.production` has correct Render URL
2. Rebuild and redeploy frontend
3. Clear browser cache

---

### Issue 5: Build Failed on Render

**Symptom:** Render shows "Build failed"

**Cause:** Missing dependencies or Python version issue

**Solution:**
1. Check build logs in Render dashboard
2. Ensure `requirements.txt` is correct
3. Verify Python version is set to 3.14.0
4. Manually trigger redeploy

---

## 🌐 PRODUCTION URLS

After successful deployment:

### Frontend (GitHub Pages):
```
https://sentinex-technologies.github.io/sentinex-social-intelligence/
```

**Use this URL for:**
- ✅ SIH submission
- ✅ Demo to judges
- ✅ Sharing with evaluators

### Backend (Render):
```
https://YOUR-SERVICE-NAME.onrender.com
```

**API Documentation:**
```
https://YOUR-SERVICE-NAME.onrender.com/api/docs
```

**Health Check:**
```
https://YOUR-SERVICE-NAME.onrender.com/api/health
```

---

## 📊 DEPLOYMENT CHECKLIST

### Before Deployment:
- [x] Render account created
- [x] Repository has deployment configuration
- [x] Backend CORS updated
- [x] Frontend environment configured

### Backend Deployment:
- [ ] Render web service created
- [ ] Backend URL copied
- [ ] Health check passing
- [ ] API docs accessible

### Frontend Deployment:
- [ ] `.env.production` updated with Render URL
- [ ] Changes committed and pushed
- [ ] Merged to main branch
- [ ] GitHub Pages enabled
- [ ] Workflow completed successfully

### Verification:
- [ ] Frontend loads without errors
- [ ] API calls succeed
- [ ] Demo data generates
- [ ] All 6 cards display data
- [ ] Charts render correctly

---

## 🎯 SIH SUBMISSION URLS

**For your SIH submission form, use:**

**Live Demo URL:**
```
https://sentinex-technologies.github.io/sentinex-social-intelligence/
```

**API Documentation:**
```
https://YOUR-RENDER-URL.onrender.com/api/docs
```

**GitHub Repository:**
```
https://github.com/Sentinex-Technologies/sentinex-social-intelligence
```

---

## 💡 TIPS FOR DEMO

### For Judges:
1. **Mention free tier:** "Backend runs on Render free tier, so first request takes 30-60 seconds to wake up. In production, we'd use paid tier for instant responses."

2. **Highlight features:**
   - "Dashboard auto-deployed via GitHub Actions"
   - "Backend API documented with Swagger"
   - "CORS properly configured for security"
   - "Production-ready architecture"

3. **Show scalability:**
   - "Easy to upgrade to paid tier ($7/month)"
   - "Can add PostgreSQL database"
   - "Can add Redis for caching"
   - "Horizontal scaling supported"

### Performance Expectations:
- **First request:** 30-60 seconds (cold start)
- **Subsequent requests:** <200ms
- **Data generation:** 5-10 seconds
- **Sentiment analysis:** 3-5 seconds

---

## 🔄 CONTINUOUS DEPLOYMENT

### Auto-Deploy is Enabled!

**Frontend:**
- ✅ Push to `main` branch → Auto-deploys via GitHub Actions
- ✅ Takes 2-3 minutes

**Backend:**
- ✅ Push to `main` branch → Auto-deploys via Render
- ✅ Takes 3-5 minutes

**To update:**
```bash
git add .
git commit -m "Update message"
git push origin main
# Wait for auto-deployment!
```

---

## 📞 SUPPORT

### If You Face Issues:

**Render Support:**
- Dashboard: https://dashboard.render.com
- Docs: https://render.com/docs
- Status: https://status.render.com

**GitHub Pages:**
- Settings: Repository → Settings → Pages
- Actions: Repository → Actions tab
- Docs: https://docs.github.com/pages

---

## 🎉 SUCCESS!

If you've followed all steps and verifications pass:

✅ **Frontend deployed to GitHub Pages**  
✅ **Backend deployed to Render**  
✅ **APIs working correctly**  
✅ **Demo data generates successfully**  
✅ **All 6 components operational**

**🏆 Your project is now LIVE and ready for SIH 2026 submission! 🚀**

---

*Deployment Guide Version 1.0*  
*Last Updated: September 29, 2026*  
*Team: Sentinex Technologies - VNITSW*
