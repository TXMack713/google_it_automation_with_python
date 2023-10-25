#!/usr/bin/env python3

# Google IT Automation with Python
# Troubleshooting and Debugging Techniques,
# Fix a slow system with Python - Qwiklabs Assessment

import subprocess
import multiprocessing
import os

src = "/data/prod/"
dest = "/data/prod_backup/"

path = os.getcwd()

path_arr = path.split("/")
path_arr.pop()
new_path = "/".join(path_arr)

new_src = new_path + src
new_dest = new_path + dest

if not os.path.exists(new_dest):
   os.mkdir(new_dest)


def copy_files(source):
    print(source)
    subprocess.call(["rsync", "-aq", source, new_dest])


core_count = multiprocessing.cpu_count()

if __name__ == '__main__':
    directories = []
    for root, dirs, files in os.walk(new_src, topdown=False):
        for dir in dirs:
            directories.append(os.path.join(root, dir))
    with multiprocessing.Pool(processes=core_count) as pool:
        pool.map(copy_files, directories)

    pool.join()

