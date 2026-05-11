# 🛡️ InsureIQ — AI Claims Intelligence Platform

> An end-to-end GenAI system that reads insurance claims, detects fraud using RAG-enhanced AI, scores risk with XGBoost, and delivers real-time decisions through a custom executive dashboard built on Snowflake.

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Claude AI](https://img.shields.io/badge/Claude_AI-Anthropic-FF6B35?style=flat)](https://anthropic.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-AUC_1.0-green?style=flat)](https://xgboost.readthedocs.io)
[![Snowflake](https://img.shields.io/badge/Snowflake-Data_Platform-29B5E8?style=flat&logo=snowflake&logoColor=white)](https://snowflake.com)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat&logo=docker&logoColor=white)](https://docker.com)
[![CI/CD](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=githubactions&logoColor=white)](https://github.com/features/actions)

---

## What Is InsureIQ?

Insurance fraud costs the global industry **$80 billion every year**. Traditional detection relies on manual claim review — slow, inconsistent, and impossible to scale.

InsureIQ solves this with a four-layer AI pipeline:

- **Claude AI (LLM)** reads raw claim documents and extracts structured data with no templates required
- **RAG Pipeline (ChromaDB)** cross-references every claim against 500+ indexed historical cases
- **XGBoost ML Model** scores fraud probability in real time — achieving AUC 1.0
- **Custom Executive Dashboard** built from scratch in HTML/CSS/JS, connected live to Snowflake MART

The result: a claim goes in, a risk-scored decision comes out. In seconds.

---

## 🌐 Live Links

| | |
|---|---|
| 🛡️ **Portfolio** | [momna-bit.github.io/insureiq](https://momna-bit.github.io/insureiq) |
| 📊 **Executive Dashboard** | [momna-bit.github.io/insureiq/dashboard.html](https://momna-bit.github.io/insureiq/dashboard.html) |
| 💻 **Source Code** | [github.com/Momna-bit/insureiq](https://github.com/Momna-bit/insureiq) |

---

## 🎬 Quick Start

```bash
git clone https://github.com/Momna-bit/insureiq.git
cd insureiq
pip install -r requirements.txt
```

Set up your `.env` file:

```env
ANTHROPIC_API_KEY=your_claude_api_key
OPENAI_API_KEY=your_openai_api_key
SNOWFLAKE_ACCOUNT=your_account_id
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=INSUREIQ_RAW
SNOWFLAKE_SCHEMA=CLAIMS
```

Train and launch:

```bash
python src/train_model.py
python src/generate_historical.py
python src/index_historical.py
python src/api.py
streamlit run src/dashboard.py
```

---

## 🏗️ Architecture

```
CLAIM INPUT
      │
      ▼
Claude AI ──► Extracts structured JSON from raw text
      │
      ▼
ChromaDB RAG ──► Finds top 3 similar historical claims
      │
      ▼
XGBoost ──► Scores fraud probability → LOW / MEDIUM / HIGH
      │
      ▼
Snowflake: RAW → TRANSFORM → MART
      │
      ├──► Streamlit Dashboard
      ├──► Custom HTML Executive Dashboard
      └──► Flask REST API
```

---

## 📁 Project Structure

```
insureiq/
├── src/
│   ├── extract.py              # Claude LLM claim extraction
│   ├── embeddings.py           # OpenAI embeddings + ChromaDB indexing
│   ├── rag.py                  # RAG pipeline + similarity search
│   ├── generate_historical.py  # 500+ synthetic claims generator
│   ├── index_historical.py     # Index claims into ChromaDB
│   ├── train_model.py          # XGBoost + SMOTE model training
│   ├── api.py                  # Flask REST API (3 endpoints)
│   └── dashboard.py            # Streamlit interactive dashboard
├── docs/
│   ├── index.html              # Live portfolio (GitHub Pages)
│   └── dashboard.html          # Custom executive dashboard
├── models/
│   └── fraud_model.pkl         # Trained XGBoost model
├── data/
│   └── historical_claims.json  # 500+ historical claims dataset
├── .github/workflows/
│   └── ci.yml                  # GitHub Actions CI/CD
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🔌 API Reference

Base URL: `http://localhost:5000`

```bash
GET  /health    # System health check
POST /analyze   # Extract claim + return fraud score
POST /risk      # Full RAG analysis + recommendation
```

---

## 📊 Performance

| Metric | Result |
|--------|--------|
| XGBoost AUC Score | **1.0** |
| Fraud Detection Accuracy | **99.7%** |
| Historical Claims Indexed | **500+** |
| REST API Endpoints | **3** |
| End-to-End Test Pass Rate | **100%** |
| Snowflake Data Layers | **3** |

---

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

---

## ✅ Project Status

- [x] Claude LLM claim extraction
- [x] ChromaDB RAG pipeline with 500+ indexed claims
- [x] XGBoost fraud detection model (AUC 1.0)
- [x] Flask REST API with 3 endpoints
- [x] Streamlit interactive dashboard
- [x] Snowflake 3-layer architecture
- [x] Docker containerization
- [x] GitHub Actions CI/CD pipeline
- [x] Custom HTML Executive Dashboard
- [x] Live portfolio on GitHub Pages

---

## 👩‍💻 Built By

**Momna Ali** — AI and Data Engineer

[![GitHub](https://img.shields.io/badge/GitHub-Momna--bit-181717?style=flat&logo=github&logoColor=white)](https://github.com/Momna-bit)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live-00D4FF?style=flat)](https://momna-bit.github.io/insureiq)
[![Dashboard](https://img.shields.io/badge/Dashboard-Live-10B981?style=flat)](https://momna-bit.github.io/insureiq/dashboard.html)

---

*Built in 4 weeks. Tested end to end. Production-ready.*
