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
      string toHex(int num) {
        map<int,char> mci = {{0,'0'},{1,'1'},{2,'2'},{3,'3'},{4,'4'},{5,'5'},{6,'6'},{7,'7'},{8,'8'},{9,'9'},{10,'a'},{11,'b'},{12,'c'},{13,'d'},{14,'e'},{15,'f'}};
        String anw = "";
        for(auto i = 0;i < num.size();i++){

        }
      }
};

int main(int argc, char const *argv[]) {
  /* code */
  int num = 26;
  Solution solution;
  auto anw = solution.toHex(num);
  cout << anw << endl;
  return 0;
}
