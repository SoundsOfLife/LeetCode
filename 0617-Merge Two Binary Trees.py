# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        elif t1 is not None and t2 is not None:
            temp = TreeNode(t1.val + t2.val)
            temp.left = self.mergeTrees(t1.left, t2.left)
            temp.right = self.mergeTrees(t1.right, t2.right)
            return temp
        else:
            if t1 is None:
                temp = TreeNode(t2.val)
                temp.left = self.mergeTrees(t2.left, None)
                temp.right = self.mergeTrees(t2.right, None)
                return temp
            if t2 is None:
                temp = TreeNode(t1.val)
                temp.left = self.mergeTrees(t1.left, None)
                temp.right = self.mergeTrees(t1.right, None)
                return temp
