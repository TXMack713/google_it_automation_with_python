#!/usr/bin/env python3

# Google IT Automation with Python - Testing, Practice Testing

import re

my_txt = "An investment in knowledge pays the best interest."
# my_txt = "The best preparation for tomorrow is doing your best today."
def LetterCompiler(txt):
    result = re.findall(r"([a-c]).", txt)
    if result is None:
        empty = []
        return empty
    else:
        return result

print(LetterCompiler(my_txt))
# print(LetterCompiler("ox"))
