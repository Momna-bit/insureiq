import os
import json
import re
import anthropic
from dotenv import load_dotenv

load_dotenv(os.path.expanduser('~/insureiq/.env'))

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extract_claim(claim_text: str) -> dict:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Extract the following fields from this insurance claim and return ONLY valid JSON with no markdown, no code blocks, no extra text:
- claimant_name
- incident_type
- claim_amount (number only)
- incident_date (YYYY-MM-DD)
- description
- red_flags (list of suspicious elements, empty list if none)

Claim text:
{claim_text}"""
            }
        ]
    )
    raw = message.content[0].text
    # Strip markdown code blocks if present
    raw = re.sub(r'```json|```', '', raw).strip()
    return json.loads(raw)

if __name__ == "__main__":
    test_claim = """
    Claimant: Sarah Johnson
    Date of Incident: 2024-03-15
    Type: Vehicle Accident
    Amount Claimed: $15,000
    Description: My car was totaled in a parking lot overnight.
    No witnesses. Third accident this year.
    """
    result = extract_claim(test_claim)
    print(json.dumps(result, indent=2))
