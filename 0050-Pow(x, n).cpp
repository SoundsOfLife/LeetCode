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
    double myPow(double x, int n) {
      if(n < 0){
        if(n == INT_MIN){
          return myPow(x, n + 2) * myPow(x, 2);
        }else
          return 1.0 / myPow(x, -1 * n);
      }else if(n == 1){
        return x;
      }else if(n > 0){
        double temp = myPow(x, n / 2);
        return temp * temp * myPow(x, n % 2);
      }else{
        return 1.0;
      }
    }
};

int main(int argc, char const *argv[]) {
  /* code */
  Solution solution;
  double x = 1.00000;
  int n = -2147483648;
  auto anw = solution.myPow(x, n);
  cout << anw << endl;
  return 0;
}
