# scanner/burp_client.py
import requests
import json

BURP_API_URL = 'https://your-burp-suite-url:8080'
BURP_API_KEY = 'your_api_key'

def trigger_burp_scan(target_url):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {BURP_API_KEY}'
    }
    data = {
        'url': target_url,
        'application_id': 'your_application_id',
    }
    response = requests.post(f'{BURP_API_URL}/scan', headers=headers, data=json.dumps(data))
    return response.json()

def get_burp_scan_results(scan_id):
    headers = {
        'Authorization': f'Bearer {BURP_API_KEY}'
    }
    response = requests.get(f'{BURP_API_URL}/scan/{scan_id}/results', headers=headers)
    return response.json()
