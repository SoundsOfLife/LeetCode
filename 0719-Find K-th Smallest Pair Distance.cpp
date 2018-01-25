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
    int smallestDistancePair(vector<int>& nums, int k) {
      sort(nums.begin(),nums.end());
      multiset<int> anw;
      for(int i = 0; i < nums.size() - 1;i++){
        for(int j = i + 1;j < nums.size();j++){
          anw.insert(abs(nums[j] - nums[i]));
        }
      }
      auto it = anw.begin();
      int i = 0;
      while(i < k - 1)i++,it++;
      return *it;
    }
};


int main(int argc, char const *argv[]) {
  /* code */
  Solution solution;
  vector<int> nums = {1,3,1};
  auto anw = solution.smallestDistancePair(nums,0);
  cout << anw << endl;
  return 0;
}
