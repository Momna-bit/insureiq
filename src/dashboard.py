import streamlit as st
import requests
import json

st.set_page_config(page_title="InsureIQ", page_icon="🛡️", layout="wide")

st.title("🛡️ InsureIQ — AI Claims Intelligence Platform")
st.markdown("*Powered by Claude AI + XGBoost + RAG*")

st.divider()

claim_text = st.text_area(
    "📄 Paste Insurance Claim Text",
    height=200,
    placeholder="Claimant: John Smith\nDate: 2024-03-15\nType: Vehicle Accident\nAmount: $15,000\nDescription: Car damaged in parking lot. No witnesses..."
)

col1, col2 = st.columns(2)

with col1:
    if st.button("⚡ Quick Analyze", use_container_width=True):
        if claim_text:
            with st.spinner("Claude is reading the claim..."):
                res = requests.post(
                    "http://localhost:5000/analyze",
                    json={"claim_text": claim_text}
                )
                data = res.json()

            st.subheader("📊 Extraction Results")
            extracted = data["extracted"]
            st.metric("Claimant", extracted.get("claimant_name", "N/A"))
            st.metric("Incident Type", extracted.get("incident_type", "N/A"))
            st.metric("Claim Amount", f"${extracted.get('claim_amount', 0):,.0f}")

            score = data["fraud_score"]
            label = data["fraud_label"]
            color = "🔴" if label == "HIGH" else "🟡" if label == "MEDIUM" else "🟢"
            st.subheader("🎯 Fraud Score")
            st.metric(f"{color} Risk Level", label)
            st.progress(score)
            st.caption(f"Fraud probability: {score*100:.1f}%")

            if extracted.get("red_flags"):
                st.subheader("🚩 Red Flags")
                for flag in extracted["red_flags"]:
                    st.error(f"⚠️ {flag}")

with col2:
    if st.button("🧠 Deep RAG Analysis", use_container_width=True):
        if claim_text:
            with st.spinner("Searching 500 historical claims + Claude analyzing..."):
                res = requests.post(
                    "http://localhost:5000/risk",
                    json={"claim_text": claim_text}
                )
                data = res.json()

            rag = data.get("rag_analysis", {})
            score = data.get("fraud_score", 0)
            label = data.get("fraud_label", "N/A")
            color = "🔴" if label == "HIGH" else "🟡" if label == "MEDIUM" else "🟢"

            st.subheader("🔍 RAG Analysis")
            st.metric(f"{color} Risk Level", label)
            st.metric("Similar Claims Found", data.get("similar_claims_found", 0))
            st.progress(score)

            st.subheader("📋 Recommendation")
            rec = rag.get("recommendation", "N/A")
            if rec == "REJECT":
                st.error(f"❌ {rec}")
            elif rec == "INVESTIGATE":
                st.warning(f"🔎 {rec}")
            else:
                st.success(f"✅ {rec}")

            st.subheader("💡 Reasoning")
            st.info(rag.get("reasoning", "N/A"))

            if rag.get("red_flags"):
                st.subheader("🚩 Red Flags")
                for flag in rag["red_flags"]:
                    st.error(f"⚠️ {flag}")
