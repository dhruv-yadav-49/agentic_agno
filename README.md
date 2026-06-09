# Agentic Agno AI Agents

This repository contains two autonomous AI agents built using the **Agno** (formerly Phidata) framework and powered by **Groq** (`llama-3.3-70b-versatile` and `qwen/qwen3-32b`).

## Projects

### 1. Travel Agent (`agent.py`)
An expert travel assistant that advises on travel safety, itineraries, and queries. It is equipped with **DuckDuckGo Search Tools** to fetch real-time information from the web.

### 2. Investment Analyst (`finance.py`)
An investment analysis agent designed to research stock prices, fundamentals, and analyst recommendations. It uses **Yahoo Finance Tools** and **DuckDuckGo Search Tools** to gather and display data in structured tables.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dhruv-yadav-49/agentic_agno.git
   cd agentic_agno
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install agno python-dotenv openai groq yfinance duckduckgo-search
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your keys:
   ```env
   GROQ_API_KEY="your-groq-api-key"
   ```

5. **Run the agents:**
   * Travel Agent:
     ```bash
     python agent.py
     ```
   * Financial Agent:
     ```bash
     python finance.py
     ```
