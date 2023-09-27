#!/usr/bin/env python3

# Google IT Automation with Python - Bash Scripting, Pipes and Pipelines

import sys

for line in sys.stdin:
	print(line.strip().capitalize())


