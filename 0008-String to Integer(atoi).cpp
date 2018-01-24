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
      int myAtoi(string str) {
        int i = 0;
        long long anw = 0;
        while(i < str.size() && str[i] == ' ')i++;

        if(i == str.size()){
          return 0;
        }else{
          if(str[i] == '+'){
            i++;
            int j = i;
            while(j < str.size() && str[j] <= '9' && str[j] >= '0')j++;
            for(int k = i;k < j;k++){
              anw *= 10;
              if(anw >= INT_MAX){
                return INT_MAX;
              }
              anw += (str[k] - '0');
              if(anw >= INT_MAX){
                return INT_MAX;
              }
            }
            return anw;
          }else if(str[i] == '-'){
            i++;
            int j = i;
            long long flag = INT_MAX;
            while(j < str.size() && str[j] <= '9' && str[j] >= '0')j++;
            for(int k = i;k < j;k++){
              anw *= 10;
              if(anw >= flag + 1){
                return INT_MIN;
              }
              anw += (str[k] - '0');
              if(anw >= flag + 1){
                return INT_MIN;
              }
            }
            return -1 * anw;
          }else if(str[i] > '9' || str[i] < '0'){
            return 0;
          }else{
            int j = i;
            while(j < str.size() && str[j] <= '9' && str[j] >= '0')j++;

            for(int k = i;k < j;k++){
              anw *= 10;
              if(anw >= INT_MAX){
                return INT_MAX;
              }
              anw += (str[k] - '0');
              if(anw >= INT_MAX){
                return INT_MAX;
              }
            }
            return anw;
          }
        }
      }
};

int main(int argc, char const *argv[]) {
  /* code */
  Solution solution;
  string str = "    -1231231231231312313123123  ";
  auto anw = solution.myAtoi(str);
  cout << anw << endl;
  return 0;
}
