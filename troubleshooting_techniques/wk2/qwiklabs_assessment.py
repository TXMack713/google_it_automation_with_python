#!/usr/bin/env python3

# Google IT Automation with Python
# Troubleshooting and Debugging Techniques,
# Fix a slow system with Python

import subprocess
src = "/data/prod/"
dest = "/data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])
