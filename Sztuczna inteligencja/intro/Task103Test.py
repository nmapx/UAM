#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
Zadanie 103

Napisz funkcje `oov(text, vocab)`, która zwraca listę wyrazów (bez
duplikatów), które występują w tekście `text` i nie występują w
liście znanych wyrazów `vocab`. Argumenty funkcji `text` i `vocab`
to odpowiednio łańcuch znakowy i lista łańuchów znakowych.
Wszystkie wyrazy należy zmienić na małe litery. (OOV = out of
vocabulary)

NAME: oov
PARAMS: string, list
RETURN: list
POINTS: 3
"""

import unittest
from Task103 import oov

class Task103Test(unittest.TestCase):
    """Testy do zadania 103."""

    def test(self):
        """Prosty test."""
        text   = "This is a string , which I will use for string testing"
        vocab  = [',', 'this', 'is', 'a', 'which', 'for', 'will', 'I']
        oo_voc = ['string', 'testing', 'use']

        self.assertEqual(set(oov(text, vocab)), set(oo_voc))

if __name__ == '__main__':
    unittest.main()
