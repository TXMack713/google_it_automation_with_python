#!/usr/bin/env python3

# Google IT Automation with Python - Unit Tests, Writing Unit Tests in Python

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        print("Testcase: " + testcase)
        print("Expected: " + expected)
        print("Actual: " + rearrange_name(testcase))
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()