import requests
import json

url = "http://127.0.0.1:8000/api/users/register/"
data = {
    "username": "testuser_debug",
    "email": "testdebug@example.com",
    "password": "testpassword123",
    "role": "student"
}

try:
    print(f"Sending POST request to {url}...")
    print(f"Data: {data}")
    response = requests.post(url, json=data)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    
    if response.status_code == 201:
        print("SUCCESS: User created via API.")
    else:
        print("FAILURE: API returned error.")
        
except Exception as e:
    print(f"EXCEPTION: {e}")
