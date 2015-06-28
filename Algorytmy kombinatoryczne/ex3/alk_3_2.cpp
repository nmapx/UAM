#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int t[9999];
int c=0;

int pot2 (int n) {
    int m = 2;
    for (int i=1; i<n; i++) {
        m = m*2;
    }
    return m;
}

void unrank(int r, int n) {
    int v;
    if (n == 1) {
        t[c] = r%2;
        c++;
    } else {
        v = pot2(n-1);
        if (r < v) {
            t[c] = 0;
            c++;
            unrank(r,n-1);
        } else {
            t[c] = 1;
            c++;
            unrank(v-r%v-1,n-1);
        }
    }
}

int main() {
    int r,n,i;

    cout << "Podaj r: ";
    cin >> r;

    cout << "Podaj n: ";
    cin >> n;

    unrank(r,n);

    //////////////////
    for (i=0; i<c; i++) {
        cout << t[i];
    }
    //////////////////

    return 0;
}
