#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 203."""

def dominoes_heuristics(stat):
    """dominoes_heuristics"""
    win = check_final_state(stat)
    if win is not None:
        if win == 'min':
            return -1
        else:
            return 1
    else:
        return float((len(stat[3])-len(stat[2])))/len(stat[3]+stat[2])

def check_final_state(stat):
    """check_final_state"""
    if len(stat[2]) == 0:
        return 'max'
    if len(stat[3]) == 0:
        return 'min'
    if not is_possible_move(stat):
        if len(stat[2]) < len(stat[3]):
            return "max"
        elif len(stat[3]) < len(stat[2]):
            return "min"
    return None

def is_possible_move(stat):
    """Sprawdza czy są możliwe jakieś ruchy."""
    for pair in stat[2]+stat[3]:
        if set(stat[1]) & set(pair):
            return True
    return False
