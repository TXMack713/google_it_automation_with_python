#!/usr/bin/env python3

# Google IT Automation with Python - Git and GitHub, The Basic Git Workflow

import os
import sys


def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)


main()
