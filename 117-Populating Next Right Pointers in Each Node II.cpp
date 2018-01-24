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
            while(1){
              before = temp;
              // find before node who has at least one chlid node.
              while(before != NULL && before->left == NULL && before->right == NULL){
                before = before->next;
              }
              if(before == NULL){
                break;
              }else{
                if(before->left != NULL)
                  temp = before->left;
                else
                  temp = before->right;
                // next begin node
                begin = temp;
                // begin node's next node is
                if(before->left != NULL && before->right != NULL){
                  begin->next = before->right;
                  begin = begin->next;
                  before = before->next;
                }else{
                  before = before->next;
                }
                while(before != NULL){
                  if(before->left != NULL){
                    begin->next = before->left;
                    begin = begin->next;
                  }
                  if(before->right != NULL){
                    begin->next = before->right;
                    begin = begin->next;
                  }
                  before = before->next;
                }
              }
            }
         }
      }
};

int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}
