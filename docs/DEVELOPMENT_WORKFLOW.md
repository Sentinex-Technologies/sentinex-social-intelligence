# Development Workflow

This document explains the Git branching strategy and development workflow for **Sentinex Social Intelligence**.

---

## 🌳 Branch Structure

```
main
  ├── Stable, presentation-ready code
  ├── Only merged from develop after thorough testing
  └── Protected branch (no direct commits)
  
develop
  ├── Main development/integration branch
  ├── Features are merged here first
  └── Created from main
  
feature/*
  ├── Individual feature development
  ├── Created from develop
  └── Merged back to develop via Pull Request
```

---

## 🔄 Workflow Diagram

```
┌─────────┐
│  main   │  ← Stable, production-ready, presentation-ready
└────┬────┘
     │
     │ (merge after testing and approval)
     │
┌────▼────────┐
│   develop   │  ← Integration branch (all features merge here)
└────┬────────┘
     │
     ├──────────┬──────────┬──────────┬──────────┬──────────┐
     │          │          │          │          │          │
┌────▼──┐  ┌───▼──┐  ┌───▼──┐  ┌───▼──┐  ┌───▼──┐  ┌───▼──┐
│feature/│  │feature│  │feature│  │feature│  │feature│  │feature│
│data-   │  │/senti-│  │/trend-│  │/demo- │  │/net-  │  │/dash- │
│ingest. │  │ment   │  │detect.│  │graphic│  │work   │  │board  │
└────────┘  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘
```

---

## 🚀 Getting Started

### Initial Setup

```bash
# Clone repository
git clone <repository-url>
cd sentinex-social-intelligence

# Check current branch
git branch

# If develop doesn't exist, create it
git checkout -b develop

# Push develop to remote
git push -u origin develop
```

### Starting a New Feature

```bash
# Always start from develop
git checkout develop

# Pull latest changes
git pull origin develop

# Create feature branch
git checkout -b feature/sentiment-analysis

# Verify you're on the right branch
git branch
# * feature/sentiment-analysis
#   develop
#   main
```

---

## 💻 Development Cycle

### 1. Make Changes

```bash
# Edit files
# Add new functionality
# Write tests

# Check what changed
git status

# See differences
git diff
```

### 2. Commit Changes

```bash
# Stage all changes
git add .

# Or stage specific files
git add backend/sentiment.py
git add tests/test_sentiment.py

# Commit with meaningful message
git commit -m "feat: implement VADER sentiment analysis"

# Make multiple commits as you work
git commit -m "test: add sentiment analysis unit tests"
git commit -m "docs: update sentiment analysis documentation"
```

**Commit Message Format:**
```
<type>: <short description>

[optional detailed description]

[optional footer: Fixes #123]
```

**Types:** `feat`, `fix`, `docs`, `test`, `refactor`, `style`, `chore`, `perf`

### 3. Keep Branch Updated

```bash
# Regularly sync with develop to avoid conflicts
git checkout develop
git pull origin develop

# Go back to your feature branch
git checkout feature/sentiment-analysis

# Merge develop into your branch
git merge develop

# OR rebase (cleaner history)
git rebase develop

# Resolve conflicts if any
```

### 4. Push to Remote

```bash
# First time pushing branch
git push -u origin feature/sentiment-analysis

# Subsequent pushes
git push
```

### 5. Create Pull Request

**On GitHub/GitLab:**

1. Go to repository
2. Click **"New Pull Request"**
3. Set **base:** `develop` (target)
4. Set **compare:** `feature/sentiment-analysis` (your branch)
5. Fill in PR title and description
6. Assign reviewers
7. Add labels (if applicable)
8. Submit PR

**PR Title Examples:**
- `feat: Add sentiment analysis module`
- `fix: Handle empty social media posts`
- `docs: Update architecture documentation`

### 6. Code Review & Iteration

```bash
# Reviewer leaves comments
# Make requested changes

git add .
git commit -m "fix: address PR review comments"
git push

# PR updates automatically
# Repeat until approved
```

