#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By CW

#prompt for file to analyze
#log_file = input("Which file to analyze?")

#open file
f = open("start/CH07/access.log", "r")

#Read file line by line
while True:
    line = f.readline()
    if not line:
        break
    #check for 404
    if "404" in line:
        print(line.strip())

    #close file
    f.close()