# Hackathon: AI-powered Workflow Agent in a Sandboxed Environment

**DevShellBot** is a simple AI agent that translates natural language into bash commands and runs them securely inside a Docker container.
⚠️ Due to hardware limitations (incompatible CPU for Docker), the current version uses local execution with subprocess instead of Docker sandbox. The architecture remains the same and fully supports secure execution with sandboxing where compatible.

## 🚀 Usage

1. Build Docker image:
```bash
docker build -t devshell .