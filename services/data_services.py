import requests
import json

def fetch_data_from_api(api_url, api_key):
    headers = {'Authorization': 'Bearer ' + api_key}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None
