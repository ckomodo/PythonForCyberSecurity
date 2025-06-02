#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By 

import requests
import configparser

def get_api_key(key_name):
    #create configparser object
    config = configparser.ConfigParser()
    config.read("/home/justincase/secrets.ini")
    #select and find api key
    api_key = config["APIkeys"][key_name]
    return api_key
 

url = "https://api.github.com/user/repos"

token = get_api_key('GitHub')

payload = {}
headers = {
  'Authorization': 'token' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
