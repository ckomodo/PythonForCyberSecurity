#!/usr/bin/env python3
# Example brute-force attacker
#By Ed Goad
# date: 2/5/2021

# NOTE: this example is limited to numbers. 
# There are no letters or symbols in this example
# Suggested to start by debugging to show how 
# brute force walks through all available options 

from passlib.hash import sha512_crypt

def test_password(hashed_password, 
    salt, plaintext_password):
    # Using the provided algorithm/salt and
    # plaintext password, create a hash
    crypted_password = sha512_crypt.using(rounds=5000).hash(
        plaintext_password, salt=salt)
    # Compare hashed_password with the just created hash
    if hashed_password == crypted_password:
        return True
    return False

hashed_password = "$6$G.DTW7g9s5U7KYf5$QFcHx0/J88HV/Q0ab653"
hashed_password += "gfYQ1KyNGx5HRhDQYyai2ZUy7Aw4tyfJ6/kI6kl"
hashed_password += "lfXl0DyS.LuaUJvqnlIn2fVM5F0"
salt = "G.DTW7g9s5U7KYf5"

for password in range(100000):
    result = test_password(hashed_password, \
        salt, str(password))
    if result:
        print("Match found: {0}".format(password))
        break
