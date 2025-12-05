LangGraph Agentic AI Blog Generation App
An Agentic AI project using LangGraph + FastAPI + Groq LLM to generate blog titles and full SEO-optimized blog content using a multi-step AI workflow.

🧠 Project Overview

This project demonstrates how to build an Agentic AI workflow using:

✅ LangGraph — to build multi-step AI workflows (nodes + graph)
✅ Groq LLM (Llama 3.1) — for extremely fast content creation
✅ FastAPI — for a production-ready API
✅ Pydantic + Typed States — for structured data flow

The workflow follows a 2-step agent graph:

START → Title Node → Content Node → END


This produces:

Creative SEO-friendly blog title

Long-form detailed blog content

🚀 Features

✨ Multi-step AI workflow using LangGraph

✨ Uses Groq Llama 3.1 8B Instant for blazing speed

✨ Modular structure (state → nodes → graph → API)

✨ Clean FastAPI endpoint (POST /blogs)

✨ Auto blog generation from a single topic input

✨ Fully extensible for multi-agent and RAG workflows



⚙️ Installation
1️⃣ Clone repo
git clone https://github.com/dearnidhi/langgraph-agentic-blog-app.git
cd langgraph-agentic-blog-app

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add your GROQ API key

Create .env
GROQ_API_KEY=your_api_key

▶️ Run the FastAPI server
uvicorn app:app --reload


API available at:
👉 http://127.0.0.1:8000/docs

🧪 API Usage
POST /blogs
Request:
{
  "topic": "Benefits of AI in Education"
}

Response:
{
  "data": {
    "blog": {
      "title": "The Future of AI in Education",
      "content": "Full detailed blog here..."
    }
  }
}

📦 Tech Stack
Component	Technology
AI Model	Groq Llama 3.1 8B Instant
Workflow Engine	LangGraph
Framework	FastAPI
Data Models	Pydantic

🌟 Why This Project?
This project is perfect for:
Learning LangGraph basics
Building multi-step AI workflows
Understanding Agentic AI
Creating real-world AI apps
Fast portfolio-ready project
