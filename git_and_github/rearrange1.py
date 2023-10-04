#!/usr/bin/env python3

# Google IT Automation with Python - Git and GitHub, Diffing Files

import re

def rearrange_name(name):
	result = re.search(r"^([\w .]*), ([\w .]*)$", name)
	if result == None:
		return result
	return "{} {}".format(result[2], result[1])


