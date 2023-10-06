#!/usr/bin/env python3

# Google IT Automation with Python - Managing Data and Processes with Python, Obtaining the Output of a System Command

import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print("Printing the result and returncode of data from the run subprocess with the capture output field set to True: " + str(result.returncode))
print(result)
print("Printing the result.stdout result: " + str(result.stdout))

print("Decoding the stdout output: " + str(result.stdout.decode().split()))
print("Printing the result.stderr output: " + str(result.stderr))

result1 = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print("Printing the result and returncode of data from the run subprocess for the remove command for a file that does not exist with the capture output field set to True: " + str(result1.returncode))
print("Printing the result.stderr output: " + str(result1.stderr))

