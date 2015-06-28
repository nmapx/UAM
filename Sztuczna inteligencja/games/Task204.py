#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 204."""

from minimax import state_minimax

def best_move(game, stat):
    """Funkcja"""
    val = game.check_final_state(stat)
    if val != None:
        return (val, None)
    if game.player_to_go(stat) == 'min':
        val = 1000
    else:
        val = -10000
    best_stat = None
    for next_stat in game.moves(stat):
        current_val = state_minimax(game, next_stat)
        if game.player_to_go(stat) == 'min':
            if min(current_val, val) == current_val:
                val = current_val
                best_stat = next_stat
        else:
            if max(current_val, val) == current_val:
                val = current_val
                best_stat = next_stat
    return (val, best_stat)
