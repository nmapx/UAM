#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

unsigned tab[99999];

int potega(int n) {
    int pot = 1;
    while (0 < n--) {
        pot = pot+pot;
    }
    return pot;
}

void kod(int n) {
    int pot, i;

    if (n != 1) {
        kod(n-1);
        pot = potega(n-1);
        i = pot;
        while (i < 2*pot) {
            tab[i] = tab[2*pot-i-1]+pot;
            i++;
        }
    } else {
        tab[0] = 0; tab[1] = 1;
    }
}

void podzbiory(int n) {
    int i = 0, j = 0, c = 0;
    unsigned kod;
    string str;

    cout << "\nPodzbiory: \n";
    while (i < potega(n)) {
        cout << "{";
        c = 0;
        str = "";
        kod = tab[i];
        j = 1;
        while (j <= n) {
            str = (char) (kod%2+48)+str;
            kod = kod/2;
            j++;
        }
        j = 0;
        while (j < n) {
            if (str[j] == '1') {
                if (c != 0) {
                    cout << ",";
                }
                cout << j+1;
                c++;
            }
            j++;
        }
        cout << "}\n";
        i++;
    }
}

int main() {
    int n;

    cout << "Podaj n: ";
    cin >> n;

    if (n>=1 && n<=16) {
        kod(n);
        podzbiory(n);
    }

    return 0;
}
