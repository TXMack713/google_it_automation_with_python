#!/usr/bin/env python3


# Google IT Automation With Python
# Troubleshooting and Debugging Techniques
# Debugging and Solving Software Problems - Final Assessment

import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    # Convert the given inputs from the user to integers to be used with the datetime function
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines


'''
Here are few hints to fix this issue:

Download the file only once from the URL.
Pre-process it so that the same calculation doesn't need to be done over and over again. This can be done in two ways. You can choose any one of them:
1. To create a dictionary with the start dates and then use the data in the dictionary instead of the complicated calculation.
2. To sort the data by start_date and then go date by date.
'''


def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    start_information = {}
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        start_information[row_date] = []
        start_information[row_date].append("{} {}".format(row[0], row[1]))

    # for row in reader:
    #     row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
    #     start_information[row_date].append("{} {}".format(row[0], row[1]))

    for key in start_information.keys():
        # If this date is smaller than the one we're looking for,
        # we skip this row
        if key < start_date:
            continue

        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.
        if key < min_date:
            min_date = key
            min_date_employees = []

        # If this date is the same as the current minimum,
        # we add the employee in this row to the list of
        # employees at the minimal date.
        if key == min_date:
            min_date_employees.append(start_information[key])

    return min_date, min_date_employees


def list_newer(start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()
