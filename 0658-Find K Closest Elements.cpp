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
      vector<int> findClosestElements(vector<int>& arr, int k, int x) {
          int min = abs(arr[0] - x);
          int minIndex = 0;
          for(int i = 0; i < arr.size();i++){
            if(abs(arr[i] - x) <= min){
              min = abs(arr[i] - x);
              minIndex = i;
            }
          }
          if(k == 1){
            vector<int> anw;
            anw.push_back(arr[minIndex]);
            return anw;
          }else{
            int flag = minIndex - k + 1 >= 0 ? minIndex - k + 1:0;
            while(flag + k < arr.size() && abs(x - arr[flag]) > abs(arr[flag + k] - x))flag++;
            vector<int> anw(arr.begin() + flag, arr.begin() + flag + k);
            return anw;
          }
      }

      /*
      vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size() - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (x - arr[mid] > arr[mid+k] - x) left = mid + 1;
            else right = mid;
        } //find left, don't care too much about right
        return vector<int>(arr.begin() + left, arr.begin() + left + k);
      }
      */
};

int main(int argc, char const *argv[]) {
  /* code */
  vector<int> arr = {1};
  Solution solution;
  auto anw = solution.findClosestElements(arr,1,0);
  cout << anw[0] << endl;
  return 0;
}
