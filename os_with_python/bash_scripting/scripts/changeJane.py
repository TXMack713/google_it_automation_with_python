#!/usr/bin/env python3

# Google IT Automation with Python - Bash Scripting, Qwiklabs Assessment

import sys
import subprocess
import os
#
# dir = os.getcwd()
# dir_arr = dir.split("/")
# dir_arr.pop()
# new_dir = "/".join(dir_arr) + "/data"

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        print("Original: " + line)
        file = line.strip()
        new_file = file.replace("jane_", "jdoe_")
        print("New: " + new_file)
        result1 = subprocess.run(["mv", file, new_file])
        #print("Printing the returncode and data from running the mv subprocess with Python: " + str(result1.returncode))
        #print(result1)
f.close()
