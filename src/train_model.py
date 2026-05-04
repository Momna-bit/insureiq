import json
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report
import pickle
import os

# Load historical claims
with open("data/historical_claims.json") as f:
    claims = json.load(f)

# Feature engineering
rows = []
for claim in claims:
    d = claim["data"]
    red_flags = d.get("red_flags", "")
    flag_count = len(red_flags.split(",")) if red_flags and red_flags != "none" else 0
    rows.append({
        "claim_amount": float(d.get("claim_amount", 0)),
        "red_flag_count": flag_count,
        "is_vehicle": 1 if d.get("incident_type") == "Vehicle Accident" else 0,
        "is_theft": 1 if d.get("incident_type") == "Theft" else 0,
        "is_fire": 1 if d.get("incident_type") == "Fire Damage" else 0,
        "is_medical": 1 if d.get("incident_type") == "Medical" else 0,
        "is_fraud": 1 if d.get("fraud_label") == "FRAUD" else 0
    })

df = pd.DataFrame(rows)
X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

# SMOTE balancing
X_res, y_res = SMOTE(random_state=42).fit_resample(X, y)
print(f"After SMOTE — Fraud: {sum(y_res==1)}, Legit: {sum(y_res==0)}")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Train XGBoost
model = XGBClassifier(n_estimators=100, max_depth=4, random_state=42, eval_metric="logloss")
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred)
print(f"\n✅ AUC Score: {auc:.4f}")
print(classification_report(y_test, model.predict(X_test)))

# Save model
os.makedirs("models", exist_ok=True)
with open("models/fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("✅ Model saved to models/fraud_model.pkl")
