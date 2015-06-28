# -*- coding: utf-8 -*-

"""
Zadanie 604

Napisz funkcję `docprob(bayes, item, cat)`, która oblicza uogólnioną
sumę z równania (5) - łącznie z prawdopodobieństwem kategorii.
Podobnie jak w zadaniu 601 wykorzystujemy funkcję
`self.get_features(item)` w celu uzyskania zbioru cech dokumentu
`item`. Skorzystać z rozwiązań zadań 602 i 603.

NAME: docprob
PARAMS: NaiveBayes, item, cat
RETURN: float
POINTS: 4
"""

import unittest
import NaiveBayes
from Task604 import docprob

class Task604Test(unittest.TestCase):
    """Testy do zadania Task604."""

    def test(self):
        """Test na sztucznych danych."""

        def getfeatures(text):
            """Funkcja do testów."""
            return list(set(text.split()))

        bayes = NaiveBayes.NaiveBayes(getfeatures)

        bayes.feature_count = {('terms,', 'C1'): 1, ('considers', 'C2'): 1,
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

        bayes.class_count = {'C1': 2, 'C2': 3, 'C3': 2}

        categories = ['C1', 'C2', 'C3', 'C4', 'C5']

        expected_probs = [
            [-49.630766, -59.494565, -71.047179,
              -1.2000000000000003e+301, -1.2000000000000003e+301 ],
            [-86.248984, -96.9237086, -86.248984,
             -1.4000000000000004e+301, -1.4000000000000004e+301 ],
            [-64.139424, -67.500928, -85.55583720,
             -1.3000000000000003e+301, -1.3000000000000003e+301 ],
            [ -79.34122, -83.9191283, -93.8498868,
             -1.5000000000000004e+301, -1.5000000000000004e+301 ],
            [  -47.55132, -49.98411, -40.6435696,
             -8e+300, -8e+300] ]

        items = [
            "Depending on the precise nature of the probability"
            " model, naive Bayes classifiers",
            "can be trained very efficiently in a supervised"
            " learning setting. In many practical",
            "applications, parameter estimation for naive Bayes"
            " models uses the method of maximum",
            "likelihood; in other words, one can work with"
            " the naive Bayes model without believing",
            "in Bayesian probability or using any Bayesian methods."
            ]

        for idx in range(len(items)):
            for category_id in range(len(categories)):
                self.assertAlmostEqual(
                    docprob(bayes, items[idx], categories[category_id]),
                    expected_probs[idx][category_id],
                    4)

if __name__ == '__main__':
    unittest.main()
