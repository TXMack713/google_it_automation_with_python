#!/usr/bin/env python3

# Google IT Automation with Python - Managing Data and Processes, Qwiklabs Assessment

import sys
import re
import os

def error_search(log_file):
    error = input("What is the error?: ")
    returned_errors = []

    with open(log_file, mode='r', encoding="UTF-8") as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(" "))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)

        file.close()
    return returned_errors

def file_output(returned_errors):
    dir = os.getcwd()
    dir_arr = dir.split("/")
    if dir_arr[len(dir_arr) - 1] == "scripts":
        dir_arr.pop()
    new_dir = "/".join(dir_arr) + "/data/errors_found.log"
    with open(new_dir, "w") as file:
        for error in returned_errors:
            file.write(error)

    file.close()

if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)

