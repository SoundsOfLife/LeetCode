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
    vector<int> twoSum(vector<int> &nums, int target) {
        vector<int> anw;
        map<int, int> mii;
        map<int, int>::iterator iter, solve;
        for (int i = 0; i < nums.size(); i++) {
            mii.insert(pair<int, int>(nums[i], i));
        }
        if (target % 2 == 0 && mii.find(target / 2) != mii.end()) {
            for (int i = 0; i < nums.size(); i++) {
                if (nums[i] == target / 2) {
                    anw.push_back(i);
                }
            }
            if (anw.size() >= 2) {
                vector<int> tt(anw.begin(), anw.begin() + 2);
                return tt;
            }
        }
        anw.clear();
        for (iter = mii.begin(); iter != mii.end(); iter++) {
            map<int, int> m = mii;
            m.erase(iter->first);
            solve = m.find(target - iter->first);
            if (solve != m.end()) {
                anw.push_back(iter->second);
                anw.push_back(solve->second);
                break;
            }
        }
        return anw;
    }
};

int main(int argc, char const *argv[]) {
  /* code */

  return 0;
}
