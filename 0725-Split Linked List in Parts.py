# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import copy


class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        nodes = []
        length = 0
        temp = root
        while temp is not None:
            nodes.append(temp)
            length += 1
            temp = temp.next
        ans = []
        nums = length // k
        more = length % k
        for i in range(k):
            ans.append(nodes[])


if __name__ == '__main__':
    s = Solution()
    r1 = ListNode(1)
    r2 = ListNode(2)
    r3 = ListNode(3)
    r4 = ListNode(4)
    r1.next = r2
    r2.next = r3
    r3.next = r4
    r4.next = None
    s = Solution()
    print(7 // 3)
    s.splitListToParts(r1, 5)
