#!/usr/bin/env python3

# Google IT Automation with Python - Unit Tests

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])

