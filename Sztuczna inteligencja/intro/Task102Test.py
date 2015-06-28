#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
Zadanie 102

(Zadanie rozgrzewkowe z Pythona).

Napisz funkcję `days_in_year` zwracającą liczbę dni w roku (365 albo 366).

NAME: days_in_year
PARAMS: int
RETURN: int
POINTS: 1
"""

import unittest
from Task102 import days_in_year

class Task101Test(unittest.TestCase):
    """Testy do zadania 101"""

    def test_this_year(self):
        """Prosty test."""
        self.assertEqual(days_in_year(2015), 365)

    def test_leap_year(self):
        """Rok przestępny"""
        self.assertEqual(days_in_year(2012), 366)

    def test_century_turn_non_leap(self):
        """Podzielny przez 100."""
        self.assertEqual(days_in_year(1900), 365)

    def test_century_turn_leap(self):
        """Podzielny przez 400."""
        self.assertEqual(days_in_year(2400), 366)

    def test_century_2000(self):
        """Rok 2000."""
        self.assertEqual(days_in_year(2000), 366)

    def test_some_year(self):
        """Jakiś tam rok nieprzestępny."""
        self.assertEqual(days_in_year(1977), 365)

    def test_other_year(self):
        """Jakiś tam rok przestępny."""
        self.assertEqual(days_in_year(2040), 366)


if __name__ == '__main__':
    unittest.main()
