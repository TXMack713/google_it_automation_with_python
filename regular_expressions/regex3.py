#!/usr/bin/env python3

# Google IT Automation with Python - Regular Expressions, Extracting a PID Using Regexes

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

result = re.search(regex, "99 elements in a [cage]")
print(result[1])

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return "No log found"
    else:
        return result[1]

print(extract_pid(log))