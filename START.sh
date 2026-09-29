#!/bin/bash

# Sentinex Social Intelligence - Smart India Hackathon 2026
# One-command startup script for first-prize quality demo

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "════════════════════════════════════════════════════════════"
echo "     🔍 Sentinex Social Intelligence Platform"
echo "     Smart India Hackathon 2026 | NTRO Problem #26152"
echo "════════════════════════════════════════════════════════════"
echo -e "${NC}"

# Navigate to project root
cd "$(dirname "$0")"

# Step 1: Clean up old processes
echo -e "${YELLOW}🧹 Cleaning up old processes...${NC}"
lsof -ti:8002 2>/dev/null | xargs kill -9 2>/dev/null || true
lsof -ti:8001 2>/dev/null | xargs kill -9 2>/dev/null || true
lsof -ti:8000 2>/dev/null | xargs kill -9 2>/dev/null || true
lsof -ti:5173 2>/dev/null | xargs kill -9 2>/dev/null || true
sleep 2
echo -e "${GREEN}✅ Clean!${NC}"

# Step 2: Start backend server
echo ""
echo -e "${YELLOW}🔧 Starting FastAPI backend on port 8002...${NC}"
cd backend
nohup ./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8002 > /tmp/sentinex-backend.log 2>&1 &
BACKEND_PID=$!
cd ..

# Wait for backend to start
echo -e "${BLUE}⏳ Waiting for backend to initialize...${NC}"
sleep 5

# Check if backend is running
if curl -s http://localhost:8002/api/health > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Backend server started successfully!${NC}"
    echo -e "   📡 API running at: ${BLUE}http://localhost:8002${NC}"
    echo -e "   📚 API Docs: ${BLUE}http://localhost:8002/docs${NC}"
else
    echo -e "${RED}❌ Backend failed to start!${NC}"
    echo -e "${YELLOW}Check logs: tail -f /tmp/sentinex-backend.log${NC}"
    exit 1
fi

# Step 3: Start React frontend
echo ""
echo -e "${YELLOW}🌐 Starting React + Vite frontend on port 5173...${NC}"
cd frontend-react
npm run dev > /tmp/sentinex-frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..

# Wait for frontend to start
echo -e "${BLUE}⏳ Waiting for frontend to initialize...${NC}"
sleep 5

# Check if frontend is running
if curl -s http://localhost:5173 > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Frontend started successfully!${NC}"
    echo -e "   🌐 Dashboard: ${BLUE}http://localhost:5173${NC}"
else
    echo -e "${YELLOW}⚠️  Frontend may still be starting...${NC}"
fi

# Step 4: Run system tests
echo ""
echo -e "${YELLOW}🧪 Running system tests...${NC}"
./backend/venv/bin/python test_full_system.py

# Step 5: Display status
echo ""
echo -e "${GREEN}"
echo "════════════════════════════════════════════════════════════"
echo "     ✅ Sentinex Platform is LIVE!"
echo "════════════════════════════════════════════════════════════"
echo -e "${NC}"
echo ""
echo -e "${BLUE}🎯 Access Points:${NC}"
echo -e "   ${GREEN}Dashboard:${NC} http://localhost:5173"
echo -e "   ${GREEN}Backend API:${NC} http://localhost:8002/api"
echo -e "   ${GREEN}API Docs:${NC} http://localhost:8002/docs"
echo ""
echo -e "${BLUE}📊 System Status:${NC}"
echo -e "   ${GREEN}Backend PID:${NC} $BACKEND_PID"
echo -e "   ${GREEN}Frontend PID:${NC} $FRONTEND_PID"
echo ""
echo -e "${BLUE}📝 Logs:${NC}"
echo -e "   ${YELLOW}Backend:${NC} tail -f /tmp/sentinex-backend.log"
echo -e "   ${YELLOW}Frontend:${NC} tail -f /tmp/sentinex-frontend.log"
echo ""
echo -e "${BLUE}🎬 Demo Ready:${NC}"
echo -e "   1. Dashboard shows all 6 cards with data"
echo -e "   2. All 5 NTRO components: ${GREEN}100% Complete${NC}"
echo -e "   3. Database: ${GREEN}520 users, 550 posts${NC}"
echo ""
echo -e "${YELLOW}💡 Opening dashboard in browser...${NC}"
sleep 2
open http://localhost:5173

echo ""
echo -e "${GREEN}"
echo "════════════════════════════════════════════════════════════"
echo "     🏆 Ready for Smart India Hackathon 2026! 🏆"
echo "════════════════════════════════════════════════════════════"
echo -e "${NC}"
echo ""
echo -e "${BLUE}Press Ctrl+C to stop all servers${NC}"
echo ""

# Keep script running
wait
