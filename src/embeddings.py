import os
import json
import chromadb
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(os.path.expanduser('~/insureiq/.env'))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Setup ChromaDB locally
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="insurance_claims")

def get_embedding(text: str) -> list:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def index_claim(claim_id: str, claim_data: dict):
    text = f"""
    Claimant: {claim_data.get('claimant_name', '')}
    Incident: {claim_data.get('incident_type', '')}
    Amount: {claim_data.get('claim_amount', '')}
    Description: {claim_data.get('description', '')}
    Red Flags: {', '.join(claim_data.get('red_flags', []))}
    """
    embedding = get_embedding(text)
    collection.add(
        ids=[claim_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[claim_data]
    )
    print(f"✅ Indexed claim {claim_id}")

def find_similar_claims(claim_data: dict, top_k: int = 3) -> list:
    text = f"""
    Claimant: {claim_data.get('claimant_name', '')}
    Incident: {claim_data.get('incident_type', '')}
    Amount: {claim_data.get('claim_amount', '')}
    Description: {claim_data.get('description', '')}
    Red Flags: {', '.join(claim_data.get('red_flags', []))}
    """
    embedding = get_embedding(text)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=min(top_k, collection.count())
    )
    return results

if __name__ == "__main__":
    # Test with a sample claim
    test_claim = {
        "claimant_name": "Sarah Johnson",
        "incident_type": "Vehicle Accident",
        "claim_amount": 15000,
        "incident_date": "2024-03-15",
        "description": "Car totaled in parking lot overnight",
        "red_flags": ["No witnesses", "Third accident this year"]
    }
    index_claim("test-001", test_claim)
    print(f"Total indexed: {collection.count()}")
    print("✅ Embeddings working!")
