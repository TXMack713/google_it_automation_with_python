#!/usr/bin/env python3

# Google IT Automation with Python - CSV Module - Reading CSV Files

import csv

# f = open("csv_file.txt")
# csv_f = csv.reader(f)
#
# for row in csv_f:
#     name, phone, role = row
#     print("Name: {}, Phone: {}, Role: {}".format(name,phone,role))
#
# f.close()

with open("csv_file.txt") as f:
    csv_f = csv.reader(f)

    for row in csv_f:
        name, phone, role = row
        print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

