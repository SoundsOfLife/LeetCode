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

/**
 * Definition for a binary tree node.
 *
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int rob(TreeNode* root) {
        return max(robbed(root,true),robbed(root,false));
    }

    int robbed(TreeNode* root,bool flag){
      if(root == NULL){
        return 0;
      }else if(root->left == NULL && root->right == NULL){
        if(flag){
          return 0;
        }else{
          return root->val;
        }
      }else if(root->left == NULL){
        int temp = robbed(root->right,false);
        if(flag){
          return temp;
        }else{
          return max(temp,robbed(root->right,true) + root->val);
        }
      }else if(root->right == NULL){
        int temp = robbed(root->left,false);
        if(flag){
          return temp;
        }else{
          return max(temp,robbed(root->left,true) + root->val);
        }
      }else{
        int temp = robbed(root->left, false) + robbed(root->right,false);
        if(flag){
          // don't rob root
          return temp;
        }else{
          // rob root
          return max(temp,robbed(root->left,true) + robbed(root->right,true) + root->val);
        }
      }
    }
};

int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}
