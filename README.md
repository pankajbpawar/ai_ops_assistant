# AI Operations Assistant – GenAI Intern Assignment

## Overview
This project implements an **AI Operations Assistant** using a **multi-agent architecture**
(Planner, Executor, Verifier).

The assistant accepts a natural language task, converts it into a structured execution plan
using an LLM, executes real third-party APIs, verifies results, and returns a final
human-readable response.

The system runs **locally on localhost** via CLI or FastAPI.

---

## Architecture

### 1. Planner Agent
- Converts user input into a structured JSON plan
- Uses an LLM (Groq) for planning
- Includes a rule-based fallback plan if LLM output is invalid

### 2. Executor Agent
- Executes each planned step
- Calls real APIs (GitHub, OpenWeather)
- Handles execution errors gracefully

### 3. Verifier Agent
- Validates execution results
- Formats final output for readability

---

## Integrated APIs

- **GitHub Search API** – fetches top repositories by stars
- **OpenWeather API** – fetches real-time weather by city
- **Groq LLM API** – used for structured planning

---

## Project Structure

ai_ops_assistant/
├── agents/
│ ├── planner_agent.py
│ ├── executor_agent.py
│ └── verifier_agent.py
├── tools/
│ ├── github_tool.py
│ └── weather_tool.py
├── llm/
│ └── client.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md


## How to Run the Project (For Reviewers)

Follow the steps below to run the project locally.

### Step 1: Clone the Repository
```bash
git clone https://github.com/pankajbpawar/ai_ops_assistant.git
cd ai_ops_assistant
