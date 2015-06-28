# -*- coding: utf-8 -*-

"""
Zadanie 104

W `DepthFirstSearch` wprowadzić limit na głębokość - `depth_first`
powinno mieć argument `maxdepth` określający maksymalny poziom
zagłębienia.

NAME: depth_first
PARAMS: puzzle, node, maxdepth
RETURN: list
POINTS: 2
"""

import unittest
from InfinitePuzzle import InfinitePuzzle
from CrossingRiver import CrossingRiver
from Task104 import depth_first

class Task104Test(unittest.TestCase):
    """Testy do zadania 104"""

    def test_infinite(self):
        """Test na nieskończonej łamigłówce."""
        infinity_puzzle = InfinitePuzzle()

        self.assertEqual(depth_first(infinity_puzzle, ('s',), 3), None)
        self.assertEqual(depth_first(infinity_puzzle, ('s',), 4),
                         [('s',),
                          ('s', 'b'),
                          ('s', 'b', 'b'),
                          ('s', 'b', 'b', 'b'),
                          ('s', 'b', 'b', 'b', 'b')])

    def test_crossing_river(self):
        """Test na przekraczaniu rzeki."""
        crossing_puzzle = CrossingRiver()

        start_state = (('c', 'f', 'k', 'w'), ())

        self.assertEqual(depth_first(crossing_puzzle, start_state, 0),
                         None)

        self.assertEqual(depth_first(crossing_puzzle, start_state, 6),
                         None)

        solution = depth_first(crossing_puzzle, start_state, 7)

        self.assertNotEqual(solution, None)



if __name__ == '__main__':
    unittest.main()
