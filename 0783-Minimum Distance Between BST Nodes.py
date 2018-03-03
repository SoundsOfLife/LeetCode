# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math


class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.solve(root)

    def getLeftMax(self, root):
        if root == None:
            return math.inf
        while root.right != None:
            root = root.right
        return root.val

    def getRightMin(self, root):
        if root == None:
            return math.inf
        while root.left != None:
            root = root.left
        return root.val

    def solve(self, root):
        if root != None:
            a = self.solve(root.left)
            b = self.solve(root.right)
            l = self.getLeftMax(root.left)
            r = self.getRightMin(root.right)
            s = min(min(abs(l - root.val), abs(r - root.val)), min(a, b))
            return s
        else:
            return math.inf
