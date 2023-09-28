#!/usr/bin/env python3

# Google IT Automation with Python - Interacting with the OS with Python, Log Analysis Using Regular Expressions

import os
import re
import subprocess
import sys
import operator


error_dict = {}
filename = sys.argv[1]

with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        regex = r"ticky: ([\w\s]*) \("
        result = re.search(regex, line)
        if result is not None:
            print(result)
        # item = result.split("ticky: ")
        # result1 = result[1].split("(")
        # error_dict[result] = error_dict.get(result, 0) + 1
f.close()

# print(error_dict)
