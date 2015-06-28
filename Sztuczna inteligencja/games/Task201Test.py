# -*- coding: utf-8 -*-

"""
Zadanie 201

Napisz klasę Dominoes, reprezentującą grę w domino. Stan w grze to
krotka (P, X, A, B), gdzie P to gracz przy ruchu, X to krotka
dwuelementowa (L, R) składająca się z lewego i prawego brzegu kostek
już wyłożonych lub None, jeśli nie wyłożono jeszcze żadnej kostki, A i
B to krotki składające się z kostek gracza, odpowiednio, 'max' i
'min'. (Kostka to para liczb). Zakładamy, że X, A i B są posortowane
(przy użyciu funkcji `sorted`). Stan początkowy może być dowolny i
powinien być podawany w konstruktorze (inaczej niż w przykładowym
tictactoe.py, gdzie stan początkowy był jeden, z góry ustalony).
Wygrywa ten gracz, który wyłoży wszystkie kostki lub ten, który ma
mniej kostek, gdy żaden z graczy nie może wykonać ruchu. Uwaga: jeśli
gracz nie może dołożyć żadnej kostki, funkcja moves, powinna zwracać
listę jednoelementową złożoną z danego stanu (strata kolejki).

NAME: Dominoes
PARAMS:
RETURN:
POINTS: 6
"""

import unittest
from Task201 import Dominoes

class Task201Test(unittest.TestCase):
    """Testy do zadania 201"""

    def test(self):
        """Test."""
        dominoes = Dominoes(('max', None, ((0, 0), (1, 2)), ((3, 4),)))

        self.assertEqual(
            dominoes.initial_state(),
            ('max', None, ((0, 0), (1, 2)), ((3, 4),)))

        # żadne kostki nie są wyłożone
        self.assertItemsEqual(
            dominoes.moves(dominoes.initial_state()),
            [('min', (0, 0), ((1, 2),), ((3, 4),)),
             ('min', (1, 2), ((0, 0),), ((3, 4),))])

        # jakieś kostki wyłożone, 'min' może wyłożyć jedną z czterech kostek
        self.assertItemsEqual(
            dominoes.moves(
                ('min',
                 (1, 5),
                 ((2, 4),),
                 ((0, 0), (0, 1), (2, 3), (3, 5), (5, 5), (5, 6)))),
            [('max',
              (0, 5),
              ((2, 4),),
              ((0, 0), (2, 3), (3, 5), (5, 5), (5, 6))),
             ('max',
              (1, 3),
              ((2, 4),),
              ((0, 0), (0, 1), (2, 3), (5, 5), (5, 6))),
             ('max',
              (1, 5),
              ((2, 4),),
              ((0, 0), (0, 1), (2, 3), (3, 5), (5, 6))),
             ('max',
              (1, 6),
              ((2, 4),),
              ((0, 0), (0, 1), (2, 3), (3, 5), (5, 5)))])

        # strata kolejki
        dead_end_state = ('max',
                          (1, 5),
                          ((2, 4),),
                          ((0, 0), (0, 1), (2, 3), (3, 5), (5, 5), (5, 6)))
        self.assertItemsEqual(
                dominoes.moves(dead_end_state),
                [dead_end_state])


        # ślepy zaułek dla max-a, ale nie dla mina, więc
        # gra się jeszcze nie kończy
        self.assertIsNone(
                dominoes.check_final_state(dead_end_state))

        self.assertEqual(
                dominoes.check_final_state(
                    ('max',
                     (1, 5),
                     (),
                     ((4, 5),))),
                1)

        self.assertEqual(
                dominoes.check_final_state(
                    ('max',
                     (1, 5),
                     ((2, 5),(1, 4)),
                     ())),
                -1)

        # blokada, wygrywa max
        self.assertEqual(
                dominoes.check_final_state(
                    ('max',
                     (0, 1),
                     ((2, 5), (4, 4)),
                     ((2, 2), (2, 3), (5, 5), (6, 6)))),
                1)

        # blokada - remis
        self.assertEqual(
                dominoes.check_final_state(
                    ('max',
                     (0, 1),
                     ((2, 5), (4, 4)),
                     ((2, 2), (2, 3)))),
                0)

        self.assertEqual(
            dominoes.player_to_go(
                ('max',
                 (1, 5),
                 ((1, 3),),
                 ((4, 5),))),
            'max')

        self.assertEqual(
            dominoes.player_to_go(
                ('min',
                 (1, 5),
                 ((1, 3),),
                 ((4, 5),))),
            'min')

if __name__ == '__main__':
    unittest.main()
