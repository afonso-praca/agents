# AI Course - LLM Agents

This repository contains Python scripts demonstrating the implementation of AI agents using Large Language Models (LLMs) through the LiteLLM library.

## Project Overview

The project includes two main agent implementations:

- **agent.py**: A simple AI agent that acts as a digital commerce expert, providing solutions for online businesses.
- **vtex-agent.py**: A more advanced agent that integrates with the VTEX API to list and customize email templates.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key (required for running the agents)

## Setup Instructions

### 1. Create a Python Virtual Environment

A virtual environment keeps your project dependencies isolated from your system Python installation.

**On macOS/Linux:**

```bash
# Navigate to the project directory
cd /path/to/ai-course

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

**On Windows:**

```bash
# Navigate to the project directory
cd \path\to\ai-course

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

You should see `(venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 2. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install:
- **litellm**: A unified interface for multiple LLM providers (OpenAI, Anthropic, etc.)
- **requests**: For making HTTP requests (used in vtex-agent.py)

### 3. Set Up OpenAI API Key

The agents require an OpenAI API key to function. You need to set it as an environment variable.

**On macOS/Linux:**

```bash
export OPENAI_API_KEY='your-api-key-here'
```

**On Windows (Command Prompt):**

```bash
set OPENAI_API_KEY=your-api-key-here
```

**On Windows (PowerShell):**

```bash
$env:OPENAI_API_KEY='your-api-key-here'
```

**Alternative - Using a .env file:**

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-api-key-here
```

## Running the Agents

### Running agent.py

This script demonstrates a simple agent that provides digital commerce expertise:

```bash
python3 agent.py
```

Expected output: The agent will respond to the question "If composing an ecommerce solutions architecture, what are the key components to consider?"

### Running vtex-agent.py

This script demonstrates a more complex agent that interacts with the VTEX API:

```bash
python3 vtex-agent.py
```

**Note:** This script requires a valid VTEX authentication cookie (`VtexIdclientAutCookie`) to access the VTEX API. You'll need to update line 18 in `vtex-agent.py` with your credentials.

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

## Project Structure

```
ai-course/
├── agent.py              # Simple digital commerce AI agent
├── vtex-agent.py         # VTEX email template customization agent
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── venv/                # Virtual environment (created during setup)
```

## Troubleshooting

### "Module not found" errors

Make sure you have:
1. Activated the virtual environment
2. Installed the requirements: `pip install -r requirements.txt`

### API Key errors

Ensure your `OPENAI_API_KEY` environment variable is set correctly:

```bash
echo $OPENAI_API_KEY  # macOS/Linux
echo %OPENAI_API_KEY%  # Windows Command Prompt
echo $env:OPENAI_API_KEY  # Windows PowerShell
```

### VTEX API errors

The `vtex-agent.py` script requires proper VTEX authentication. Make sure to update the `VtexIdclientAutCookie` header value with your valid credentials.

## Learning Resources

These scripts are part of an AI/LLM agents course, demonstrating:
- Basic LLM integration using LiteLLM
- Prompt engineering with system and user messages
- Tool/function calling patterns
- External API integration
- Agent design patterns and loops

## License

This project is for educational purposes.
