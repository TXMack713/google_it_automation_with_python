#!/usr/bin/env python3
import shutil
# import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100
    print("Free disk space available: " + str(int(free)) + "%")
    return free > 20


if not check_disk_usage("/"):
    print("ERROR!")
else:
    print("Everything is OK!")

