#!/usr/bin/env python3

# Google IT Automation with Python - Testing, Raising Errors

def validate_user(username, minlen):
    assert type(username) == str, "username my be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

