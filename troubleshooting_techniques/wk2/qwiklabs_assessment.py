#!/usr/bin/env python3

# Google IT Automation with Python
# Troubleshooting and Debugging Techniques,
# Fix a slow system with Python - Qwiklabs Assessment

import subprocess
import multiprocessing
import os

src = "/data/prod/"
dest = "/data/prod_backup/"

if not os.path.exists(dest):
    os.mkdir(dest)


def copy_files(source):
    subprocess.call(["rsync", "-arq", source, dest])


core_count = multiprocessing.cpu_count()

if __name__ == '__main__':
    directories = []
    for root, dirs, files in os.walk(src):
        for file in files:
            directories.append(os.path.join(root, file))
    with multiprocessing.Pool(processes=core_count) as pool:
        pool.map(copy_files, directories)

    pool.join()

