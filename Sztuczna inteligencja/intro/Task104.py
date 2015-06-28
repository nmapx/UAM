#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Rozwiazanie zadania 4 """

def depth_first(puzzle, node, step):
    if puzzle.is_target(node):
        return [node]
    if step == 0:
        return None
    for next_node in puzzle.transition(node):
        path_found = depth_first(puzzle, next_node, step - 1)
        if path_found != None:
            return [node] + path_found
    return None
