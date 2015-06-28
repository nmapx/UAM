# -*- coding: utf-8 -*-

"""Implementacja algorytmu min-max."""

def minimax(game):
    """Wylicza wartość gry."""
    return state_minimax(game, game.initial_state())

def state_minimax(game, state):
    """Wylicza wartość stanu."""
    game_value = game.check_final_state(state)
    if game_value != None:
        return game_value

    if game.player_to_go(state) == 'min':
        fun = min
    else:
        fun = max

    return fun([state_minimax(game, next_state)
                for next_state in game.moves(state)])

from tictactoe import TicTacToe

if __name__ == '__main__':
    TICTACTOE = TicTacToe()
    print minimax(TICTACTOE)
    print state_minimax(TICTACTOE,
                  (('x', 'o', ' '),
                   (' ', 'x', 'o'),
                   (' ', 'x', 'o')))
