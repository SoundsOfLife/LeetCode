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

class MapSum {
public:
    /** Initialize your data structure here. */
    map<string,int> msi;
    MapSum() {

    }

    void insert(string key, int val) {
      if(msi.count(key) == 0)
        msi.insert(pair<string,int>(key, val));
      else
        msi.find(key)->second = val;
    }

    int sum(string prefix) {
      int anw = 0;
      for(auto it = msi.begin();it != msi.end();it++){
          string key = it->first;
          if(key.substr(0,prefix.size()) == prefix){
            anw += it->second;
          }
      }
      return anw;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */

int main(int argc, char const *argv[]) {
  /* code */
  MapSum obj;
  string key = "apple";
  string prefix = "a";
  int val = 2;
  obj.insert(key,val);
  int param_2 = obj.sum(prefix);
  cout << param_2 << endl;
  return 0;
}
