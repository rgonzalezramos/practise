#include <iostream>
#include <sstream>

using namespace std;

string solve(long initial) {
    if (initial == 0) {
        return "INSOMNIA";
    }

    int missing_digits = 10;
    int* seen_digits = (int*) calloc(10, sizeof(int));

    long multiplier = 1;
    long number = initial;
    long acc;

    while (true) {
        number = multiplier * initial;
        acc = number;

        while (acc > 0) {
            int digit = acc % 10;
            if (seen_digits[digit] == 0) {
                seen_digits[digit] = 1;
                missing_digits--;
            }
            acc = acc / 10;
        }

        if (missing_digits == 0) {
            return to_string(number);
        }

        multiplier += 1;
    }
}

int main(int argc, char** argv) {
    int nlines;
    
    cin >> nlines;
    for (int i = 0; i < nlines; i++) {
        int input;
        cin >> input;
        cout << "Case #" << i << " " << solve(input) << "\n";
    }
    return 0;
}
