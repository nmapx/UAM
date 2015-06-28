#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int nsym(int n, int k) {
    int i,j;
    int c1=1,c2=1;

    for (i=n-k+1; i<=n; i++) {
        c1 = c1*i;
    }
    if (c1 == 0) {
        c1 = 1;
    }

    for (i=1; i<=k; i++) {
        c2 = c2*i;
    }
    if (c2 == 0) {
        c2 = 1;
    }

    return c1/c2;
}

int main() {
    int i,j;
    int n,k,r,x=1;
    int tab[9999];

    cout << "Podaj n: ";
    cin >> n;

    cout << "Podaj k: ";
    cin >> k;

    cout << "Podaj r: ";
    cin >> r;

    cout << "T = {";
    for (i=1; i<=k; i++) {
        while (nsym(n-x,k-i) <= r) {
            r = r-nsym(n-x,k-i);
            x = x+1;
        }
        tab[i] = x;
        x = x+1;
        ///////////////
        cout << tab[i];
        if (i != k) {
            cout << ",";
        }
    }
    cout << "}";

    return 0;
}
