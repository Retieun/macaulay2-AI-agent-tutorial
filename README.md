# Macaulay2 AI Agent with Claude

AI agent powered by Claude (Anthropic) for solving algebraic geometry and commutative algebra problems using Macaulay2.

## Features

- Natural language interface for Macaulay2
- Powered by Claude Sonnet 4
- Gröbner bases, Hilbert series, resolutions
- LangChain-based agent architecture

## Prerequisites

- macOS 10.15+
- Python 3.8+
- Homebrew
- Anthropic API key with billing enabled

## Quick Start

```bash
# Install Macaulay2
brew tap macaulay2/tap
brew install macaulay2

# Clone and setup
git clone https://github.com/YOUR-USERNAME/macaulay2-agent.git
cd macaulay2-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure API key
echo 'ANTHROPIC_API_KEY=sk-ant-api03-your-key-here' > .env

# Run
python3 agent.py
```

## Installation Details

### 1. Install Homebrew (if needed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Macaulay2

```bash
brew tap macaulay2/tap
brew install macaulay2
M2 --version  # Verify installation
```

### 3. Setup Project

```bash
mkdir macaulay2-agent && cd macaulay2-agent
python3 -m venv venv
source venv/bin/activate
pip install anthropic langchain langchain-anthropic python-dotenv
```

### 4. Get API Key

1. Sign up at https://console.anthropic.com/
2. Add billing (minimum $5)
3. Create API key
4. Add to `.env` file:

```bash
echo 'ANTHROPIC_API_KEY=sk-ant-api03-your-key-here' > .env
chmod 600 .env
```

## Usage

```bash
source venv/bin/activate
python3 agent.py
```

### Example Queries

- `Compute Gröbner basis of ideal(x^2-y, xy-1) in Q[x,y]`
- `Dimension of variety x^2+y^2+z^2-1?`
- `Hilbert series of Q[x,y,z]/(x^2, y^2, z^2)`
- `Minimal free resolution of ideal(x^2, xy, y^2)`

Type `quit` to exit.

## Project Structure

```
macaulay2-agent/
├── agent.py                 # Main agent
├── macaulay2_executor.py    # M2 code executor
├── m2_tool.py              # LangChain tool wrapper
├── requirements.txt         # Dependencies
├── .env                    # API key (gitignored)
└── README.md               # This file
```

## Architecture

```
User Query → Claude Agent → Macaulay2Tool → Executor → M2 → Results → Claude → User
```

## Cost

- ~$0.05-$0.20 per query
- $5 minimum credit
- Monitor: https://console.anthropic.com/settings/usage

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `M2: command not found` | `brew install macaulay2` |
| `API key not found` | Check `.env` in project root |
| `Module not found` | `pip install -r requirements.txt` |
| Timeout errors | Increase timeout in `Macaulay2Tool(timeout=60)` |

## Security

- `.env` is gitignored by default
- Never commit API keys
- Use `.env.example` for templates

## License

MIT

## Links

- [Macaulay2](http://macaulay2.com/)
- [Claude API](https://docs.anthropic.com/)
- [LangChain](https://www.langchain.com/)
