#!/usr/bin/env python3

# Google IT Automation with Python - Git and GitHub, The Basic Git Workflow

import os

def check_reboot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exist("/run/reboot-required")


def main():
	pass

main()

