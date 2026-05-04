import os
key = input('Paste new API key: ')
content = 'ANTHROPIC_API_KEY=' + key.strip() + '\n'
content += 'SNOWFLAKE_ACCOUNT=vofuxrl-mz31151.snowflakecomputing.com\n'
content += 'SNOWFLAKE_USER=MOMNAALI345\n'
content += 'SNOWFLAKE_PASSWORD=cibrer-tymzuq=rucfa6\n'
content += 'SNOWFLAKE_WAREHOUSE=COMPUTE_WH\n'
content += 'SNOWFLAKE_DATABASE=INSUREIQ_RAW\n'
content += 'SNOWFLAKE_SCHEMA=CLAIMS\n'
with open(os.path.expanduser('~/insureiq/.env'), 'w') as f:
    f.write(content)
print('Done! Key saved cleanly.')
