#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int pot2 (int n) {
    int m = 2;
    for (int i=1; i<n; i++) {
        m = m*2;
    }
    return m;
}

int main() {
    int i,j;
    int r=0,b=0,n,k,t[9999];

    cout << "Podaj n: ";
    cin >> n;

    cout << "Podaj liczbę elementow w zbiorze T: ";
    cin >> k;

    cout << "Wprowadz kolejno elementy zbioru T:\n";
    for (i=0; i<k; i++) {
        cin >> t[i];
    }

    for (i=n-1; i>=0; i--) {
        for (j=0; j<k; j++) {
            if (t[j] == n-i) {
                b = 1-b;
                break;
            }
        }
        if (b == 1) {
            r = r+pot2(i);
        }
    }

    cout << "Ranga podzbioru: " << r;

    return 0;
}
