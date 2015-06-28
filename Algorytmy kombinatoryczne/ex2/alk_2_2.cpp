#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int i, n, r, c;
    unsigned podzb[10000];

    cout << "Podaj n: ";
    cin >> n;

    cout << "Zdefiniuj liczbe elementow w podzbiorze: ";
    cin >> c;

    cout << "Wprowadz kolejno elementy podzbioru:\n";
    for (i=0; i<c; i++) {
        cin >> podzb[i];
    }

    r = 0;
    for (i=0; i<2; i++) {
        r += pow(2, n-podzb[i]);
    }

    cout << "\nPozycja wprowadzonego podzbioru: " << r;

    return 0;
}
