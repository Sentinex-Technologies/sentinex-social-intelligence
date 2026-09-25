# Contributing to Sentinex Social Intelligence

Thank you for contributing to the **SIH26152 Social Media Analytics** project!

## 🔄 Development Workflow

### Branch Strategy

```
main (stable, presentation-ready)
  ↑
develop (integration/development)
  ↑
feature/* (individual features)
```

### Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sentinex-social-intelligence
   ```

2. **Switch to develop branch**
   ```bash
   git checkout develop
   git pull origin develop
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

   **Branch naming examples:**
   - `feature/sentiment-analysis`
   - `feature/trend-detection`
   - `feature/dashboard`
   - `feature/data-ingestion`
   - `feature/network-analysis`
   - `feature/demographic-insights`

---

## 💻 Development Process

### 1. Implement Your Feature

- Keep changes focused on **one feature**
- Write clean, well-documented code
- Follow coding standards
- Add tests if applicable

### 2. Test Locally

```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

Ensure:
- ✅ All tests pass
- ✅ No errors in console
- ✅ Feature works as expected

### 3. Commit Your Changes

```bash
git add .
git commit -m "feat: add sentiment analysis pipeline"
```

---

## 📝 Commit Message Convention

Use meaningful commit messages following this format:

```
<type>: <description>

[optional body]
[optional footer]
```

### Types

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Adding or updating tests
- `refactor:` - Code refactoring (no functionality change)
- `style:` - Code style changes (formatting, semicolons, etc.)
- `chore:` - Maintenance tasks (dependencies, configs, etc.)
- `perf:` - Performance improvements

### Examples

```bash
git commit -m "feat: add sentiment analysis using VADER"
git commit -m "fix: handle empty social media posts"
git commit -m "docs: update architecture documentation"
git commit -m "test: add trend detection unit tests"
git commit -m "refactor: simplify data processing pipeline"
git commit -m "chore: update dependencies"
```

---

## 🚀 Pull Request Process

### 1. Push Your Branch

```bash
git push origin feature/your-feature-name
```

### 2. Open Pull Request

1. Go to GitHub/repository
2. Click **"New Pull Request"**
3. Set **base:** `develop`
4. Set **compare:** `feature/your-feature-name`
5. Fill in PR description (use template below)

### 3. Pull Request Template

```markdown
## Description
Brief description of what this PR does

## Changes
- Change 1: Added sentiment analysis module
- Change 2: Updated API endpoints
- Change 3: Added unit tests

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots for UI changes

## Related Issues
Fixes #issue-number (if applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No sensitive data committed
```

### 4. Code Review

- Wait for team review
- Address review comments
- Make requested changes
- Push updates to the same branch (PR auto-updates)

```bash
# Make changes based on feedback
git add .
git commit -m "fix: address PR review comments"
git push
```

### 5. Merge

- After approval, PR will be merged to `develop`
- **Delete your feature branch** after merge

```bash
git checkout develop
git pull origin develop
git branch -d feature/your-feature-name
```

---

## 🚫 What NOT to Commit

**NEVER commit:**

- ❌ API keys or access tokens
- ❌ Passwords or credentials
- ❌ `.env` files with real values
- ❌ Database files with real data (*.db, *.sqlite)
- ❌ Personal information
- ❌ Large binary files (except approved assets)
- ❌ Scraped data with personal info
- ❌ Private keys or certificates

**✅ Use `.env.example` for templates only**

---

## 🧪 Testing Guidelines

### Backend (Python)

```bash
cd backend
python -m pytest tests/
python -m pytest --cov=.
```

### Frontend (React)

```bash
cd frontend
npm test
npm run test:coverage
```

### Integration Tests

```bash
# Test full pipeline
npm run test:integration
```

**Testing Best Practices:**
- Write tests for new features
- Ensure existing tests pass
- Test edge cases
- Document test coverage
- Mock external API calls

---

## 📝 Code Style Guidelines

### Python (Backend)

- Follow **PEP 8** style guide
- Use **type hints** for functions
- Add **docstrings** for modules, classes, functions
- Maximum line length: **88 characters** (Black formatter)
- Use **meaningful variable names**

```python
def analyze_sentiment(text: str) -> dict:
    """
    Analyze sentiment of social media text.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Sentiment results with polarity and confidence
    """
    # Implementation
    pass
