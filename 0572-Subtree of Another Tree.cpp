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
    bool isSubtree(TreeNode* s, TreeNode* t) {
      if(s == NULL)
        return isSameTree(s, t);
      else if(s->left != NULL && s->right != NULL)
        return isSameTree(s,t) || isSubtree(s->left, t) || isSubtree(s->right, t);
      else if(s->left == NULL && s->right == NULL)
        return isSameTree(s,t);
      else if(s->left == NULL && s->right != NULL)
        return isSameTree(s,t) || isSubtree(s->right, t);
      else if(s->left != NULL && s->right == NULL)
        return isSameTree(s,t) || isSubtree(s->left, t);
      else
        return isSameTree(s,t);
    }

    bool isSameTree(TreeNode* s,TreeNode* t){
      if(s == NULL && t == NULL){
        return true;
      }else if(s != NULL && t != NULL){
        if(s->val == t->val)
          return isSameTree(s->right,t->right) && isSameTree(s->left,t->left);
      }
      return false;
    }
};

int main(int argc, char const *argv[]) {
  /* code */

  return 0;
}