### 7. After Merge

```bash
# Switch back to develop
git checkout develop

# Pull merged changes
git pull origin develop

# Your feature is now in develop!

# Delete local feature branch (cleanup)
git branch -d feature/sentiment-analysis

# Delete remote branch (optional, often auto-deleted)
git push origin --delete feature/sentiment-analysis
```

---

## 🔀 Merging to Main

**Only project leads or designated members should merge to main.**

```bash
# Ensure develop is stable and tested
git checkout develop
git pull origin develop

# Run all tests
python -m pytest
npm test

# Verify everything works
# Run integration tests
# Check demo

# Switch to main
git checkout main
git pull origin main

# Merge develop into main
git merge develop

# Push to main
git push origin main

# Optionally tag release
git tag -a v0.1.0 -m "SIH prototype demo v0.1.0"
git push origin v0.1.0
```

---

## 📋 Common Scenarios

### Scenario 1: Starting a New Feature

```bash
git checkout develop
git pull origin develop
git checkout -b feature/trend-detection

# Work on feature
git add .
git commit -m "feat: implement trend detection algorithm"
git push -u origin feature/trend-detection

# Create PR on GitHub
```

### Scenario 2: Fixing a Bug

```bash
git checkout develop
git pull origin develop
git checkout -b feature/fix-empty-posts

# Fix the bug
git add .
git commit -m "fix: handle empty social media posts gracefully"
git push -u origin feature/fix-empty-posts

# Create PR
```

### Scenario 3: Working on Multiple Features

```bash
# Feature 1 - Sentiment Analysis
git checkout develop
git checkout -b feature/sentiment
# Work on sentiment
git commit -m "feat: add sentiment analysis"
git push -u origin feature/sentiment

# Switch to Feature 2 - Trend Detection
git checkout develop
git checkout -b feature/trends
# Work on trends
git commit -m "feat: add trend detection"
git push -u origin feature/trends

# Switch between features anytime
git checkout feature/sentiment   # Work on sentiment
git checkout feature/trends      # Work on trends
git checkout develop             # Back to develop
```

### Scenario 4: Updating Feature Branch with Latest Develop

```bash
# You're on feature/sentiment-analysis
git checkout develop
git pull origin develop
git checkout feature/sentiment-analysis

# Option 1: Merge (creates merge commit)
git merge develop

# Option 2: Rebase (cleaner history, recommended)
git rebase develop

# If conflicts occur during rebase:
# 1. Fix conflicts in files
# 2. git add <fixed-files>
# 3. git rebase --continue

# Push updated branch
git push --force-with-lease
```

### Scenario 5: Resolving Merge Conflicts

```bash
# Conflict occurs during merge or rebase
git status  # See conflicted files

# Open conflicted files
# Look for conflict markers:
# <<<<<<< HEAD
# Your changes
# =======
# Incoming changes
# >>>>>>> develop

# Edit to resolve, remove markers
# Save file

# Mark as resolved
git add <resolved-file>

# Continue merge/rebase
git commit  # For merge
git rebase --continue  # For rebase

git push
```

---

## ⚠️ Important Rules

### ✅ DO:
- Always work on feature branches
- Keep commits focused and atomic
- Pull from develop regularly
- Write meaningful commit messages
- Test before pushing
- Request code reviews
- Update documentation
- Delete branches after merge

### ❌ DON'T:
- Never commit directly to `main`
- Never commit to `develop` without review (except in early stages)
- Never commit API keys or credentials
- Never commit large binary files (>10MB)
- Never force push to shared branches (except your own feature)
- Never merge without approval (except in prototype phase)
- Never commit broken code
- Never ignore `.gitignore`

---

## 🆘 Troubleshooting

### Problem: "Branch is behind develop"

```bash
git checkout feature/your-feature
git fetch origin
git merge origin/develop
# Fix conflicts if any
git push
```

### Problem: "Accidentally committed to develop"

