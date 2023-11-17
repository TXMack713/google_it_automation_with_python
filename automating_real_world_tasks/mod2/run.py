#!/usr/bin/env python3
# Google IT Automation with Python
# Automating Real-World Tasks with Python
# Module 2 - Qwiklabs Assessment: Process Text Files with Python Dictionaries ad Upload to Running Web Service

import os
import requests

review_path = os.getcwd()

for root, directory, files in os.walk(review_path):
    for file in files:
        full_file = os.path.join(root, file)
        print("Full file: " + full_file)
        if os.path.isfile(full_file):
            # new_file = new_path + "/" + file
            try:
                with open(full_file) as review:

            except :
                pass