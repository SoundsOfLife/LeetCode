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
      int rob(vector<int>& nums) {
        if(nums.size() == 0){
          return 0;
        }else{
          int dp[nums.size()][2];
          dp[0][0] = 0,dp[0][1] = nums[0];
          for(int i = 1;i < nums.size();i++){
              dp[i][0] = max(dp[i - 1][0],dp[i - 1][1]);
              dp[i][1] = max(dp[i - 1][0] + nums[i],dp[i - 1][1]);
          }
          return max(dp[nums.size() - 1][0],dp[nums.size() - 1][1]);
        }
      }
};

int main(int argc, char const *argv[]) {
  /* code */
  vector<int> nums = {1,2,3,4,5};
  Solution solution;
  auto anw = solution.rob(nums);
  cout << anw << endl;
  return 0;
}
