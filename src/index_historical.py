import json
import os
import sys
sys.path.append(os.path.expanduser('~/insureiq/src'))
from embeddings import index_claim, collection

with open("data/historical_claims.json") as f:
    claims = json.load(f)

print(f"Indexing {len(claims)} claims into ChromaDB...")

for i, claim in enumerate(claims):
    index_claim(claim["id"], claim["data"])
    if (i + 1) % 50 == 0:
        print(f"Progress: {i+1}/500 indexed...")

print(f"\n✅ Done! Total in ChromaDB: {collection.count()}")
