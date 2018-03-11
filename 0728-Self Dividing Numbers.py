class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right + 1):
            if self.check(i):
                ans.append(i)
        return ans

    def check(self, num):
        temp = num
        while num != 0:
            a = num % 10
            if a == 0 or temp % a != 0:
                return False
            num = num // 10
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.selfDividingNumbers(1, 22))
