#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
Zadanie 102
"""

import calendar

def days_in_year(number):
    """funkcja"""
    return 366 if calendar.isleap(number) else 365
