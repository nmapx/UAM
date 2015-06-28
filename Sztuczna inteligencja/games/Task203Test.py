# -*- coding: utf-8 -*-

"""
Zadanie 203

Napisz klasę `dominoes_heuristics(state)`, która dla zadanego stanu
gry (jak opisano w zadaniu 201) zwraca heurystyczne oszacowanie
wartości gry wg następującego wzoru: różnica kostek posiadanych przez
mina i posiadanych przez maxa podzielona przez liczbę wszystkich
kostek posiadanych przez obu graczy. (Im mniej kostek gracz ma, tym
lepiej). Jeśli pozycja jest pozycją końcową (któryś z graczy wyłożył
wszystkie kostki lub jeśli żaden z graczy nie może wyłożyć żadnej
kostki), należy zwrócić końcową, dokładną wartość gry.

NAME: dominoes_heuristics
PARAMS:
RETURN: float
POINTS: 4
"""

import unittest
from Task203 import dominoes_heuristics

class Task203Test(unittest.TestCase):
    """Testy do zadania 203"""

    def test(self):
        """Test."""

        self.assertAlmostEqual(
            dominoes_heuristics(
                ('max',
                 (1, 5),
                 ((2, 3), (3, 3), (3, 4)),
                 ((0, 1), (0, 2)))),
            -0.2)


        self.assertAlmostEqual(
            dominoes_heuristics(
                ('min',
                 (1, 5),
                 ((0, 0),),
                 ((1, 3), (2, 4), (4, 4)))),
            0.5)

        self.assertAlmostEqual(
            dominoes_heuristics(
                ('min',
                 (1, 5),
                 ((0, 0), (3, 5)),
                 ((1, 1), (5, 5)))),
            0)

        # wygrana max-a
        self.assertAlmostEqual(
            dominoes_heuristics(
                ('min',
                 (1, 5),
                 (),
                 ((1, 3), (2, 4), (4, 4)))),
            1)


        # blokada, wygrana min-a (ma mniej kostek)
        self.assertAlmostEqual(
            dominoes_heuristics(
                ('min',
                 (0, 0),
                 ((1, 3), (2, 4), (5, 6), (6, 6)),
                 ((1, 4), (4, 4), (4, 5)))),
            -1)

        # blokada, remis
        self.assertAlmostEqual(
            dominoes_heuristics(
                ('min',
                 (0, 0),
                 ((1, 3), (2, 4), (5, 6), (6, 6)),
                 ((1, 4), (4, 4), (4, 5), (4, 6)))),
            0)

if __name__ == '__main__':
    unittest.main()
