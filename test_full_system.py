#!/usr/bin/env python3
"""
Comprehensive System Test - Frontend + Backend
Tests all API endpoints and frontend configuration
"""
import sys
import requests
import json
from pathlib import Path

# Colors for output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}{text.center(60)}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text):
    print(f"{RED}❌ {text}{RESET}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{RESET}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{RESET}")

# Test Configuration
API_BASE = "http://localhost:8002"
TIMEOUT = 5

# Test Results
total_tests = 0
passed_tests = 0
failed_tests = 0
errors = []

def test_endpoint(name, url, method="GET", expected_status=200, data=None):
    """Test a single API endpoint"""
    global total_tests, passed_tests, failed_tests, errors
    total_tests += 1
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=TIMEOUT)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=TIMEOUT)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        if response.status_code == expected_status:
            passed_tests += 1
            print_success(f"{name}: {response.status_code}")
            try:
                data = response.json()
                print(f"   Response keys: {list(data.keys()) if isinstance(data, dict) else 'list'}")
            except:
                pass
            return True
        else:
            failed_tests += 1
            error_msg = f"{name}: Got {response.status_code}, expected {expected_status}"
            print_error(error_msg)
            errors.append(error_msg)
            try:
                print(f"   Response: {response.text[:200]}")
            except:
                pass
            return False
            
    except requests.exceptions.ConnectionError:
        failed_tests += 1
        error_msg = f"{name}: Connection refused! Is backend running on {API_BASE}?"
        print_error(error_msg)
        errors.append(error_msg)
        return False
    except Exception as e:
        failed_tests += 1
        error_msg = f"{name}: {str(e)}"
        print_error(error_msg)
        errors.append(error_msg)
        return False

def check_frontend():
    """Check React frontend configuration"""
    global total_tests, passed_tests, failed_tests, errors
    
    print_header("FRONTEND CONFIGURATION CHECK")
    
    frontend_file = Path(__file__).parent / "frontend-react" / "src" / "App.jsx"
    
    total_tests += 1
    if not frontend_file.exists():
        failed_tests += 1
        error_msg = "React frontend file not found!"
        print_error(error_msg)
        errors.append(error_msg)
        return
    
    passed_tests += 1
    print_success(f"React frontend found: {frontend_file}")
    
    # Check API_BASE configuration
    content = frontend_file.read_text()
    
    total_tests += 1
    if "const API_BASE = '/api'" in content:
        passed_tests += 1
        print_success("API_BASE correctly configured (Vite proxy)")
    else:
        failed_tests += 1
        error_msg = "API_BASE configuration not found or incorrect"
        print_error(error_msg)
        errors.append(error_msg)
    
    # Check if all required API calls are present
    total_tests += 1
    required_endpoints = [
        '/data/stats',
        '/posts/sentiment/distribution',
        '/network/statistics',
        '/sentiment/emotions',
        '/posts/topics'
    ]
    
    all_found = True
    for endpoint in required_endpoints:
        if endpoint not in content:
            print_warning(f"Endpoint not found in frontend: {endpoint}")
            all_found = False
    
    if all_found:
        passed_tests += 1
        print_success("All required API endpoints are referenced in React frontend")
    else:
        failed_tests += 1
        error_msg = "Some API endpoints missing from frontend"
        print_error(error_msg)
        errors.append(error_msg)

def check_backend_health():
    """Check if backend server is running"""
    print_header("BACKEND SERVER CHECK")
    
    print_info(f"Checking backend at: {API_BASE}")
    
    if not test_endpoint("Health Check", f"{API_BASE}/api/health"):
        print_error("\n🚨 BACKEND IS NOT RUNNING! 🚨")
        print_info("Start backend with:")
        print_info("  cd backend")
        print_info("  ./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8002")
        return False
    return True

def test_api_endpoints():
    """Test all API endpoints"""
    print_header("API ENDPOINTS TEST")
    
    endpoints = [
        ("Data Statistics", f"{API_BASE}/api/data/stats"),
        ("Network Statistics", f"{API_BASE}/api/network/statistics"),
        ("Sentiment Distribution", f"{API_BASE}/api/posts/sentiment/distribution?days_back=30"),
        ("Emotion Analysis", f"{API_BASE}/api/sentiment/emotions?days_back=7"),
        ("Trending Topics", f"{API_BASE}/api/posts/topics?days_back=7&limit=10"),
        ("Trending Hashtags", f"{API_BASE}/api/posts/trending?days_back=7&limit=10"),
    ]
    
    for name, url in endpoints:
        test_endpoint(name, url)

def check_database():
    """Check database status"""
    print_header("DATABASE CHECK")
    
    try:
        response = requests.get(f"{API_BASE}/api/data/stats", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print_success(f"Total Users: {data.get('total_users', 0)}")
            print_success(f"Total Posts: {data.get('total_posts', 0)}")
            
            if data.get('total_users', 0) > 0 and data.get('total_posts', 0) > 0:
                print_success("Database has data!")
            else:
                print_warning("Database is empty - need to generate data")
                print_info("Generate data:")
                print_info("  POST /api/data/generate?num_users=100&num_posts=500")
    except Exception as e:
        print_error(f"Could not check database: {e}")

def main():
    """Run all tests"""
    print_header("🚀 SENTINEX SYSTEM TEST - COMPREHENSIVE CHECK 🚀")
    
    # Check frontend
    check_frontend()
    
    # Check backend
    if not check_backend_health():
        print_header("SUMMARY")
        print_error("Backend is not running! Cannot continue tests.")
        sys.exit(1)
    
    # Test API endpoints
    test_api_endpoints()
    
    # Check database
    check_database()
    
    # Print summary
    print_header("TEST SUMMARY")
    print(f"Total Tests: {total_tests}")
    print_success(f"Passed: {passed_tests}")
    if failed_tests > 0:
        print_error(f"Failed: {failed_tests}")
    
    if errors:
        print_header("ERRORS FOUND")
        for i, error in enumerate(errors, 1):
            print(f"{i}. {RED}{error}{RESET}")
    
    print_header("STATUS")
    if failed_tests == 0:
        print_success("🎉 ALL TESTS PASSED! System is working perfectly!")
        print_info("Frontend: http://localhost:5173 (React + Vite)")
        print_info("Backend: http://localhost:8002")
        print_info("API Docs: http://localhost:8002/docs")
        sys.exit(0)
    else:
        print_error(f"❌ {failed_tests} test(s) failed!")
        print_warning("Please fix the errors above before demo")
        sys.exit(1)

if __name__ == "__main__":
    main()
