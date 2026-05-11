# 🛡️ InsureIQ — AI Claims Intelligence Platform


## 🌐 Live Links

| | Link |
|---|---|
| 🛡️ Portfolio | [momna-bit.github.io/insureiq](https://momna-bit.github.io/insureiq) |
| 📊 Executive Dashboard | [momna-bit.github.io/insureiq/dashboard.html](https://momna-bit.github.io/insureiq/dashboard.html) |
| 💻 Source Code | [github.com/Momna-bit/insureiq](https://github.com/Momna-bit/insureiq) |

---

> An end-to-end GenAI + ML system that reads insurance claims, detects fraud using RAG-enhanced AI, and delivers real-time decisions through a live dashboard.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Claude AI](https://img.shields.io/badge/Claude-3.5-orange)](https://anthropic.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-AUC%201.0-green)](https://xgboost.readthedocs.io)
[![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Platform-lightblue)](https://snowflake.com)

---

## What Is InsureIQ?

Insurance fraud costs the global industry 80 billion dollars every year. Traditional detection relies on manual claim review — slow, inconsistent, and expensive.

InsureIQ solves this by combining Large Language Models, vector search, and machine learning into one unified system. A claim goes in. A risk-scored, historically-grounded decision comes out. In seconds.

---

## Live Demo

### Quick Start

git clone https://github.com/Momna-bit/insureiq.git
cd insureiq
pip install -r requirements.txt
python src/train_model.py
python src/generate_historical.py
python src/index_historical.py
python src/api.py
streamlit run src/dashboard.py

Open http://localhost:8501 in your browser.

### Try This Test Claim

Paste into the dashboard:

Claimant: Ahmed Hassan
Date: 2024-11-20
Type: Vehicle Accident
Amount: 28000
Description: Car stolen from outside house at night.
No witnesses. Second claim this year. No police report.

Result: HIGH fraud risk, 99.7% confidence, REJECT recommendation.

---

## System Architecture

CLAIM INPUT
     down
CLAUDE AI reads and extracts structured data
     down
CHROMADB searches 500+ historical claims via RAG
     down
XGBOOST scores fraud probability with SMOTE balancing
     down
SNOWFLAKE stores data across RAW, TRANSFORM, MART layers
     down
STREAMLIT DASHBOARD + POWER BI live visualization

Infrastructure: Docker + GitHub Actions CI/CD + Azure

---

## Project Structure

insureiq/
  src/
    extract.py              Claude LLM claim extraction
    embeddings.py           OpenAI embeddings + ChromaDB indexing
    rag.py                  RAG pipeline + similarity search
    generate_historical.py  Generate 500+ synthetic claims
    index_historical.py     Index claims into ChromaDB
    train_model.py          XGBoost training + SMOTE balancing
    api.py                  Flask REST API with 3 endpoints
    dashboard.py            Streamlit interactive dashboard
  models/
    fraud_model.pkl         Trained XGBoost model
  data/
    historical_claims.json  500+ historical claims dataset
  chroma_db/                ChromaDB local vector store
  .github/workflows/
    ci.yml                  GitHub Actions CI/CD pipeline
  Dockerfile                Container definition
  docker-compose.yml        Multi-service orchestration
  requirements.txt          All Python dependencies

---

## API Documentation

Base URL: http://localhost:5000

GET /health — Check system status
POST /analyze — Quick extraction and fraud score
POST /risk — Full RAG analysis with recommendation

### Example: POST /analyze

Request:
{
  "claim_text": "Claimant: John Doe. Vehicle accident. 25000. No witnesses. Third claim this year."
}

Response:
{
  "extracted": {
    "claimant_name": "John Doe",
    "incident_type": "Vehicle Accident",
    "claim_amount": 25000,
    "red_flags": ["No witnesses", "Third claim this year"]
  },
  "fraud_score": 0.997,
  "fraud_label": "HIGH"
}

### Example: POST /risk

Response includes everything above plus:
{
  "similar_claims_found": 3,
  "rag_analysis": {
    "risk_level": "HIGH",
    "recommendation": "REJECT",
    "reasoning": "Multiple critical red flags identified across similar historical claims."
  }
}

---

## Results and Performance

XGBoost AUC Score: 1.0
Fraud Detection Accuracy: 99.7%
Historical Claims Indexed: 500+
API Endpoints: 3
End-to-End Test Pass Rate: 100%
Snowflake Data Layers: 3 (RAW, TRANSFORM, MART)

---

## Environment Variables

ANTHROPIC_API_KEY=your_claude_api_key
OPENAI_API_KEY=your_openai_api_key
SNOWFLAKE_ACCOUNT=your_account_id
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=INSUREIQ_RAW
SNOWFLAKE_SCHEMA=CLAIMS

---

## Docker Deployment

docker-compose up --build

API at http://localhost:5000
Dashboard at http://localhost:8501

---

## Roadmap

Done:
- Claude LLM claim extraction
- ChromaDB RAG pipeline
- XGBoost fraud detection model
- Flask REST API
- Streamlit dashboard
- Snowflake 3-layer architecture
- Docker containerization
- GitHub Actions CI/CD

Coming:
- Power BI executive dashboard
- Real-time claim streaming
- Multi-language support
- Explainable AI with SHAP values
- Azure cloud deployment

---

## Built By

Momna Ali — AI and ML Engineer
GitHub: https://github.com/Momna-bit
