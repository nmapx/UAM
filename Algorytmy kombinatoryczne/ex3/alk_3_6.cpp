#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int k;
unsigned t[9999];
int r = 0;

void unshift() {
    int i;
    for (i=k; i>=0; i--) {
        t[i] = t[i-1];
    }
    t[0] = 0;
}

int nsym(int n, int k) {
    int i,j;

    int c1 = 1;
    for (i=n-k+1; i<=n; i++) {
        c1 = c1*i;
    }
    if (c1 == 0) {
        c1 = 1;
    }

    int c2 = 1;
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
    int n;

    cout << "Podaj n: ";
    cin >> n;

    cout << "Podaj liczbe elementow zbioru T: ";
    cin >> k;

    cout << "Wprowadz kolejno elementy zbioru T:\n";
    for (i=0; i<k; i++) {
        cin >> t[i];
    }
    unshift();

    for (i=1; i<=k; i++) {
        if (t[i-1]+1 <= t[i]-1) {
            for (j=t[i-1]+1; j<= t[i]-1; j++) {
                r = r+nsym(n-j,k-i);
            }
        }
    }

    cout << "Ranga: " << r;

    return 0;
}
