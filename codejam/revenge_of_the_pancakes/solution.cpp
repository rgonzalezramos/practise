#include <iostream>
#include <sstream>

#define HAPPY '+'
#define BLANK '-'

using namespace std;


int solve(string input) {
    int len = input.length();
    
    int flips = 0;
    char top_stack = input.at(0);

    for (int i = 1; i < len; i++) {
        char pancake = input.at(i);

        if (top_stack != pancake) {
            flips += 1;
        }

        top_stack = pancake;
    }

    if (top_stack == BLANK) {
        flips += 1;
    }

    return flips;
}


int main(int argc, char** argv) {
    int nlines;
    
    cin >> nlines;
    for (int i = 0; i < nlines; i++) {
        string input;
        cin >> input;
        cout << "Case #" << i + 1 << ": " << solve(input) << "\n";
    }

    return 0;
}
