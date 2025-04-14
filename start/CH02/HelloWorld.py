#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created 
print ("Hello there and Welcome")
user_name = input("Please enter your name ")
print("Hello {0}, " .format(user_name), "today will be a good day")
age = float(input("What year were you born?"))
next_age = 2027 - age
print ("In two years you will be {0}" .format(next_age))