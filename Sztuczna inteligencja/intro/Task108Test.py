# -*- coding: utf-8 -*-

"""
Zadanie 108

Opracować heurystykę dla piętnastki - funkcja ma zwracać sumę
odległości (w metryce miasta) każdej płytki od docelowego położenia.

NAME: fifteen_totdist
PARAMS: state
RETURN: int
POINTS: 5
"""

import unittest
from Task108 import fifteen_totdist

class Task108Test(unittest.TestCase):
    """Testy do zadania 108"""

    def test_target_state(self):
        """Test dla układu docelowego."""
        self.assertEqual(fifteen_totdist(
                (( 1,  2,  3,  4),
                 ( 5,  6,  7,  8),
                 ( 9, 10, 11, 12),
                 (13, 14, 15,  0))), 0)

    def test_almost_state(self):
        """Testy dla układów prawie docelowych."""
        self.assertEqual(fifteen_totdist(
                (( 1,  2,  3,  4),
                 ( 5,  6,  7,  8),
                 ( 9, 10, 11,  0),
                 (13, 14, 15, 12))), 1)

        self.assertEqual(fifteen_totdist(
                (( 1,  2,  3,  4),
                 ( 5,  6,  7,  8),
                 ( 9, 10, 11, 12),
                 (13, 14,  0, 15))), 1)

    def test_various_state(self):
        """Testy dla różnych stanów."""
        self.assertEqual(fifteen_totdist(
                (( 2,  1,  3,  4),
                 ( 5,  6,  7,  8),
                 ( 9, 10, 11, 12),
                 (13, 14, 15,  0))), 2)

        self.assertEqual(fifteen_totdist(
                (( 1,  2, 11,  4),
                 ( 5,  6,  7,  8),
                 ( 9, 10,  3, 12),
                 (13, 14, 15,  0))), 4)

        self.assertEqual(fifteen_totdist(
                (( 1, 15,  3,  4),
                 ( 5,  6,  7,  2),
                 ( 9,  0, 11, 12),
                 (13, 14,  8, 10))), 13)

if __name__ == '__main__':
    unittest.main()
