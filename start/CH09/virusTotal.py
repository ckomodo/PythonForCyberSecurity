#API Key: 7309a9d813315245507949a0793adeabe61c766701a0dbe1ddc1fc5faf0b8dc1

import requests

url = 'https://www.virustotal.com/vtapi/v2/file/report'

params = {'apikey': '<apikey>', 'resource': '<resource>'}

response = requests.get(url, params=params)

print(response.json())