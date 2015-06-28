"""Zadanie D02"""
from math import sqrt

def sim_distance(ratings1, ratings2):
    """Zadanie D02"""
    for band in ratings1:
        if band not in ratings2:
            ratings2[band] = 0
    for band in ratings2:
        if band not in ratings1:
            ratings1[band] = 0
    dist = 0.0
    for band in ratings1:
        dist += (ratings1[band] - ratings2[band])**2
    dist = sqrt(dist)
    return 1/(1+dist)
