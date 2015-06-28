"""Makes recommendations"""

from TaskD01 import load_data
from TaskD03 import sim_pearson
from TaskD04 import get_recommendations

if __name__ == '__main__':
    PREFS = load_data(open("lastfm.dat", 'r'), normalize=True)

    MY_PREFS = {
        "Silverchair": 1,
        "Adele": 0.8,
        "Britney Spears": -0.5,
        "Oasis": 0.7,
        "Nirvana": 0.5,
        "Metallica": -0.4,
        "Depeche Mode": -0.3
    }

    for i, (n, r) in enumerate(get_recommendations(PREFS,
                               MY_PREFS, 3, sim_pearson)[:10]):
        print "%d\t%s\t%.3f" % (i+1, n, r)
