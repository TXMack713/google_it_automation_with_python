#!/usr/bin/env python3

# Google IT Automation with Python - Managing Data and Processes, Running System Commands in Python

import subprocess

result1 = subprocess.run(["date"])
print("Printing the returncode and data from running the date subprocess with Python: " + str(result1.returncode))
print(result1)

result2 = subprocess.run(["sleep", "2"])
print("Printing the returncode and data from running the sleep subprocess with Python: " + str(result2.returncode))
print(result2)

result3 = subprocess.run(["ls", "this_file_does_not_exist"])
print("Printing the returncode and data from running the ls process on a file that does not exist: " + str(result3.returncode))
print(result3)

