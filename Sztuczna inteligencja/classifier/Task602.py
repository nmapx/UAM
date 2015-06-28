# -*- coding: utf-8 -*-

"""
Zadanie 602
"""

import math

def featprob(bayes, feature, cat):
    if cat not in bayes.class_count:
        return -1e+300
    if (feature, cat) not in bayes.feature_count:
        return math.log(float(0.001 / bayes.class_count[cat]))
    else:
        return math.log(float(bayes.feature_count[(feature, cat)]) / bayes.class_count[cat])
