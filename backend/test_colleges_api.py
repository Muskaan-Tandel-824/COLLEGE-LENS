import requests
import json

base_url = "http://127.0.0.1:8000/api/colleges/"

try:
    print(f"GET {base_url}")
    response = requests.get(base_url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Success! Found {len(data)} colleges.")
        print(json.dumps(data[0], indent=2))
    else:
        print("Failed to fetch colleges.")
        print(response.text)

except Exception as e:
    print(f"Error: {e}")
