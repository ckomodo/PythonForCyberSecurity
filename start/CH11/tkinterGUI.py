#!/usr/bin/env python3
# Script that checks URLs against Google's Safe Browsing API
# https://developers.google.com/safe-browsing/v4
# By CW

#import modules
import hashlib
import requests
import random
import string
import tkinter

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



def print_password():
    password = generate_password(16)
    new_password = password
    #print("The password generated is " + password)
    return password
    
#source: https://www.geeksforgeeks.org/generate-random-strings-for-passwords-in-python/

print("The password generated is " + print_password())

#print("your password is " + print_password())

#Hash the password
def final_password():
    encoded_password = print_password().encode()
    digest_password = hashlib.sha1(encoded_password)
    hashed_password = digest_password.hexdigest()
    return hashed_password

#Split the hash
#sha_prefix = hashed_password[0:5]
sha_prefix = final_password()[0:5]
#print("The first 5 characters are: ", sha_prefix)

sha_postfix = final_password()[5:].upper()

#sha_postfix = hashed_password[5:].upper()
#print("The remaining characters after the 5th one are: ", sha_postfix)

#Check the password hash
pwnd_dict = check_haveibeenpwned(sha_prefix)

#Check results 
if sha_postfix in pwnd_dict.keys():
    print("Password compromised {0} times".format(pwnd_dict[sha_postfix]))
else:
   print("This password is Secure")


window = tkinter.Tk()
window.geometry('420x420')
window.title("Password Generator")

icon = tkinter.PhotoImage(file='password.png')
window.iconphoto(True, icon)


button = tkinter.Button(window, text = "Generate Password")
button.pack()

window.config(background="#24d9dc")
window.mainloop()
