import json
import random
import uuid

incident_types = ["Vehicle Accident", "Fire Damage", "Theft", "Water Damage", "Medical", "Property Damage"]
names = ["John Smith", "Emma Wilson", "Ahmed Khan", "Lisa Chen", "Carlos Rivera", "Sara Patel", "Mike Johnson", "Fatima Ali"]
descriptions = [
    "Vehicle was damaged in a parking lot with no witnesses present.",
    "Fire broke out in the kitchen causing extensive damage.",
    "Laptop and jewelry stolen from home while on vacation.",
    "Pipe burst overnight causing flooding in basement.",
    "Injured in slip and fall accident at workplace.",
    "Storm caused roof damage and broken windows.",
    "Car rear-ended at traffic light by unknown driver.",
    "Bicycle stolen from outside gym despite being locked.",
]
red_flags_pool = [
    "No witnesses", "Third claim this year", "Recently increased coverage",
    "Incident occurred late at night", "No police report filed",
    "Claimant has prior fraud history", "Amount near policy limit",
    "Inconsistent timeline", "No photos provided", "Cash payment requested"
]

claims = []
for i in range(500):
    has_fraud = random.random() < 0.3
    num_flags = random.randint(2, 4) if has_fraud else random.randint(0, 1)
    claim = {
        "claimant_name": random.choice(names),
        "incident_type": random.choice(incident_types),
        "claim_amount": round(random.uniform(1000, 50000), 2),
        "incident_date": f"202{random.randint(2,4)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
        "description": random.choice(descriptions),
        "red_flags": ", ".join(random.sample(red_flags_pool, num_flags)) if num_flags > 0 else "none",
        "fraud_label": "FRAUD" if has_fraud else "LEGITIMATE"
    }
    claims.append({"id": str(uuid.uuid4()), "data": claim})

with open("data/historical_claims.json", "w") as f:
    json.dump(claims, f, indent=2)

print(f"✅ Generated {len(claims)} historical claims!")
