#!/usr/bin/env python3

# Google IT Automation with Python - Regular Expressions, More on Repetition Qualifiers

import re

# Examples using the search function for patterns of a certain length
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# Examples using the findall function for patterns of a certain length
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really like strawberries"))
