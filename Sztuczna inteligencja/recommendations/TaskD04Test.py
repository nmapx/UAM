# -*- coding: utf-8 -*-

"""
Zadanie D04

Zaimplementuj funkcję `get_recommendations(prefs, rating, min_users=1,
similarity=sim_pearson)`, która zwraca listę rekomendowanych artystów.
Lista wynikowa jest listą par postaci [(artysta, ocena), ...]
posortowana malejąco według oceny. Ocenę należy obliczyć jako średnią
ważoną ocen dla każdego artysty. Wagami są stopnie podobieństwa
podanego zestawu preferencji do preferencji kolejnych użytkowników ze
słownika prefs. Należy brać pod uwagę tylko tych artystów, którzy
zostali odnotowani przy przynajmniej `min_users` użytkownikach. Należy
pamiętać, żeby nie rekomendować użytkownikowi znanych mu artystów.
UWAGA: testy do tego zadania wymagają wcześniejszego wykonania zadania
D03.

NAME: get_recommendations
PARAMS: dict, dict, int, function
RETURN: list
POINTS: 3
"""

import unittest
from TaskD03 import sim_pearson
from TaskD04 import get_recommendations

class TaskD04Test(unittest.TestCase):
    """Testy do zadania TaskD04."""

    def test_complicated(self):
        """Bardziej skomplikowany test."""

        prefs = {
            "1":{
                'Daft Punk': 0.14490916772285595,
                'Talib Kweli': 0.06337135614702155,
                'Busta Rhymes': 0.05597803126320237,
                'The Roots': 1.0,
                'DJ Shadow': 0.47317279256442757,
                'Beastie Boys': 0.41233629066328686,
                'Cypress Hill': 0.3673426277989016,
                'Mobb Deep': 0.23489649345162653,
                'dead prez': 0.06928601605407689,
                'Nas': 0.3060836501901141,
                'The Coup': 0.08069286016054077,
                'Method Man': 0.2412336290663287,
                'Rage Against the Machine': 0.08005914659907055,
                'Dubfire': 0.05978031263202366,
                'XSI': 0.05175327418673426,
                'CPU': 0.09970426700464723,
                'Jedi Mind Tricks': 0.1394169835234474,
                'Jurassic 5': 0.0817490494296578,
                'Korn': 0.08280523869877482,
                'Dr. Dre': 0.07266582171525138,
                'Astrix': 0.05407689057879172,
                'Raekwon': 0.30523869877482046,
                'Azax Syndrom': 0.4907055344317702,
                'Afrika Bambaataa': 0.09674693705111956,
                'Penta': 0.05217574989438107,
                'Gang Starr': 0.3350232361639206,
                'Gravediggaz': 0.04900718208703,
                'Mos Def': 0.17574989438107308,
                'Wu-Tang Clan': 0.8910012674271229,
                'E-40': 0.07287705956907478,
                'RZA': 0.15800591465990704,
                'Naughty by Nature': 0.05999155048584706,
                'Nelly Furtado': 0.08681875792141952,
                'Digitalism': 0.2171525137304605,
                'Linkin Park': 0.10920997042670047,
                'Rinkadink': 0.07646810308407266,
                'Xeg': 0.2598225602027883,
                'T.I.': 0.053865652724968315,
                'GMS': 0.11829319814110689,
                'Public Enemy': 0.15356991972961553,
                'Klaxons': 0.07646810308407266,
                'Menog': 0.07689057879171948,
                'Peter Bailey & Richie Santana': 0.09759188846641319,
                '1200 Micrograms': 0.05407689057879172,
                'Invisibl Skratch Piklz': 0.08998732572877059,
                'Gorillaz': 0.08766370933671314,
                'Talamasca': 0.3377693282636248,
                'Kanye West': 0.27122940430925224,
                'GZA/Genius': 0.12568652302492606,
                'Sirius Isness': 0.07329953527672159},
            "2": {'Lenny Kravitz': 0.029534606205250596,
                  'Third Eye Blind': 0.03192124105011933,
                  'Tim McGraw': 0.04087112171837709,
                  'Garth Brooks': 0.06861575178997613,
                  'Red Hot Chili Peppers': 0.06980906921241051,
                  'U2': 0.053400954653937946,
                  'Amos Lee': 0.09994033412887827,
                  'Coldplay': 0.3275656324582339,
                  'James Blunt': 0.04087112171837709,
                  'Ray LaMontagne': 0.13544152744630072,
                  'Gavin DeGraw': 0.09994033412887827,
                  'Justin Timberlake': 0.028341288782816228,
                  'Sarah McLachlan': 0.035501193317422436,
                  'Pat McGee Band': 0.057577565632458236,
                  'Damien Rice': 0.05817422434367542,
                  'Creedence Clearwater Revival': 0.03013126491646778,
                  'Lynyrd Skynyrd': 0.05369928400954654,
                  'The Doors': 0.022673031026252982,
                  'Keith Urban': 0.029236276849642005,
                  'Savage Garden': 0.027744630071599045,
                  'Josh Groban': 0.029832935560859187,
                  'The Killers': 0.054295942720763726,
                  'Snow Patrol': 0.14826968973747018,
                  'Beck': 0.04355608591885442,
                  'Matchbox Twenty': 0.052804295942720764,
                  'Journey': 0.02028639618138425,
                  'Timbaland': 0.08532219570405727,
                  'Death Cab for Cutie': 0.2613365155131265,
                  'Hanson': 0.5707040572792362,
                  'OneRepublic': 0.0623508353221957,
                  'Eric Clapton': 0.10441527446300716,
                  'Default': 0.024761336515513127,
                  'Augustana': 0.03400954653937947,
                  'The Fray': 0.08890214797136038,
                  'Foo Fighters': 0.02058472553699284,
                  'The All-American Rejects': 0.03937947494033413,
                  'Averi': 0.02386634844868735,
                  'Dave Matthews Band': 0.25894988066825775,
                  'Ingram Hill': 0.03729116945107398,
                  'Boys Like Girls': 0.0331145584725537,
                  'Jimi Hendrix': 0.04892601431980907,
                  'John Mayer': 1.0,
                  'Yellowcard': 0.029236276849642005,
                  'James Morrison': 0.03967780429594272,
                  'Incubus': 0.07130071599045346,
                  'Goo Goo Dolls': 0.0808472553699284,
                  'OK Go': 0.02356801909307876,
                  'Brandi Carlile': 0.02684964200477327,
                  'Mat Kearney': 0.027446300715990454,
                  'The Hero Factor': 0.028042959427207637},
            "3": {'Daft Punk': 0.29723991507430997,
                  'Good Charlotte': 0.2760084925690021,
                  'Man\xc3\xa1': 0.22717622080679406,
                  'In Fear and Faith': 0.18046709129511676,
                  'Red Hot Chili Peppers': 0.5116772823779193,
                  'Emarosa': 0.2526539278131635,
                  'Avenged Sevenfold': 0.4309978768577495,
                  'Asking Alexandria': 0.15286624203821655,
                  'Rage Against the Machine': 0.23142250530785563,
                  '\xe4\xb8\x8b\xe6\x9d\x91\xe9\x99\xbd\xe5\xad\x90':
                      0.43736730360934184,
                  'Owl City': 0.16772823779193205,
                  'House vs. Hurricane': 0.15286624203821655,
                  'Pierce the Veil': 0.2208067940552017,
                  'Closure In Moscow': 0.5520169851380042,
                  'I Am Ghost': 0.28662420382165604,
                  'At the Drive-In': 0.19957537154989385,
                  'Adept': 0.2059447983014862,
                  'Escape The Fate': 0.39278131634819535,
                  'blink-182': 0.5392781316348195,
                  'Metallica': 0.9596602972399151,
                  'Panic! At the Disco': 0.3651804670912951,
                  'The Word Alive': 0.1613588110403397,
                  'Maximum the Hormone': 0.1762208067940552,
                  'Fall Out Boy': 0.3524416135881104,
                  'A Day to Remember': 0.5159235668789809,
                  'Yellowcard': 0.18683651804670912,
                  'Eyes Set to Kill': 0.34182590233545646,
                  'Cultura Prof\xc3\xa9tica': 0.3524416135881104,
                  'In:aviate': 0.21231422505307856,
                  'Slipknot': 0.46496815286624205,
                  'Disturbed': 0.18259023354564755,
                  'Panda': 0.3970276008492569,
                  'The Beatles': 0.2484076433121019,
                  'New Found Glory': 0.22717622080679406,
                  'Isles & Glaciers': 0.20382165605095542,
                  'Living Language': 0.3205944798301486,
                  'Rise Against': 1.0,
                  'AC/DC': 0.21443736730360935,
                  'Flobots': 0.20382165605095542,
                  'Confide': 0.21231422505307856,
                  'Alesana': 0.32696390658174096,
                  'Fiel a la Vega': 0.22929936305732485,
                  'El Canto del Loco': 0.16985138004246284,
                  'Incubus': 0.21656050955414013,
                  'deadmau5': 0.2632696390658174,
                  'Sum 41': 0.31634819532908703,
                  'Broadway': 0.23991507430997877,
                  'Calle 13': 0.208067940552017,
                  'Chiodos': 0.3630573248407643,
                  'We Came As Romans': 0.1740976645435244}}

        my_ratings = {
            "Daft Punk": 0.3,
            "Busta Rhymes": 0.1,
            "Incubus": 0.7
        }

        test3 = [
            ('Red Hot Chili Peppers', 0.3861040206746221),
            ('Rage Against the Machine', 0.1991741560575475),
            ('Yellowcard', 0.14204855696988627)
        ]

        top3 = get_recommendations(prefs, my_ratings, 2, sim_pearson)[0:3]

        self.assertEqual(len(top3), 3)

        for (name1, score1), (name2, score2) in zip(test3, top3):
            self.assertEqual(name1, name2)
            self.assertAlmostEqual(score1, score2, 4)

if __name__ == '__main__':
    unittest.main()
