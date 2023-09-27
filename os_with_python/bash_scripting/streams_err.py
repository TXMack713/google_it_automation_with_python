#!/usr/bin/env python3

# Google IT Automation with Python - Bash Scripting, Redirecting Streams

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")

