#!/usr/bin/env python3
# Script that tells us how many people there are in space
#By 

# paste code here

import requests
import json

url = "http://api.open-notify.org/astros.json"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
#convert json t python object
astronauts = response.json()

print("**********************************************")
print(astronauts)
print("#############################################")

print(json.dumps(astronauts, indent=2))

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#print specific data
print("There are {0} people in space now".format(astronauts["number"]))
print("The first astronaut is {0}, aboard the {1}".format(astronauts \
    ["people"][1]["name"], astronauts["people"][1]["craft"]))

#Loop through all people
print("Full list of people in space")
for person in astronauts["people"]:
    print("{0} is aboard the {1}".format(person["name"], person["craft"]))
