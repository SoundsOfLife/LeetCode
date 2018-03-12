# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        else:
            left = self.getMin(root.left, root.val)
            right = self.getMin(root.right, root.val)
            if left == -1:
                return right
            elif right == -1:
                return left
            else:
                return min(left, right)

    def getMin(self, node, num):
        if node is None:
            return -1
        else:
            if node.val != num:
                return node.val
            else:
                a = self.getMin(node.left, num)
                b = self.getMin(node.right, num)
                if a == -1:
                    return b
                elif b == -1:
                    return a
                else:
                    return min(a, b)
