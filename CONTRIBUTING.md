# Contributing to Idea-Enhancer

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued:

- **Report a bug**: Mention the problem you're facing.
- **Suggest a feature**: Let me know what you'd like to see.
- **Fix a typo**: Simple text fixes are welcome.
- **Improve documentation**: Documentation is part of this project.
- **Contribute code**: Submit a pull request!

> **Note:** Before you start working on any feature or submitting a bug report, please [search for existing issues](https://github.com/itzAnubis/Idea-Enhancer/issues) to see if someone else has already addressed it.

---

## 📋 How to Contribute

### **1. Reporting Bugs**

**Before submitting a bug, please check:**

- [Existing issues](https://github.com/itzAnubis/Idea-Enhancer/issues) on GitHub
- [CrewAI documentation](https://docs.crewai.com) for potential fixes

**When you file a bug report, please include:**

- A clear description of the problem
- Steps to reproduce the bug
- Expected vs actual behavior
- Your environment details (OS, Python version, crewAI version)

**Example bug report:**
```markdown
**Describe the bug**
When running the crew with a certain idea, it fails with an error.

**To Reproduce**
1. Run `uv run idea_enhancer run`
2. Enter: "Build an app for Arabic legal tech"
3. See error: `DDGS connection timeout`

**Expected behavior**
The search should retry with a fallback method.

**Environment**
- OS: Ubuntu 22.04
- Python: 3.11
- crewAI: 1.14.2
- uv: 0.5.0

**Additional context**
[Add any other context about the problem here.]
```

---

### **2. Suggesting Features**

When suggesting a feature, explain:

- **What** the feature does
- **Why** it would be useful
- **How** it would work

**Example feature request:**
```markdown
**Feature request**: Add support for Google Custom Search API

**Use case**
For users who prefer Google search over DDGS, an optional Google Custom Search provider would be helpful.

**Implementation**
Would need to add a GoogleCSearchTool similar to the existing WebSearchTool but using the Google Custom Search JSON API.
```

---

### **3. Pull Requests**

**Before submitting a pull request:**

1. **Fork** the repository
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Update documentation** if needed
6. **Submit a pull request**

**Pull request title format:**
```
feat: add new feature
fix: resolve issue with web search
docs: update README installation instructions
refactor: simplify crew.py agent configuration
test: add test for reddit search tool
chore: update dependency versions
```

**Pull request description should include:**

- What the changes do
- Why these changes are needed
- Any relevant issue numbers
- Testing performed

---

### **4. Code Style**

This project follows the **Black** and **Ruff** code style:

- **Black**: Auto-format with `uv run black .`
- **Ruff**: Lint with `uv run ruff check .`
- **Line length**: 88 characters (Black default)
- **Python version**: 3.10+

**To install pre-commit hooks:**
```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

---

### **5. Commit Messages**

Use the [Conventional Commits](https://www.conventionalcommits.org) format:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic change)
- `refactor`: Code reorganization
- `test`: Adding/fixing tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(agents): add CFO agent with financial analysis capabilities

fix(web_search): handle empty search results gracefully

docs(README): add setup instructions for Windows users

test(tools): add unit tests for WebSearchTool caching
```

---

## 🌐 Development Setup

### **Prerequisites**

- Python 3.10 or 3.11
- `uv` package manager
- Git

### **Setup Steps**

```bash
# Clone the repository
git clone https://github.com/itzAnubis/Idea-Enhancer.git
cd Idea-Enhancer

# Create a virtual environment
uv venv

# Activate it
uv sync

# Install dev dependencies
uv add -G dev

# Set up pre-commit hooks
uv run pre-commit install

# Configure your API keys
cp .env.example .env
# Edit .env with your keys
```

---

## 📁 Project Structure

```
Idea-Enhancer/
├── src/idea_enhancer/
│   ├── crew.py           # Agent orchestration
│   ├── main.py           # Entry point
│   └── tools/            # Custom tools
├── config/
│   ├── agents.yaml       # Agent definitions
│   └── tasks.yaml        # Task definitions
├── tests/                 # Unit tests
├── knowledge/             # Knowledge base
├── .github/
│   └── workflows/        # CI/CD workflows
├── .pre-commit-config.yaml  # Pre-commit hooks
└── pyproject.toml        # Project config
```

---

## 🔍 Code Review Process

All pull requests will be reviewed for:

1. **Code quality**: Follows project style guidelines
2. **Testing**: Includes appropriate test coverage
3. **Documentation**: Updates relevant docs
4. **Security**: No vulnerabilities introduced
5. **Backward compatibility**: Doesn't break existing functionality

**Review checklist:**

- [ ] Code follows existing patterns
- [ ] Tests pass locally before submitting
- [ ] Documentation is updated
- [ ] No unnecessary dependencies added
- [ ] Type hints are added for new functions

---

## 🐛 Security Policy

If you discover a security vulnerability:

1. **Do not** create a public GitHub issue
2. **Email** the maintainer directly
3. Allow time to address before public disclosure

---

## 📜 Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions.

---

## 🙏 Thank You!

Your contributions to Idea-Enhancer help make it better for everyone. Thank you for taking the time to contribute!

**Questions?** Feel free to open an issue or discussion.