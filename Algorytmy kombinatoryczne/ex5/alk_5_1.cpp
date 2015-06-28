#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <iostream>

using namespace std;

int *podzial(int blok[9999], int n) {
    int i;
    int t[9999][9999];

    for (i=1; i<=n; i++) {
        t[blok[i]-1][i] = i;
    }

    return t;
}

int main() {
    int i,j;
    int n,k;

    cout << "Podaj n: ";
    cin >> n;

    j=n;
    int nast[9999],poprz[9999],blok[9999];
    bool pr[9999];

    for (i=0; i<n; i++) {
        blok[i] = 1;
        pr[i] = true;
    }

    nast[1] = 0;

    cout << podzial(blok, n) << " - " << j; //wyswietlenie - element aktywny

    while (j>1) {
        k = blok[j];
        if (pr[j] == true) {
            if (nast[k] == 0) {
                nast[k] = j;
                poprz[j] = k;
                nast[j] = 0;
            } else {
                if (nast[k] > j) {
                    poprz[j] = k;
                    nast[j] = nast[k];
                    poprz[nast[j]] = j;
                    nast[k] = j;
                }
            }
            blok[j] = nast[k];
        } else {
            blok[j] = poprz[k];
            if (k == j) {
                if (nast[k] == 0) {
                    nast[poprz[k]] = 0;
                } else {
                    nast[poprz[k]] = nast[k];
                    poprz[nast[k]] = poprz[k];
                }
            }
        }

        cout << podzial(blok, n) << " - " << j; //wyswietlenie - element aktywny

        j=n;
        while (j>1 && (pr[j]==true && blok[j]==j) || (pr[j]==false && blok[j]==1)) {
            pr[j] = !pr[j];
            j = j-1;
        }
    }

    return 0;
}
