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
    char nextGreatestLetter(vector<char>& letters, char target) {
      char anw = 'z' + 1;
      char min = 'z';
      for(auto it = letters.begin(); it != letters.end();it++){
        if(*it <= min){
          min = *it;
        }
        if(*it > target){
          if(*it < anw){
            anw = *it;
          }
        }
      }
      if(anw == 'z' + 1){
        return min;
      }else{
        return anw;
      }
    }
};

int main(int argc, char const *argv[]) {
  /* code */
  vector<char> letters = {'c','f','j'};
  char target = 'c';
  Solution solution;
  auto anw = solution.nextGreatestLetter(letters, target);
  cout << anw << endl;
  return 0;
}
