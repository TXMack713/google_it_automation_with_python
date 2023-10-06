#!/usr/bin/env python3

# Google IT Automation with Python - Testing, Practice Testing

import unittest

from test_practice import LetterCompiler

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        print("Testcase: " + str(testcase))
        print("Expected: " + str(expected))
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_empty(self):
        testcase = "da"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_none(self):
        testcase = "da"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main()
