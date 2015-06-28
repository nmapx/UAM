#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

unsigned long long f(unsigned long long n, unsigned long long k) {
    if (k > n || k == 0) {
        return 0;
    } else if (n == k) {
        return 1;
    } else {
        return (n-1)*f(n-1,k)+f(n-1,k-1);
    }
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
