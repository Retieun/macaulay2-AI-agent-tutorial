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

