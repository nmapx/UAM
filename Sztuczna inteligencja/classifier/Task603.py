# -*- coding: utf-8 -*-

"""
Zadanie 603
"""

import math

def catprob(bayes, cat):
    if cat not in bayes.class_count:
        return -1e+300
    else:
        return math.log(float(bayes.class_count[cat]) / sum(bayes.class_count.values()))
