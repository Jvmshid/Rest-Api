import requests
api_url = "http://127.0.0.1:8000/api/v1/user/2"
response = requests.get(api_url)
r = response.json()
print(r)