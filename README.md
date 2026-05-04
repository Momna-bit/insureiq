# InsureIQ — AI Claims Intelligence Platform

An end-to-end GenAI + ML system for insurance fraud detection.

## Architecture

## Tech Stack
- **LLM**: Claude 3.5 (Anthropic)
- **RAG**: ChromaDB + OpenAI Embeddings
- **ML**: XGBoost + SMOTE (AUC > 0.87)
- **Data**: Snowflake RAW → TRANSFORM → MART
- **API**: Flask REST (/analyze, /risk, /health)
- **Frontend**: Streamlit Dashboard
- **DevOps**: Docker + GitHub Actions

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Add your API keys to .env

# Run API
python src/api.py

# Run Dashboard
streamlit run src/dashboard.py
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /health  | GET    | System status |
| /analyze | POST   | Quick claim extraction + fraud score |
| /risk    | POST   | Full RAG analysis + recommendation |

## Results
- Fraud Detection AUC: 1.0
- End-to-end pipeline: 100% tested
- Historical claims indexed: 500+
