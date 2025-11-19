🚀 Mini AI Interview Screener (Backend Only)

A lightweight FastAPI backend that evaluates candidate interview answers using an LLM and ranks multiple responses based on score.
Designed to be clean, fast, and easy to understand — perfect for real-world screening workflows.

⚡ Features
🧠 1. /evaluate-answer

Takes a single candidate answer and returns:

A score from 1 to 5

A short one-line summary

One improvement suggestion


📊 2. /rank-candidates

Takes an array of answers and:

Evaluates each one using the same LLM logic

Sorts candidates from highest → lowest score

Returns a clean JSON list


✨ Additional

Predictable, structured JSON responses

Safe JSON parsing to avoid model formatting issues

Minimal + readable architecture

Automatically documented via Swagger UI (/docs)

🛠️ Tech Stack & Why I Chose It

FastAPI
I picked FastAPI because it is:Extremely lightweight,Fast and async-friendly,Automatically generates live API docs
Perfect for small real-world backend services

OpenAI (gpt-4o-mini) 
Used as the evaluation engine because:It handles structured JSON instructions reliably,Low latency for quick scoring,Simple integration using the Python SDK

Architecture Philosophy
The app is intentionally simple:Entire logic in a single file for easy review,One evaluation function reused across endpoints,Minimal dependencies and clear flow
Product-engineering mindset: no over-engineering

📦 Setup Instructions
Clone the repository:
```bash
git clone https://github.com/JOYDALAL7/mini-ai-interview-screener
cd mini-ai-interview-screener
```

Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create your .env file:
```
OPENAI_API_KEY=your_api_key_here
```

Run the server:
```bash
uvicorn main:app --reload
```

Open the interactive API docs:
👉 http://127.0.0.1:8000/docs


🧩 Project Structure
```bash
mini-ai-interview-screener/
│── main.py
│── requirements.txt
│── .env.example
│── .gitignore
│── LICENSE
└── README.md
```

🎥 Loom Walkthrough

A short walkthrough video explaining:
Code structure
Endpoint logic
Live testing in Swagger UI
