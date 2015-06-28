#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Zadanie 106

Napisz klasę CouplesPuzzle reprezentującą zagadkę o przekraczaniu rzeki przez 3 małżeństwa:
- łódka może pomieścić tylko 2 osoby
- kobieta nie może znaleźć się w towarzystwie innego mężczyzny (na brzegu lub łódce), chyba
  że obecny jest jej mąż.

Zakładamy, że stan łamigłówki  to
krotka (L, R, b), gdzie L to stan na lewym brzegu, R - na prawym
brzegu, b - pozycja łódki ('l' albo 'r').

L i R mają postać krotki zawierające postacie z zagadki, trzy małżeństwa:
'a'/'A', 'b'/'B', 'c'/'C'. Małe litery oznaczają kobiety, wielkie - mężów.

Zakładamy, że krotka jest posortowana alfabetycznie (najpierw wielkie litery).

Podpowiedź: przerobić CrossingRiver

NAME: CouplesPuzzle
PARAMS:
RETURN:
POINTS: 9

"""

import unittest
from Task106 import CouplesPuzzle

class Task106Test(unittest.TestCase):
    """Testy do zadania 106"""

    def test(self):
        """Test."""
        puzzle = CouplesPuzzle()

        self.assertTrue(puzzle.is_target(
                ((), ('A', 'B', 'C', 'a', 'b', 'c'), 'r')))

        self.assertFalse(puzzle.is_target(
                (('a',), ('A', 'B', 'C',  'b', 'c'), 'l')))

        self.assertFalse(puzzle.is_target(
                (('a',), ('A', 'B', 'C',  'b', 'c'), 'r')))


        self.assertTrue(
            (('A', 'C', 'a', 'c'), ('B', 'b'), 'r') in
            puzzle.transition((('A', 'B', 'C', 'a', 'b', 'c'), (), 'l'))

        self.assertFalse(
            (('A', 'C', 'a', 'b', 'c'), ('B',), 'r') in
            puzzle.transition((('A', 'B', 'C', 'a', 'b', 'c'), (), 'l'))

        self.assertTrue(
            (('A', 'B', 'C', 'a', 'c'), ('b',), 'r') in
            puzzle.transition((('A', 'B', 'C', 'a', 'b', 'c'), (), 'l'))


if __name__ == '__main__':
    unittest.main()
