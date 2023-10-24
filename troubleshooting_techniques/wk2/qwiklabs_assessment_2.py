#!/usr/bin/env python3

# Google IT Automation with Python
# Troubleshooting and Debugging Techniques,
# Fix a slow system with Python

import psutil
import subprocess

# Check the current CPU's usage
psutil.cpu_percent()

# Check the disk I/O
psutil.disk_io_counters()

# Check the network I/O bandwidth
psutil.net_io_counters()

# Experimenting with subprocesses

src = "~/Desktop/GitHub/it_automation_python/troubleshooting_techniques/wk2"
dest = "~/Desktop/GitHub/it_automation_python/troubleshooting_techniques/wk2/copy"

subprocess.call(["rsync", "-arq", src, dest])

