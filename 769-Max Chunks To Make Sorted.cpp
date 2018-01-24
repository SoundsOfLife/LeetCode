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
      int maxChunksToSorted(vector<int>& arr) {
        vector<int> copy(arr);
        sort(copy.begin(),copy.end());
        map<int,int> mii;
        map<int,int> m;
        bool f = true;
        int i = 0,j= 0,anw = 0;
        while(i != arr.size() && j != arr.size()){
          if(f){
            mii.clear();
            m.clear();
              if(mii.count(arr[i]) == 0){
                mii.insert(pair<int,int>(arr[i],1));
              }else{
                mii.find(arr[i])->second = mii[arr[i]] + 1;
              }
              if(m.count(copy[i]) == 0){
                m.insert(pair<int,int>(copy[i],1));
              }else{
                m.find(copy[i])->second = m[copy[i]] + 1;
              }
          }else{
            if(mii.count(arr[j]) == 0){
              mii.insert(pair<int,int>(arr[j],1));
            }else{
              mii.find(arr[j])->second = mii[arr[j]] + 1;
            }
            if(m.count(copy[j]) == 0){
              m.insert(pair<int,int>(copy[j],1));
            }else{
              m.find(copy[j])->second = m[copy[j]] + 1;
            }
          }
          if(mii == m){
            anw++;
            j++;
            i = j;
            f = true;
          }else{
            j++;
            f = false;
          }
        }
        return anw;
      }
};


int main(int argc, char const *argv[]) {
  /* code */
  vector<int> arr = {1,0,2,3,4};
  Solution solution;
  auto anw = solution.maxChunksToSorted(arr);
  cout << anw << endl;
  return 0;
}
