#!/usr/bin/env python3
# Sample script that writes to a file
# By 04/23/2025

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

#Open File to write
f = open(dir_path + "/txtfile.txt", "w")



#Write to file

f.write("Hey friends\n")
f.write("How are you\n")
f.write("Some more text\n")



#Close the file
f.close()