```

### JavaScript/React (Frontend)

- Follow **ESLint** configuration
- Use **Prettier** for formatting
- Use **functional components** with hooks
- Use **meaningful component names**
- Add **PropTypes** or TypeScript types

```javascript
// Good
const SentimentChart = ({ data, loading }) => {
  // Implementation
};

// Bad
const comp1 = (props) => { /* ... */ };
```

### General Guidelines

- Keep functions **small and focused**
- **One function = one responsibility**
- Use **descriptive variable names**
- Avoid magic numbers (use constants)
- Comment complex logic

---

## 🔐 Security Guidelines

### DO:
✅ Use environment variables for secrets  
✅ Validate all user inputs  
✅ Sanitize data before processing  
✅ Follow secure coding practices  
✅ Use HTTPS for API calls  
✅ Implement rate limiting  
✅ Report security issues privately  

### DON'T:
❌ Hardcode credentials  
❌ Commit `.env` files  
❌ Expose sensitive data in logs  
❌ Store passwords in plain text  
❌ Ignore security warnings  

---

## 📚 Documentation

### When to Update Docs

- ✅ Adding new features
- ✅ Changing APIs
- ✅ Updating architecture
- ✅ Fixing bugs (if user-facing)
- ✅ Adding configuration options

### Documentation Files

- `README.md` - Project overview, setup instructions
- `docs/ARCHITECTURE.md` - System architecture
- `docs/DEVELOPMENT_WORKFLOW.md` - Git workflow
- Code comments - Inline documentation
- API documentation - Endpoint descriptions

---

## 🆘 Getting Help

### Stuck? Here's what to do:

1. **Check existing documentation**
   - Read README.md
   - Check docs/ folder
   - Review ARCHITECTURE.md

2. **Search for similar issues**
   - Check closed issues
   - Search pull requests
   - Look for discussions

3. **Ask the team**
   - Open a GitHub issue
   - Ask in team chat
   - Request help in PR comments

4. **Report bugs**
   - Use issue template
   - Provide reproduction steps
   - Include error logs

---

## ✅ Pre-Submission Checklist

Before submitting your Pull Request, verify:

- [ ] ✅ Code follows style guidelines (PEP 8 / ESLint)
- [ ] ✅ All tests pass locally
- [ ] ✅ Documentation updated
- [ ] ✅ No sensitive data committed (check git diff)
- [ ] ✅ Commit messages are clear and follow convention
- [ ] ✅ Branch is up to date with `develop`
- [ ] ✅ PR description is complete
- [ ] ✅ No merge conflicts
- [ ] ✅ Feature works as expected
- [ ] ✅ Code is well-commented

---

## 🎯 Team Roles

This project is designed for **6 developers** working on different modules:

| Developer | Focus Area | Feature Branch |
|-----------|-----------|----------------|
| Dev 1 | Data Ingestion | `feature/data-ingestion` |
| Dev 2 | Sentiment Analysis | `feature/sentiment-analysis` |
| Dev 3 | Trend Detection | `feature/trend-detection` |
| Dev 4 | Demographic Analysis | `feature/demographic-analysis` |
| Dev 5 | Network Analysis | `feature/network-analysis` |
| Dev 6 | Dashboard & Visualization | `feature/dashboard` |

**Note:** Roles are flexible. Developers can contribute to multiple areas.

---

## 🌟 Best Practices

### Git Best Practices
- Commit often, push regularly
- Keep commits atomic (one logical change per commit)
- Pull from `develop` before starting work
- Rebase instead of merge when appropriate
- Delete branches after merge

### Code Review Best Practices
- Be respectful and constructive
- Explain the "why" behind suggestions
- Approve quickly if changes are good
- Request changes with clear explanations
- Test the code if possible

### Development Best Practices
- Write self-documenting code
- Test edge cases
- Handle errors gracefully
- Log important events
- Optimize only when needed
- Prioritize readability over cleverness

---

## 📞 Contact

**Organization:** Sentinex Technologies  
**Project:** SIH26152 - Social Media Analytics  
**Repository:** sentinex-social-intelligence  

For questions or issues:
- Open a GitHub issue
- Contact team lead
- Check documentation first

---

## 🙏 Thank You!

Your contributions make Sentinex Social Intelligence better!

**Happy Coding!** 🚀
