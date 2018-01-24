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
      int deleteAndEarn(vector<int>& nums) {
          if(nums.size() == 0){
            return 0;
          }
          map<int, int> mii;
          for(auto it = nums.begin();it != nums.end(); it++){
              if(mii.count(*it) == 0){
                mii.insert(pair<int,int>(*it,1));
              }else{
                mii.find(*it)->second += 1;
              }
          }
          vector<pair<int,int>> vii;
          for(auto it = mii.begin(); it != mii.end();it++){
            vii.push_back(pair<int,int>(it->first,it->first * it->second));
          }
          int dp[vii.size() + 1][2];
          dp[0][0] = 0,dp[0][1] = vii[0].second;

          for(auto i = 1; i < vii.size(); i++){
            if(vii[i].first == vii[i - 1].first + 1){
              dp[i][0] = max(dp[i - 1][0],dp[i - 1][1]);
              dp[i][1] = dp[i - 1][0] + vii[i].second;
            }else{
              dp[i][0] = max(dp[i - 1][0],dp[i - 1][1]);
              dp[i][1] = max(dp[i - 1][0] + vii[i].second,dp[i - 1][1] + vii[i].second);
            }
          }
          return max(dp[vii.size() - 1][0],dp[vii.size() - 1][1]);
      }
};
int main(int argc, char const *argv[]) {
  /* code */
  vector<int> nums = {};
  Solution solution;
  auto anw = solution.deleteAndEarn(nums);
  cout << anw << endl;
  return 0;
}
