# -*- coding: utf-8 -*-

"""
Zadanie 601

Napisz funkcję `train(bayes, item, cat)`, która zlicza, ile razy pojawiła
się dana kategoria `cat` oraz, ile razy cechy dokumentu `item`
współwystępowały z daną categorią. Funkcja korzysta z metody
`bayes.get_features(item)`, żeby uzyskać zbiór cech. Należy zwiększać
słownik `bayes.feature_count` dla każdej pary cechy i kategorii o
jeden. W słowniku `bayes.class_count` należy zliczać, ile dokumentów
należy do danej kategorii.

NAME: train
PARAMS: NaiveBayes, string, string
RETURN: -
POINTS: 4
"""

import unittest
import NaiveBayes
from Task601 import train

class Task601Test(unittest.TestCase):
    """Testy do zadania Task601."""

    def test(self):
        """Test na sztucznych danych."""

        def getfeatures(text):
            """Funkcja do testów."""
            return list(set(text.split()))

        bayes = NaiveBayes.NaiveBayes(getfeatures)
        train(bayes,
            "In simple terms, a naive Bayes"
            " classifier assumes that the presence",
            "C1")
        train(bayes,
            "(or absence) of a particular feature of"
            " a class is unrelated to the",
            "C2")
        train(bayes,
            "presence (or absence) of any other feature."
            " For example, a fruit may",
            "C2")
        train(bayes,
            "be considered to be an apple if it is red,"
            " round, and about 4\" in diameter.",
            "C3")
        train(bayes,
            "Even if these features depend on each other"
            " or upon the existence of",
            "C1")
        train(bayes,
            "the other features, a naive Bayes classifier"
            " considers all of these",
            "C2")
        train(bayes,
            "properties to independently contribute"
            " to the probability that this",
            "C3")

        f_counts = {('terms,', 'C1'): 1, ('considers', 'C2'): 1,
                    ('independently', 'C3'): 1, ('each', 'C1'): 1,
                    ('that', 'C1'): 1, ('the', 'C3'): 1, ('on', 'C1'): 1,
                    ('features', 'C1'): 1, ('and', 'C3'): 1, ('is', 'C2'): 1,
                    ('feature.', 'C2'): 1, ('For', 'C2'): 1, ('fruit', 'C2'): 1,
                    ('features,', 'C2'): 1, ('classifier', 'C2'): 1,
                    ('(or', 'C2'): 2, ('these', 'C1'): 1, ('the', 'C2'): 2,
                    ('particular', 'C2'): 1, ('may', 'C2'): 1,
                    ('Bayes', 'C2'): 1, ('all', 'C2'): 1, ('feature', 'C2'): 1,
                    ('apple', 'C3'): 1, ('naive', 'C2'): 1, ('depend', 'C1'): 1,
                    ('other', 'C2'): 2, ('if', 'C3'): 1,
                    ('contribute', 'C3'): 1, ('any', 'C2'): 1,
                    ('these', 'C2'): 1, ('4"', 'C3'): 1,
                    ('classifier', 'C1'): 1, ('other', 'C1'): 1,
                    ('of', 'C1'): 1, ('assumes', 'C1'): 1,
                    ('Bayes', 'C1'): 1, ('Even', 'C1'): 1,
                    ('presence', 'C1'): 1, ('the', 'C1'): 2,
                    ('a', 'C2'): 3, ('upon', 'C1'): 1,
                    ('that', 'C3'): 1, ('example,', 'C2'): 1,
                    ('properties', 'C3'): 1, ('this', 'C3'): 1,
                    ('to', 'C2'): 1, ('In', 'C1'): 1,
                    ('round,', 'C3'): 1, ('about', 'C3'): 1,
                    ('absence)', 'C2'): 2, ('of', 'C2'): 3,
                    ('diameter.', 'C3'): 1,
                    ('existence', 'C1'): 1, ('be', 'C3'): 1,
                    ('considered', 'C3'): 1, ('a', 'C1'): 1,
                    ('it', 'C3'): 1, ('an', 'C3'): 1,
                    ('or', 'C1'): 1, ('if', 'C1'): 1,
                    ('presence', 'C2'): 1, ('is', 'C3'): 1,
                    ('to', 'C3'): 2, ('unrelated', 'C2'): 1,
                    ('red,', 'C3'): 1, ('probability', 'C3'): 1,
                    ('naive', 'C1'): 1, ('class', 'C2'): 1,
                    ('in', 'C3'): 1, ('simple', 'C1'): 1}

        c_counts = {'C1': 2, 'C2': 3, 'C3': 2}

        self.assertEqual(f_counts, bayes.feature_count)
        self.assertEqual(c_counts, bayes.class_count)

if __name__ == '__main__':
    unittest.main()
