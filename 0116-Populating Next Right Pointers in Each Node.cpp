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
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
struct TreeLinkNode {
  int val;
  TreeLinkNode *left, *right, *next;
  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};

class Solution {
  public:
      void connect(TreeLinkNode *root) {
          if(root != NULL){
            TreeLinkNode* temp = (TreeLinkNode*)malloc(sizeof(TreeLinkNode));
            TreeLinkNode* begin = (TreeLinkNode*)malloc(sizeof(TreeLinkNode));
            TreeLinkNode* before = (TreeLinkNode*)malloc(sizeof(TreeLinkNode));
            temp = root;
            while(temp->left != NULL){
              before = temp;
              temp = temp->left;
              // next begin node
              begin = temp;
              // begin node's next node is
              begin->next = before->right;
              before = before->next;
              begin = begin->next;
              while(before != NULL){
                begin->next = before->left;
                begin = begin->next;
                begin->next = before->right;
                before = before->next;
                begin = begin->next;
              }
            }
         }
      }
};

int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}
