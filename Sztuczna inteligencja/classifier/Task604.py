# -*- coding: utf-8 -*-

"""
Zadanie 604
"""

from Task602 import featprob
from Task603 import catprob

def docprob(bayes, item, cat):
    """Zadanie 604"""
    features = bayes.get_features(item)
    features_sum = 0
    for feature in features:
        features_sum = features_sum + featprob(bayes, feature, cat)
    return catprob(bayes, cat) + features_sum
