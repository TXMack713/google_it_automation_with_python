#!/usr/bin/env python3

# Google IT Automation with Python - Testing, Jupyter Practice Lab 3

import random

participants = ['Jack', 'Jill', 'Larry', 'Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except KeyError:
        print("The name 'Larry' is not available in the dictionary keys.")
        return None

print(Guess(participants))
