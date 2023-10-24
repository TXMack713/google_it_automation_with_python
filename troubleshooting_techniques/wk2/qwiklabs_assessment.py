#!/usr/bin/env python3

# Google IT Automation with Python
# Troubleshooting and Debugging Techniques,
# Fix a slow system with Python

import subprocess
import multiprocessing
import os
# from concurrent import futures

# src = "/data/prod/"
# dest = "/data/prod_backup/"
src = "/home/txmack713/Desktop/GitHub/it_automation_python/troubleshooting_techniques/wk2/"
dest = "/home/txmack713/Desktop/GitHub/it_automation_python/troubleshooting_techniques/wk2/copy/"


def copy_files(source):
    subprocess.call(["rsync", "-arq", source, dest])


core_count = multiprocessing.cpu_count()

if __name__ == '__main__':
    # src = "/home/txmack713/Desktop/GitHub/it_automation_python/troubleshooting_techniques/wk2"
    # dest = "/home/txmack713/Desktop/GitHub/it_automation_python/troubleshooting_techniques/wk2/copy"

    directory_list = next(os.walk(src))[1]
    full_paths = [os.path.join(src, directory) for directory in directory_list]
    # for root, dirs, files in os.walk(src):
    #     directories = [os.path.join(src, dir) for dir in dirs]
    with multiprocessing.Pool(processes=core_count) as pool:
        pool.map(copy_files, full_paths)

    pool.join()
    #         directory_list.append(path)

