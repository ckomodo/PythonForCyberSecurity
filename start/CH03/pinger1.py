#!/usr/bin/env python3
# First example of pinging from Python
# By 

import os
#pulls a library

#Assign IP address to a variable
ip_address = "127.0.0.1"

#Build a ping command
ping_cmd = "ping -c 1 -W 2 {0}".format(ip_address)

#Build execute
exit_code = os.system(ping_cmd)

#print out result
print(exit_code)