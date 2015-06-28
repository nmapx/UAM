#!/usr/bin/python2
# -*- coding: utf-8 -*-

from CrossingRiver import CrossingRiver
from BreadthFirstSearch import breadth_first
from DepthFirstSearch import depth_first

CROSSING_RIVER = CrossingRiver()
print breadth_first(CROSSING_RIVER, (('c', 'f', 'k', 'w'), ()))
