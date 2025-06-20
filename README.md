# 🚀 Hackathon: AI-powered Workflow Agent in a Sandboxed Environment

**DevShellBot** is an AI-powered agent that automates repetitive developer tasks by translating natural language instructions into safe Bash commands. Originally designed to run inside a Docker sandbox, this version uses local execution (`subprocess`) due to hardware limitations. The architecture remains sandbox-ready and can be upgraded on compatible systems.

---

## ✨ Features

- 🧠 Natural language → Bash (via GPT-3.5)
- 🧪 Shell command execution with output logging
- 📂 File-safe: commands only affect mounted sandbox folder
- 🔐 Supports Docker sandboxing (with fallback to local execution)
- 📜 Logs all actions to `logs/log.txt` for transparency and audit

---

## 🔧 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/JasonZeng24/Hackathon-AI-powered-Workflow-Agent-in-a-Sandboxed-Environment.git
   cd Hackathon-AI-powered-Workflow-Agent-in-a-Sandboxed-Environment
