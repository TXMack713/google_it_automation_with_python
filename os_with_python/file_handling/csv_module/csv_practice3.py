#!/usr/bin/env python3

# Google IT Automation with Python - CSV Module - Reading and Writing CSV Files with Dictionaries

import csv

with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]

with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)



