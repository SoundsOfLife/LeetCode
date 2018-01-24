#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <set>
#include <map>

using namespace std;

class Solution {
  public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        bool anw = true;
        int m = matrix.size();
        int n = matrix[0].size();
        for(auto j = 0;j < m;j++){
          for(auto k = 0;k + j < n && k < m;k++){
            if(matrix[k][j+k] != matrix[0][j]){
              anw = false;
              return anw;
            }
          }
        }
        for(auto j = 0;j < n;j++){
          for(auto k = 0;k + j < m && k < n;k++){
            if(matrix[j+k][k] != matrix[j][0]){
              anw = false;
              return anw;
            }
          }
        }
        return anw;
    }
};

int main(){
  vector<vector<int>> v;
  v.push_back({1,2,3,4});
  v.push_back({5,1,2,3});
  v.push_back({9,5,1,2});
  Solution solution;
  auto anw = solution.isToeplitzMatrix(v);
  cout << anw << endl;
}
