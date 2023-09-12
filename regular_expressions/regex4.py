#!/usr/bin/env python3

# Google IT Automation with Python - Regular Expressions, Splitting and Replacing

import re

# Example of the regex split function in Python
result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(result)

# Another example of the regex split function in Python, this time using parentheses to capture the notation marks as well
result = re.split(r"([.?!])", "One sentenece. Another one? And the last one!")
print(result)

# Example using the regex replace function in Python
result2 = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
print(result2)

result3 = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(result3)

