#!/usr/bin/env python3

# Google IT Automation with Python - Managing Data and Processes, Advanced Subprocess Management

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/advanced_subprocess_mgmt/", my_env["PATH"]])

result = subprocess.run(["advanced_subprocess_mgmt"], env=my_env)

