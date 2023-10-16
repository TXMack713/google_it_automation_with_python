#!/usr/bin/env python3

# Google IT Automation with Python - Troubleshooting and Debugging Techniques, Qwiklabs Assessment Week 1

import random


def greeting():
    name = input("Hello!, What's your name?")
    number = random.randint(1,101)
    print("hello " + name + ", your random number is " + str(number))


greeting()
