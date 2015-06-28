# -*- coding: utf-8 -*-

"""
Zadanie 105

Popraw `DepthFirstSearch`, tak aby nie były generowane cykle -
stworzyć pomocniczą funkcję, która jako argument będzie przyjmowała
zbiór do tej pory odwiedzonych stanów.

NAME: depth_first
PARAMS: puzzle, node
RETURN: list
POINTS: 4
"""

import unittest
from InfinitePuzzle import InfinitePuzzle
from CrossingRiver import CrossingRiver
from Task105 import depth_first


class Task105Test(unittest.TestCase):
    """Testy do zadania 105"""

    def test_infinite(self):
        """Test na nieskończonej łamigłówce."""
        infinity_puzzle = InfinitePuzzle()

        # możemy tylko przetestować przypadek, gdy od razu mamy rozwiązanie
        final_state = ('s', 'b', 'b', 'b', 'b')
        self.assertEqual(depth_first(infinity_puzzle, final_state),
                         [final_state])

    def test_crossing_river(self):
        """Test na przekraczaniu rzeki."""
        crossing_puzzle = CrossingRiver()

        start_state = (('c', 'f', 'k', 'w'), ())


        solution = depth_first(crossing_puzzle, start_state)

        self.assertNotEqual(solution, None)
        self.assertEqual(len(solution), 8)


if __name__ == '__main__':
    unittest.main()
