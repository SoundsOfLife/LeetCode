class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for x in [10, 8, 6, 5, 4, 3, 2]:
            while num % x == 0:
                num = num / x
        return num == 1


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(10))
