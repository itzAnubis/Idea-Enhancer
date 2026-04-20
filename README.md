# Idea-Enhancer

> An AI-powered executive board (CEO, CTO, CFO, CMO) that transforms your project ideas into comprehensive investor-ready blueprints with market validation, competitor analysis, and Reddit community insights.

[![Python Version](https://img.shields.io/pypi/pyversions/idea_enhancer)](https://pypi.org/project/idea_enhancer)
[![crewAI](https://img.shields.io/badge/crewAI-1.14.2-blue)](https://crewai.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2F3.11-3498db.svg)](https://www.python.org/)

---

## 🎯 What Is Idea-Enhancer?

Idea-Enhancer is a multi-agent AI system that simulates an executive board discussion around your project ideas. It automatically:

- **Validates your idea** through technical, market, and financial analysis
- **Researches competitors** and identifies market gaps
- **Analyzes Reddit discussions** to understand user pain points and feature requests
- **Generates a master blueprint** formatted for investor pitches

Perfect for entrepreneurs, solo founders, and product managers who need structured idea validation before building.

---

## 🚀 Key Features

| Feature | Description |
|---------|-------------|
| **Executive Board Simulation** | CEO/CTO/CFO/CMO agents collaborate hierarchically to analyze your idea |
| **Market Validation** | Automatic competitor research, pricing strategy, and go-to-market analysis |
| **Reddit Insights** | Real community feedback analysis with sentiment and trending topics |
| **Privacy-Focused Recommendations** | On-device LLM and offline capability suggestions for sensitive domains |
| **SWOT Analysis** | Initial idea critique with strategic clarity assessment |

---

## 🛠️ Installation

### System Requirements

- Python 3.10 or 3.11
- `uv` package manager (recommended)

### Setup

```bash
# Clone and navigate to project
cd Idea-Enhancer

# Install dependencies using UV
uv sync

# Configure your API keys
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY, SERPER_API_KEY, etc.
```

### Quick Start

```bash
# Enter an idea
echo "Build an app for Arabic legal tech" | uv run idea_enhancer run
```

The crew will generate `enhanced_idea_report.md` in the project root with the full analysis.

---

## 💡 Usage

### Basic Execution

```bash
# Interactive mode
uv run idea_enhancer run

# Run with a specific idea
uv run idea_enhancer run --idea "Build an app for Arabic legal tech"
```

### Training & Testing

```bash
# Train the crew on your ideas
uv run idea_enhancer train -n 5 -f training.json

# Test crew execution
uv run idea_enhancer test
```

### Advanced Options

```bash
# Replay from a specific task
uv run idea_enhancer replay -t <task_id>

# Run with trigger payload (for automation)
uv run idea_enhancer run_with_trigger -- '{"topic": "AI Agents"}'
```

---

## 📁 Project Structure

```
Idea-Enhancer/
├── src/idea_enhancer/
│   ├── crew.py           # Agent orchestration
│   ├── main.py           # Entry point with CLI commands
│   ├── __init__.py
│   └── tools/
│       ├── custom_tool.py   # WebSearchTool (DDGS-based)
│       ├── reddit_tool.py   # RedditSearchTool
│       └── __init__.py
├── config/
│   ├── agents.yaml       # Agent definitions (CEO, CTO, CFO, CMO)
│   └── tasks.yaml        # Task definitions
├── knowledge/            # Knowledge base resources
├── tests/                # Tool tests
├── pyproject.toml        # Project metadata & dependencies
├── uv.lock               # UV lockfile
├── .env                  # Environment variables (API keys)
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── AGENTS.md             # CrewAI reference documentation
```

---

## 🤖 The Executive Board Agents

### CEO (Chief Executive Officer)
- **Role**: Overall strategic direction and stakeholder management
- **Capabilities**: Human input integration, high-stakes decision-making
- **Tools**: Direct human feedback integration

### CTO (Chief Technology Officer)
- **Role**: Technical architecture and product development
- **Capabilities**: Web search for tech specs and benchmarks
- **Tools**: Web search (DDGS)

### CFO (Chief Financial Officer)
- **Role**: Financial planning and risk assessment
- **Capabilities**: SaaS pricing research, unit economics analysis
- **Tools**: Web search for market data

### CMO (Chief Marketing Officer)
- **Role**: Brand awareness and customer acquisition
- **Capabilities**: Reddit search for user insights and feature requests
- **Tools**: Web search + Reddit search

---

## 📊 Output Format

The final report (`enhanced_idea_report.md`) includes:

```markdown
# Master Project Blueprint: {your_idea}

## 🎯 Executive Vision
[1-2 paragraph pitch]

## ⚙️ Technical Architecture
- Stack & Models (offline/local)
- Data Flow & Privacy Controls
- Hardware Requirements

## 📊 Market & Go-to-Market
- Target Segments
- Competitor Positioning
- Pricing Tiers
- Reddit Community Insights

## 💰 Financial & Risk
- Development Cost Estimate
- Liability & Compliance Mitigation
- 12-Month Roadmap

## 📱 Reddit Discussion Summary
- Hot Posts & Trending Topics
- Key User Concerns & Feature Requests
- Sentiment Analysis
```

---

## 🔧 Configuration

### Customizing Agents

Edit `src/idea_enhancer/config/agents.yaml` to modify agent roles, goals, and backstories.

### Customizing Tasks

Edit `src/idea_enhancer/config/tasks.yaml` to adjust task descriptions and expected outputs.

### Adding Custom Tools

1. Create a new tool in `src/idea_enhancer/tools/`
2. Export it in `src/idea_enhancer/tools/__init__.py`
3. Import in `src/idea_enhancer/crew.py`

See [`AGENTS.md`](AGENTS.md) for the complete CrewAI reference.

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
# Required
OPENAI_API_KEY=sk-your-openai-api-key-here

# Optional (depending on tools used)
SERPER_API_KEY=your-serper-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

---

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# View detailed output
uv run pytest -v
```

Tests are located in the `tests/` directory and cover:
- Web search functionality
- Reddit search functionality

---

## 📚 Resources

- **[CrewAI Documentation](https://docs.crewai.com)** - Official documentation
- **[CrewAI GitHub](https://github.com/crewAIInc/crewai)** - Source code and issues
- **[Discord Community](https://discord.com/invite/X4JWnZnxPb)** - Join our discussions

---



```bash
# Clone and navigate to project
cd Idea-Enhancer

# Install dependencies using UV
uv sync

# Configure your API keys
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY, SERPER_API_KEY, etc.
```

### Quick Start

```bash
# Enter an idea
echo "Build an app for Arabic legal tech" | uv run idea_enhancer run
```

The crew will generate `enhanced_idea_report.md` in the project root with the full analysis.

---

## 💡 Usage

### Basic Execution

```bash
# Interactive mode
uv run idea_enhancer run

# Run with a specific idea
uv run idea_enhancer run --idea "Build an app for Arabic legal tech"
```

### Training & Testing

```bash
# Train the crew on your ideas
uv run idea_enhancer train -n 5 -f training.json

# Test crew execution
uv run idea_enhancer test
```

### Advanced Options

```bash
# Replay from a specific task
uv run idea_enhancer replay -t <task_id>

# Run with trigger payload (for automation)
uv run idea_enhancer run_with_trigger -- '{"topic": "AI Agents"}'
```

---

## 📁 Project Structure

```
Idea-Enhancer/
├── src/idea_enhancer/
│   ├── crew.py           # Agent orchestration
│   ├── main.py           # Entry point with CLI commands
│   ├── __init__.py
│   └── tools/
│       ├── custom_tool.py   # WebSearchTool (DDGS-based)
│       ├── reddit_tool.py   # RedditSearchTool
│       └── __init__.py
├── config/
│   ├── agents.yaml       # Agent definitions (CEO, CTO, CFO, CMO)
│   └── tasks.yaml        # Task definitions
├── knowledge/            # Knowledge base resources
├── tests/                # Tool tests
├── pyproject.toml        # Project metadata & dependencies
├── uv.lock               # UV lockfile
├── .env                  # Environment variables (API keys)
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── AGENTS.md             # CrewAI reference documentation
```

---

## 🤖 The Executive Board Agents

### CEO (Chief Executive Officer)
- **Role**: Overall strategic direction and stakeholder management
- **Capabilities**: Human input integration, high-stakes decision-making
- **Tools**: Direct human feedback integration

### CTO (Chief Technology Officer)
- **Role**: Technical architecture and product development
- **Capabilities**: Web search for tech specs and benchmarks
- **Tools**: Web search (DDGS)

### CFO (Chief Financial Officer)
- **Role**: Financial planning and risk assessment
- **Capabilities**: SaaS pricing research, unit economics analysis
- **Tools**: Web search for market data

### CMO (Chief Marketing Officer)
- **Role**: Brand awareness and customer acquisition
- **Capabilities**: Reddit search for user insights and feature requests
- **Tools**: Web search + Reddit search

---

## 📊 Output Format

The final report (`enhanced_idea_report.md`) includes:

```markdown
# Master Project Blueprint: {your_idea}

## 🎯 Executive Vision
[1-2 paragraph pitch]

## ⚙️ Technical Architecture
- Stack & Models (offline/local)
- Data Flow & Privacy Controls
- Hardware Requirements

## 📊 Market & Go-to-Market
- Target Segments
- Competitor Positioning
- Pricing Tiers
- Reddit Community Insights

## 💰 Financial & Risk
- Development Cost Estimate
- Liability & Compliance Mitigation
- 12-Month Roadmap

## 📱 Reddit Discussion Summary
- Hot Posts & Trending Topics
- Key User Concerns & Feature Requests
- Sentiment Analysis
```

---

## 🔧 Configuration

### Customizing Agents

Edit `src/idea_enhancer/config/agents.yaml` to modify agent roles, goals, and backstories.

### Customizing Tasks

Edit `src/idea_enhancer/config/tasks.yaml` to adjust task descriptions and expected outputs.

### Adding Custom Tools

1. Create a new tool in `src/idea_enhancer/tools/`
2. Export it in `src/idea_enhancer/tools/__init__.py`
3. Import in `src/idea_enhancer/crew.py`

See [`AGENTS.md`](AGENTS.md) for the complete CrewAI reference.

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
# Required
OPENAI_API_KEY=sk-your-openai-api-key-here

# Optional (depending on tools used)
SERPER_API_KEY=your-serper-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

---

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# View detailed output
uv run pytest -v
```

Tests are located in the `tests/` directory and cover:
- Web search functionality
- Reddit search functionality

---

## 📚 Resources

- **[CrewAI Documentation](https://docs.crewai.com)** - Official documentation
- **[CrewAI GitHub](https://github.com/crewAIInc/crewai)** - Source code and issues
- **[Discord Community](https://discord.com/invite/X4JWnZnxPb)** - Join our discussions

---


## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

For support, questions, or feedback:

- Visit our [documentation](https://docs.crewai.com)
- Open an [issue](https://github.com/itzAnubis/Idea-Enhancer/issues) on GitHub

---

## 🙏 Acknowledgments

- Built with [crewAI](https://crewai.com)
- Web search powered by [DDGS](https://github.com/Sciter/ddgs)
- Reddit search using [praw](https://praw.readthedocs.io/)