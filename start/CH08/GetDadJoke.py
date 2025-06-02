#By Christopher W

import requests
import json

url = "https://icanhazdadjoke.com/"

payload = {}
headers = {
  
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

jokes = response.json()
print(json.dumps(jokes["joke"]))