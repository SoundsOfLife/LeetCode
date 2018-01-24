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
    int lengthOfLongestSubstring(string s) {
        int i = 0, j = 0, anw = 0;
        auto len = s.size();
        deque<int> di;
        map<char, int> mci;
        map<char, int>::iterator iter;
        while (j < len) {
            iter = mci.find(s[j]);
            if (iter != mci.end()) {
                i = iter->second + 1;;
                mci.insert(pair<char, int>(s[j], j));
                anw = di.size() >= anw ? di.size() : anw;
                di.push_back(j);
                while (di.size() > 0 && di.front() < i)di.pop_front();
                mci.clear();
                while (i <= j) {
                    mci.insert(pair<char, int>(s[i], i));
                    i++;
                }
            } else {
                mci.insert(pair<char, int>(s[j], j));
                di.push_back(j);
                anw = di.size() >= anw ? di.size() : anw;
            }
            j++;
        }
        return anw;
    }
};

int main(int argc, char const *argv[]) {
  /* code */

  return 0;
}
