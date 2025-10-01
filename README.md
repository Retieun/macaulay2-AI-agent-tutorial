# Macaulay2 AI Agent with Claude - Complete Mac Setup Guide

A step-by-step beginner's guide to building an AI agent that uses Claude (Anthropic) to solve algebraic geometry and commutative algebra problems with Macaulay2.

## 🎯 What You'll Build

An intelligent agent that can:
- Understand mathematical questions in plain English
- Generate and execute Macaulay2 code
- Compute Gröbner bases, Hilbert series, resolutions
- Explain results clearly

## 📋 Prerequisites

- **Mac computer or Linux** (macOS 10.15 or later)
- **No coding experience required!**
- **API account** with billing, here I use Anthropic as an example
- About 1 hour to complete setup

## 💰 Cost

- **Anthropic API**: Requires $5 minimum credit (~$0.05-$0.20 per query)
- **Everything else**: Free

---

##  1. Install Dependencies
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Macaulay2
brew tap macaulay2/tap
brew install macaulay2

# Verify
M2 --version

##  2.  Setup Project
# Create project
mkdir macaulay2-agent && cd macaulay2-agent

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install anthropic langchain langchain-anthropic python-dotenv

##  3.  Configure API Key
#  Create .env file
echo 'ANTHROPIC_API_KEY=sk-ant-api03-your-key-here' > .env
chmod 600 .env
#  Project Structure
macaulay2-agent/
├── agent.py                 # Main agent
├── macaulay2_executor.py    # M2 code executor
├── m2_tool.py              # LangChain tool wrapper
├── .env                    # API key (gitignored)
└── requirements.txt         # Dependencies



