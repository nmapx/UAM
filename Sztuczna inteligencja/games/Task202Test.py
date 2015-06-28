# -*- coding: utf-8 -*-

"""
Zadanie 202

Napisz klasę Nim, reprezentującą grę nim (zob.
https://pl.wikipedia.org/wiki/Nim). Stan w grze to krotka (P, K1, ...,
KN), gdzie P to gracz przy ruchu ('min' bądź 'max'), K1, ..., KN to
liczba pionków w poszczególnych kupkach. Stan początkowy powinien być
podawany w konstruktorze. Aby uniknąć niepotrzebnych powtórzeń stanów,
K1, ..., KN są posortowane rosnąco (przypominamy, że w Pythonie do
sortowanie służy funkcja `sorted`). Nie odnotowujemy kupek, z których
zabrano wszystkie piony (K1, ..., KN są zawsze dodatnie). Stanem
końcowym jest stan (P), tzn. stan osiągany, gdy zostały zabrane
wszystkie pionki. Przyjmujemy wariant, w którym wygrywa ten gracz,
który zabrał ostatni pionek.


NAME: Nim
PARAMS:
RETURN:
POINTS: 5
"""

import unittest
from Task202 import Nim

class Task202Test(unittest.TestCase):
    """Testy do zadania 202"""

    def test(self):
        """Test."""
        nim = Nim(('min', 4, 5, 6, 7))

        self.assertEqual(nim.initial_state(), ('min', 4, 5, 6, 7))

        self.assertItemsEqual(
            nim.moves(('max', 5)),
            [('min',),
             ('min', 1),
             ('min', 2),
             ('min', 3),
             ('min', 4)])


        self.assertItemsEqual(
            nim.moves(('min', 2, 2, 3)),
            [('max', 1, 2, 3),
             ('max', 2, 3),
             ('max', 2, 2, 2),
             ('max', 1, 2, 2),
             ('max', 2, 2)])

        self.assertEqual(nim.check_final_state(('max',)), -1)
        self.assertEqual(nim.check_final_state(('min',)), 1)
        self.assertIsNone(nim.check_final_state(('max', 2, 5)))

        self.assertEqual(nim.player_to_go(('min', 4)), 'min')
        self.assertEqual(nim.player_to_go(('max', 4, 5, 8)), 'max')

if __name__ == '__main__':
    unittest.main()
