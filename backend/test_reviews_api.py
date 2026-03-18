import requests
import json

# 1. Login to get token (or just use basic auth if configured, but we likely need a real user context)
# For this test, verifying the endpoint exists and handles unauth request is a good start, 
# then we can try to post if we can easily authenticate.

base_url = "http://127.0.0.1:8000/api/reviews/"

# Test GET (List)
try:
    print(f"GET {base_url}")
    response = requests.get(base_url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! Reviews list accessible.")
        print(response.json())
    else:
        print("Failed to fetch reviews.")

except Exception as e:
    print(f"Error: {e}")

# TODO: For full test we need to log in first.
# This simple test just checks if the endpoint is up.
