#!/usr/bin/env python3

# Practice using the OS module in Python
import os
import datetime

os.path.exists("draft.txt")
print("Does draft.txt exist? -- " + str(os.path.exists("draft.txt")))

os.rename("draft.txt", "first_draft.txt")
print("The file draft.txt was renamed to first_draft.txt. \nDoes draft.txt still exist -- " + str(os.path.exists("draft.txt")))

size = os.path.getsize("first_draft.txt")
print("The size of first_draft.txt is -- " + str(size))

timestamp = os.path.getmtime("first_draft.txt")
time_created = datetime.datetime.fromtimestamp(timestamp)

print("The file first_draft.txt was created at " + str(time_created))