```bash
# If NOT pushed yet
git checkout main
git branch -D develop
git checkout -b develop origin/develop

# If ALREADY pushed - contact team lead immediately
```

### Problem: "Want to undo last commit"

```bash
# Keep changes, undo commit (soft reset)
git reset --soft HEAD~1

# Discard changes, undo commit (hard reset - careful!)
git reset --hard HEAD~1

# Undo last commit but keep changes staged
git reset HEAD~1
```

### Problem: "Pushed wrong files"

```bash
# Remove file from staging
git rm --cached <file>
git commit -m "chore: remove accidentally committed file"
git push

# If sensitive data (API key) was committed:
# 1. Remove file
# 2. Rotate credentials immediately
# 3. Consider using git-filter-branch or BFG Repo-Cleaner
```

### Problem: "Feature branch is very outdated"

```bash
git checkout feature/old-feature
git fetch origin
git rebase origin/develop

# Fix conflicts
git add .
git rebase --continue

git push --force-with-lease
```

---

## 🎓 Quick Reference

| Command | Description |
|---------|-------------|
| `git status` | Check current status and branch |
| `git branch` | List all branches |
| `git branch -a` | List all branches (including remote) |
| `git checkout -b feature/name` | Create & switch to new branch |
| `git checkout branch-name` | Switch to existing branch |
| `git pull origin develop` | Update from remote develop |
| `git add .` | Stage all changes |
| `git add file.py` | Stage specific file |
| `git commit -m "message"` | Commit with message |
| `git push` | Push to remote |
| `git push -u origin branch` | Push new branch to remote |
| `git log --oneline` | View commit history |
| `git log --graph --oneline --all` | Visual commit graph |
| `git diff` | See unstaged changes |
| `git diff --staged` | See staged changes |
| `git stash` | Temporarily save changes |
| `git stash pop` | Restore stashed changes |
| `git merge branch-name` | Merge branch into current |
| `git rebase branch-name` | Rebase current onto branch |
| `git branch -d branch-name` | Delete local branch |
| `git fetch origin` | Fetch remote changes |

---

## 📊 Example Workflow Timeline

**Day 1:**
```bash
git checkout develop
git pull origin develop
git checkout -b feature/sentiment-analysis
# Work on feature
git commit -m "feat: initial sentiment analysis setup"
git push -u origin feature/sentiment-analysis
```

**Day 2:**
```bash
git checkout feature/sentiment-analysis
# Continue work
git commit -m "feat: implement VADER sentiment scoring"
git commit -m "test: add sentiment analysis tests"
git push
```

**Day 3:**
```bash
# Update from develop
git checkout develop
git pull origin develop
git checkout feature/sentiment-analysis
git merge develop
# Continue work
git commit -m "docs: add sentiment analysis documentation"
git push
# Create PR
```

**Day 4:**
```bash
# Address review comments
git checkout feature/sentiment-analysis
# Make changes
git commit -m "fix: address PR review feedback"
git push
# PR approved and merged!
```

**Day 5:**
```bash
# Cleanup
git checkout develop
git pull origin develop
git branch -d feature/sentiment-analysis
# Start next feature!
```

---

## 🌟 Best Practices Summary

1. **Branch Early, Branch Often** - Create feature branches for any non-trivial work
2. **Commit Regularly** - Small, focused commits are better than large ones
3. **Pull Before Push** - Always sync with develop before pushing
4. **Test Before Commit** - Ensure code works before committing
5. **Write Clear Messages** - Future you will thank present you
6. **Review Before Merge** - Code review catches issues early
7. **Keep Branches Short-Lived** - Merge within 1-2 weeks when possible
8. **Delete After Merge** - Keep repository clean

---

## 📞 Need Help?

- **Documentation:** Check `README.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md`
- **Issues:** Search existing issues or create new one
- **Team:** Ask in team chat or tag in PR comments
- **Stuck?** Don't hesitate to ask! We're all learning.

---

**Happy Coding!** 🚀

**Organization:** Sentinex Technologies  
**Project:** SIH26152 - Social Media Analytics
