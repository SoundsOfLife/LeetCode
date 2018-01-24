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
        }else if(nums.size() == 1){
          return nums[0];
        }else if(nums.size() == 2){
          return max(nums[0],nums[1]);
        }else{
          int dp[nums.size()][2];
          // room one was rabbed
          dp[1][0] = nums[0],dp[1][1] = nums[0];
          for(int i = 2;i < nums.size() - 1;i++){
              dp[i][0] = max(dp[i - 1][0],dp[i - 1][1]);
              dp[i][1] = max(dp[i - 1][0] + nums[i],dp[i - 1][1]);
          }
          int temp = max(dp[nums.size() - 2][0],dp[nums.size() - 2][1]);
          // room one didn’t be rabbed
          dp[0][0] = 0,dp[0][1] = 0;
          for(int i = 1;i < nums.size();i++){
              dp[i][0] = max(dp[i - 1][0],dp[i - 1][1]);
              dp[i][1] = max(dp[i - 1][0] + nums[i],dp[i - 1][1]);
          }
          return max(temp, max(dp[nums.size() - 1][0],dp[nums.size() - 1][1]));
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
