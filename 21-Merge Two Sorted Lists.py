class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 if l2 is None else l2
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l = l1
        while 1:
            if l2 is None:
                return l
            elif l1.next is None:
                l1.next = l2
                return l
            else:
                if l1.next.val >= l2.val >= l1.val:
                    t = l2.next
                    l2.next = l1.next
                    l1.next = l2
                    l2 = t
                else:
                    l1 = l1.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    sol = Solution()
    t = sol.mergeTwoLists(l1, l2)
    # t = l1
    while t is not None:
        print(t.val)
        t = t.next
