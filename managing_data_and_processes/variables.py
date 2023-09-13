#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", "Variable not found"))
print("SHELL: " + os.environ.get("SHELL", "Variable not found"))
print("FRUIT: " + os.environ.get("FRUIT", "Variable not found"))
print("PYTHON: " + os.environ.get("PYTHON3", "Variable not found"))


