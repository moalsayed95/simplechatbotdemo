# Simple Chatbot Demo

Minimal Streamlit chatbot using OpenAI's Responses API.

## Prerequisites

- Python 3.10+
- OpenAI API key from [platform.openai.com](https://platform.openai.com/api-keys)

## Setup

1. Install dependencies:
   ```bash
   uv init .
   uv add openai streamlit python-dotenv
   ```

2. Create `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Run

```bash
uv run streamlit run app.py
```