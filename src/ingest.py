import os
import json
import uuid
import snowflake.connector
from dotenv import load_dotenv

load_dotenv(os.path.expanduser('~/insureiq/.env'))

def get_connection():
    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse="COMPUTE_WH",
        autocommit=True
    )

def store_raw_claim(raw_json: dict, source_file: str = "test.txt"):
    conn = get_connection()
    cursor = conn.cursor()
    claim_id = str(uuid.uuid4())
    json_str = json.dumps(raw_json).replace("'", "\\'")
    sql = f"""
        INSERT INTO INSUREIQ_RAW.CLAIMS.RAW_CLAIMS (claim_id, raw_json, source_file)
        SELECT '{claim_id}', PARSE_JSON('{json_str}'), '{source_file}'
    """
    cursor.execute(sql)
    print(f"Rows affected: {cursor.rowcount}")
    cursor.close()
    conn.close()
    print(f"✅ Stored claim {claim_id} in Snowflake RAW!")
    return claim_id

if __name__ == "__main__":
    from extract import extract_claim
    test_claim = """
    Claimant: Sarah Johnson
    Date of Incident: 2024-03-15
    Type: Vehicle Accident
    Amount Claimed: $15,000
    Description: My car was totaled in a parking lot overnight.
    No witnesses. Third accident this year.
    """
    extracted = extract_claim(test_claim)
    store_raw_claim(extracted, "test_claim.txt")
