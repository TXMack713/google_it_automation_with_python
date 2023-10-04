#!/usr/bin/env python3

# Google IT Automation with Python - Git and GitHub, Applying Changes

import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: usage: {}".format(usage))
    return usage < percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
else:
    print("Everythink ok")

