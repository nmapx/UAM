#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main() {
    int i, n, r, counter;
    unsigned t[10000];

    cout << "Podaj range: ";
    cin >> r;

    cout << "Podaj n: ";
    cin >> n;

    i = n;
    counter = 0;
    while (i >= 1) {
        if (r%2 == 1) {
            t[counter] = i;
            counter++;
        }
        r /= 2;
        i--;
    }

    cout << "{";
    for (i=0; i<counter; i++) {
        cout << t[i];
        if (i != counter-1) {
            cout << ",";
        }
    }
    cout << "}";

    return 0;
}
