#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int newt(int n, int k) {
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
    int i,j,c=1,m;
    int b[9999] = {1};

    cin >> m;

    for (i=1; i<=m; i++) {
        b[i] = 0;
        for (j=0; j<=i-1; j++) {
            b[i] += newt(i-1,j)*b[j];
        }
        c++;
    }

    cout << b[c-1];

    return 0;
}

