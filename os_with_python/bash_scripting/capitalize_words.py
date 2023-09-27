#!/usr/bin/env python3

# Google IT Automation with Python - Bash Scripting, Choosing Between Bash and Python

import sys

for line in sys.stdin:
    words = line.strip().split()
    print(" ".join([word.capitalize() for word in words]))

