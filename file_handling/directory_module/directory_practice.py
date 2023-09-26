#!/usr/bin/env python3

#Directory practice using the OS module for directories

import os

path = os.getcwd()

print(path)

dir_arr = path.split("/")
print(dir_arr)

dir = dir_arr.pop()

new_path = "/".join(dir_arr)

os.chdir(new_path)

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))