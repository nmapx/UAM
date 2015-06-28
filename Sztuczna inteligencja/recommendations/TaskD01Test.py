# -*- coding: utf-8 -*-

"""
Zadanie D01

Zaimplementuj funkcję `load_data(file_obj, normalize=True)`, która zwraca
słownik słowników. Kluczami głównego słownika są identyfikatory
użytkowników, wartościami są kolejne słowniki. Klucze tych słowników
to nazwy artystów, wartości to liczba, ile raz dany użytkownik
odsłuchał utwór tego artysty. W wypadku, gdy zmienna `normalize` ma
wartość `True`, należy normalizować liczby odtwarzania, tzn. dla danego
użytkownika należy podzielić te liczby przez największą z nich.

NAME: load_data
PARAMS: file, bool
RETURN: dict
POINTS: 3
"""

import unittest
import codecs
from TaskD01 import load_data

class TaskD01Test(unittest.TestCase):
    """Testy do zadania TaskD01."""

    @staticmethod
    def round_dict_values(old_dict, precision=4):
        """Pomocnicza funkcja do zaokrąglania."""
        new_dict = {}
        for key in old_dict:
            new_dict[key] = dict(
                (k, round(old_dict[key][k], precision)) for k in old_dict[key])
        return new_dict


    def test_no_normalization(self):
        """Test bez normalizacji."""

        prefs_test = {
            '10': {u'Beirut': 1137.0}, '13': {u'Evanescence': 2.0},
            '15': {u'le bowl': 835.0}, '14': {u'The Montesas': 602.0},
            '17': {u'Rihanna': 129.0, u'The Veronicas': 891.0, u'Sia': 168.0,
                   u'Britney Spears': 118.0},
            '16': {u'Lena': 264.0},
            '18': {u'Eric Clapton': 236.0, u'The White Stripes': 660.0},
            '22': {u'Corpus Christi': 1284.0},
            '20': {u'The Crystal Method': 99.0, u'Salem': 285.0},
            '2': {u'Röyksopp': 3644.0, u'Japan': 1332},
            '4': {u'אביתר בנאי': 384.0},
            '7': {u'Danity Kane': 1027.0},
            '6': {u'Jill Scott': 17.0,
                  u'Lokua Kanza': 20.0,
                  u'Dru Hill': 16.0},
            '9': {u'Katatonia': 1113.0},
            '8': {u'Milow': 400.0, u'Lily Allen': 613.0},
            '21': {u'Dima Bilan': 180.0}}

        dat_file = codecs.open("lastfm.test.dat", "r", "utf-8")

        prefs = load_data(dat_file, normalize=False)

        dat_file.close()

        self.assertTrue("userID" not in prefs)
        self.assertEqual(prefs_test, self.round_dict_values(prefs))

    def test_normalization(self):
        """Test z normalizacją."""

        prefs_norm_test = {
            '10': {u'Beirut': 1.0}, '13': {u'Evanescence': 1.0},
            '15': {u'le bowl': 1.0}, '14': {u'The Montesas': 1.0},
            '17': {u'Rihanna': 0.1448, u'The Veronicas': 1.0, u'Sia': 0.1886,
                   u'Britney Spears': 0.1324},
            '16': {u'Lena': 1.0},
            '18': {u'Eric Clapton': 0.3576, u'The White Stripes': 1.0},
            '22': {u'Corpus Christi': 1.0}, '21': {u'Dima Bilan': 1.0},
            '2': {u'Röyksopp': 1.0, u'Japan': 0.3655},
            '4': {u'אביתר בנאי': 1.0},
            '7': {u'Danity Kane': 1.0},
            '6': {u'Jill Scott': 0.85, u'Lokua Kanza': 1.0, u'Dru Hill': 0.8},
            '9': {u'Katatonia': 1.0},
            '20': {u'The Crystal Method': 0.3474, u'Salem': 1.0},
            '8': {u'Milow': 0.6525, u'Lily Allen': 1.0}}

        dat_file = codecs.open("lastfm.test.dat", "r", "utf-8")

        prefs_norm = load_data(dat_file, normalize=True)

        dat_file.close()

        self.assertTrue("userID" not in prefs_norm)
        self.assertEqual(prefs_norm_test, self.round_dict_values(prefs_norm))

if __name__ == '__main__':
    unittest.main()
