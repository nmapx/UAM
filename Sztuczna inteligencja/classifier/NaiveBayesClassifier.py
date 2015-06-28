# encoding: utf-8

"""Program do testowania naiwnego klasyfikatora bayesowskiego."""

import glob
import re

import NaiveBayes
from Task801 import train
from Task805 import classify

def getwords(docname):
    """Wyznacza zbiór cech (słów)."""
    doc = open(docname).read()
    splitter = re.compile('\\W*')
    words = [s for s in splitter.split(doc)]
    return set(words)

def category(name):
    """Zwraca etykietę kategorii."""
    if "spm" in name:
        return "SPAM"
    else:
        return "NO-SPAM"

def cross_eval(directory, parts, verbose=False):
    """Dokonuje sprawdzenia krzyżowego."""
    correct = 0
    total = 0

    for i in range(1, parts+1):
        testlist = []
        trainlist = []
        for j in range(1, parts+1):
            if i == j:
                testlist.extend(glob.glob("%s/part%d/*" % (directory, j)))
            else:
                trainlist.extend(glob.glob("%s/part%d/*" % (directory, j)))

        classifier = NaiveBayes.NaiveBayes(getwords)

        if verbose:
            print i, "\tTraining classifier"
        for doc in trainlist:
            train(classifier, doc, category(doc))

        if verbose:
            print "\tClassifying"
        for doc in testlist:
            bestcat = classify(classifier, doc)
            if verbose:
                print "\t", doc, ":", bestcat, "-",
            if bestcat == category(doc):
                if verbose:
                    print "correct"
                correct += 1
            else:
                if verbose:
                    print "wrong"
            total += 1

    return float(correct)/float(total)

if __name__ == '__main__':
    ACCURACY = cross_eval("mailbox", 10, True)
    print "Accuracy:", ACCURACY
