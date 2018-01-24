#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <deque>
#include <map>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long anw = 0, k = x;
        if (x < 0) {
            x = x * -1;
        }
        while (x != 0) {
            anw = anw * 10 + x % 10;
            x = x / 10;
        }
        if (k < 0) {
            anw = anw * -1;
        }

        if (anw > INT_MAX || anw < INT_MIN) {
            return 0;
        } else {
            return anw;
        }
    }
};

int main(int argc, char const *argv[]) {
  /* code */

  return 0;
}
