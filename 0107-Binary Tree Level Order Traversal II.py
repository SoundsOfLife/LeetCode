class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root is not None:
            ans.append([root.val, ])
            floorNodes = [root, ]
            while 1:
                temp = []
                floorValues = []
                for node in floorNodes:
                    if node.left is not None:
                        temp.append(node.left)
                        floorValues.append(node.left.val)
                    if node.right is not None:
                        temp.append(node.right)
                        floorValues.append(node.right.val)
                if len(temp) != 0:
                    ans.append(floorValues)
                    floorNodes = temp
                else:
                    break

        ans.reverse()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.levelOrderBottom())
