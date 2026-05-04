import os
import sys
import json
import pickle
import re
import numpy as np
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv(os.path.expanduser('~/insureiq/.env'))
sys.path.append(os.path.expanduser('~/insureiq/src'))

from extract import extract_claim
from rag import analyze_claim_with_rag

app = Flask(__name__)

# Load model
with open("models/fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

def get_fraud_score(extracted: dict) -> dict:
    red_flags = extracted.get("red_flags", [])
    if isinstance(red_flags, list):
        flag_count = len(red_flags)
    else:
        flag_count = len(str(red_flags).split(",")) if red_flags and red_flags != "none" else 0

    incident = extracted.get("incident_type", "")
    features = np.array([[
        float(extracted.get("claim_amount", 0)),
        flag_count,
        1 if incident == "Vehicle Accident" else 0,
        1 if incident == "Theft" else 0,
        1 if incident == "Fire Damage" else 0,
        1 if incident == "Medical" else 0,
    ]])
    score = model.predict_proba(features)[0][1]
    label = "HIGH" if score > 0.7 else "MEDIUM" if score > 0.4 else "LOW"
    return {"fraud_score": round(float(score), 4), "fraud_label": label}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model": "InsureIQ v1.0"})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    claim_text = data.get("claim_text", "")
    extracted = extract_claim(claim_text)
    fraud = get_fraud_score(extracted)
    return jsonify({
        "extracted": extracted,
        "fraud_score": fraud["fraud_score"],
        "fraud_label": fraud["fraud_label"]
    })

@app.route("/risk", methods=["POST"])
def risk():
    data = request.json
    claim_text = data.get("claim_text", "")
    result = analyze_claim_with_rag(claim_text)
    fraud = get_fraud_score(result["extracted_claim"])
    result["fraud_score"] = fraud["fraud_score"]
    result["fraud_label"] = fraud["fraud_label"]
    return jsonify(result)

if __name__ == "__main__":
    print("✅ InsureIQ API running on http://localhost:5000")
    app.run(debug=True, port=5000)
