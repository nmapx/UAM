#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main() {
    int i,j;
    int n,c,k,tmp;
    int t[9999],u[9999];

    cout << "Podaj n: ";
    cin >> n;

    cout << "Podaj liczbe elementow zbioru T: ";
    cin >> c;

    cout << "Wprowadz kolejno elementy zbioru T:\n";
    for (i=0; i<c; i++) {
        cin >> tmp;
        t[i] = tmp;
        u[i] = tmp;
    }

    k = c-1;
    i = k;

    while (i >= 0 && t[i] == n-k+i) {
        i--;
    }

    if (i != -1) {
        for (j=i; j<=k; j++) {
            u[j] = t[i]+1+j-i;
        }
        ////////////////
        cout << "Nastepnik: {";
        for (j=0; j<c; j++) {
            cout << u[j];
            if (j != k) {
                cout << ",";
            }
        }
        cout << "}";
        ////////////////
    } else {
        cout << "Brak!";
    }

    return 0;
}
