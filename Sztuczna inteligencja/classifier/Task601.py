# -*- coding: utf-8 -*-

"""
Zadanie 601
"""

def train(bayes, item, cat):
    features = bayes.get_features(item)
    if cat in bayes.class_count.keys():
        bayes.class_count[cat] += 1
    else:
        bayes.class_count[cat] = 1

    for feature in features:
        if (feature, cat) in bayes.feature_count.keys():
            bayes.feature_count[(feature, cat)] += 1
        else:
            bayes.feature_count[(feature, cat)] = 1
