import os
import json
import sys
sys.path.append(os.path.expanduser('~/insureiq/src'))
from embeddings import find_similar_claims, collection
from extract import extract_claim
import anthropic
from dotenv import load_dotenv

load_dotenv(os.path.expanduser('~/insureiq/.env'))

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analyze_claim_with_rag(claim_text: str) -> dict:
    # Step 1 — Extract structured data from raw claim
    print("🔍 Extracting claim data...")
    extracted = extract_claim(claim_text)

    # Step 2 — Find similar historical claims
    print("🔎 Searching similar claims...")
    similar = find_similar_claims(extracted, top_k=3)

    similar_context = ""
    if similar and similar["documents"][0]:
        for i, doc in enumerate(similar["documents"][0]):
            similar_context += f"\nSimilar Claim {i+1}:\n{doc}\n"

    # Step 3 — Claude analyzes with RAG context
    print("🧠 Claude analyzing with RAG context...")
    prompt = f"""You are an insurance fraud analyst.

A new claim has been submitted:
{json.dumps(extracted, indent=2)}

Here are the 3 most similar historical claims from our database:
{similar_context}

Based on the new claim AND the historical patterns, provide:
1. Fraud risk assessment (LOW / MEDIUM / HIGH)
2. Key red flags identified
3. Recommendation (APPROVE / INVESTIGATE / REJECT)
4. Brief reasoning in 2-3 sentences

Return ONLY valid JSON with keys: risk_level, red_flags, recommendation, reasoning"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    import re
    raw = re.sub(r'```json|```', '', response.content[0].text).strip()
    analysis = json.loads(raw)

    return {
        "extracted_claim": extracted,
        "similar_claims_found": len(similar["documents"][0]),
        "rag_analysis": analysis
    }

if __name__ == "__main__":
    test_claim = """
    Claimant: Ahmed Hassan
    Date of Incident: 2024-11-20
    Type: Vehicle Accident
    Amount Claimed: $28,000
    Description: Car was stolen from outside my house at night.
    No witnesses. This is my second claim this year.
    No police report filed yet.
    """
    result = analyze_claim_with_rag(test_claim)
    print("\n" + "="*50)
    print("RAG ANALYSIS RESULT:")
    print("="*50)
    print(json.dumps(result, indent=2))
