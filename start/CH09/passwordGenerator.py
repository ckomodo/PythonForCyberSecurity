#!/usr/bin/env python3
# Script that checks URLs against Google's Safe Browsing API
# https://developers.google.com/safe-browsing/v4
# By CW

#import modules
import hashlib
import requests
import random
import string

#function to check password
def check_haveibeenpwned(sha_prefix):
    pwnd_dict = {}
    #Perform API request
    request_uri = "https://api.pwnedpasswords.com/range/" + sha_prefix
    results = requests.get(request_uri)

    #Confirm if found
    pwned_list = results.text.split("\r\n")
    for pwnd_pass in pwned_list:
        temp_pass = pwnd_pass.split(":")
        pwnd_dict[temp_pass[0]] = temp_pass[1]
    return pwnd_dict

# Generate a random password of length 16
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

password = generate_password(16)
print("The password generated is " + password)
#source: https://www.geeksforgeeks.org/generate-random-strings-for-passwords-in-python/

new_password = password

#Hash the password
encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest()

#Split the hash
sha_prefix = hashed_password[0:5]
#print("The first 5 characters are: ", sha_prefix)

sha_postfix = hashed_password[5:].upper()
#print("The remaining characters after the 5th one are: ", sha_postfix)

#Check the password hash
pwnd_dict = check_haveibeenpwned(sha_prefix)

#Check results 
if sha_postfix in pwnd_dict.keys():
    print("Password compromised {0} times".format(pwnd_dict[sha_postfix]))
else:
    print("Secure password")

