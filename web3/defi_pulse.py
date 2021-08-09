import requests
import json
import pandas as pd

# input your token here
api_key = "73e72770e1757bca83127c49ed61bb42fc04f42b0f4e6b310131aa1f2b0e"

url = (
    "https://data-api.defipulse.com/api/v1/defipulse/api/GetHistory?api-key=" + api_key
)
response = requests.get(url)
result = json.loads(response.text)


def get_pretty_json_string(value):
    return json.dumps(value, indent=4, sort_keys=True, ensure_ascii=False)


## print(get_pretty_json_string(result))
## print(result)

print(pd.json_normalize(result))
print(result[0]["tvlUSD"])
