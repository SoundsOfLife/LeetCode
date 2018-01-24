#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <deque>
#include <map>

/**
  * a square if and only if each prime factor occurs to an even power in the number's prime factorization.
  * a sum of two squares if and only if each prime factor that's 3 modulo 4 occurs to an even power in the number's prime factorization.
  * a sum of three squares if and only if it's not of the form 4a(8b+7) with integers a and b.
  * a sum of four squares. Period. No condition. You never need more than four.
  **/

using namespace std;

class Solution {
public:
  int numSquares(int n) {
    int ub = sqrt(n);
    for (int a=0; a<=ub; ++a) {
        for (int b=a; b<=ub; ++b) {
            int c = sqrt(n - a*a - b*b);
            if (a*a + b*b + c*c == n)
                return !!a + !!b + !!c;
        }
    }
    return 4;
  }
};


int main(int argc, char const *argv[]) {
  /* code */
  Solution solution;
  auto anw = solution.numSquares(13);
  cout << anw << endl;
  return 0;
}
