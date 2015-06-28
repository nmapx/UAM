# -*- coding: utf-8 -*-

"""
Zadanie 204

Na podstawie minimax.py napisz funkcję `best_move(game, state)`, która
dla zadanej gry i zadanego stanu zwraca parę `(val, best_state)`,
gdzie `val` jest wartością gry, `best_state` - stanem, który zostanie
osiągnięty przy najlepszym ruchu. Jeśli state jest stanem końcowym,
należy zwrócić parę `(val, None)`. Zauważmy, że różnica między `best_move`
a `minimax` polega tylko na tym, że `minimax` zwraca tylko wartość gry, a
`best_move` również optymalne posunięcie dla gracza przy ruchu.

NAME: best_move
PARAMS: Game, state
RETURN: pair
POINTS: 4
"""

import unittest
from tictactoe import TicTacToe
from Task204 import best_move

class Task204Test(unittest.TestCase):
    """Testy do zadania 204"""

    def test(self):
        """Test."""
        tictactoe = TicTacToe()

        self.assertEqual(
            best_move(
                tictactoe,
                ((' ', 'o', 'x'),
                 (' ', 'x', 'o'),
                 (' ', 'x', 'o'))),
            (1,
             ((' ', 'o', 'x'),
              (' ', 'x', 'o'),
              ('x', 'x', 'o'))))

        self.assertEqual(
            best_move(
                tictactoe,
                (('x', 'o', ' '),
                 (' ', 'x', 'o'),
                 (' ', 'x', 'o'))),
            (0,
             (('x', 'o', 'x'),
              (' ', 'x', 'o'),
              (' ', 'x', 'o'))))


        # już stan końcowy
        self.assertEqual(
            best_move(
                tictactoe,
                ((' ', 'o', 'x'),
                 (' ', 'x', 'o'),
                 ('x', 'x', 'o'))),
            (1, None))





if __name__ == '__main__':
    unittest.main()
