#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

unsigned long long f(unsigned long long n, unsigned long long k) {
    int i,j,m;
    int *a;

    m = n-k;
    a = new int[m+1];

    for (i= 0; i<=m; i++) {
        a[i] = 1;
    }

    for (i=2; i<=k; i++) {
        for(j=1; j<=m; j++) {
            a[j] += i*a[j-1];
        }
    }

    return a[m];
}

int main() {
    int n,k;

    cout << "Podaj n: ";
    cin >> n;

    cout << "Podaj k: ";
    cin >> k;

    cout << f(n,k);

    return 0;
}
