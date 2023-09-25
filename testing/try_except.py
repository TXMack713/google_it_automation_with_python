#!/usr/bin/env python3

# Google IT Automation with Python - Testing, The Try-Except Construct

import os
import sys
import re

filename = sys.argv[1]
def character_frequency(filename):
    """Counts the frequency of each character in the given file."""
    # First try to open the file
    try:
        f = open(filename, "rb")
    except OSError:
        print("Error: couldn't open the file: " + filename)
        return None

    # Now process the file
    characters = {}
    for line in f:
        """regex = r"(\w+)"
        result = re.search(regex, line.decode('utf-8'))"""
        for char in line:
            characters[chr(char)] = characters.get(chr(char),0) + 1
    f.close()

    return characters

answer = character_frequency(filename)

for char, value in answer.items():
    print(str(char) + " : " + str(value))
