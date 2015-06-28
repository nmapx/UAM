# -*- coding: utf-8 -*-

"""Implementacja alfa-beta obcinania"""


def alpha_beta(game):
    """Wylicza wartość gry."""
    return state_alpha_beta(game, -9999, +9999,
                            game.initial_state())

def state_alpha_beta(game, alpha, beta, state):
    """Wylicza wartość stanu."""

    game_value = game.check_final_state(state)
    if game_value != None:
        return game_value

    if game.player_to_go(state) == 'max':
        for next_state in game.moves(state):
            alpha = max(alpha,
                        state_alpha_beta(game, alpha, beta, next_state))
            if beta <= alpha:
                break
        return alpha
    else:
        for next_state in game.moves(state):
            beta = min(beta,
                       state_alpha_beta(game, alpha, beta, next_state))
            if beta <= alpha:
                break
        return beta

from tictactoe import TicTacToe

if __name__ == '__main__':
    TICTACTOE = TicTacToe()
    print alpha_beta(TICTACTOE)
    print state_alpha_beta(TICTACTOE, -9999, +9999,
                           ((' ', 'o', ' '),
                            (' ', 'x', ' '),
                            (' ', ' ', ' ')))
