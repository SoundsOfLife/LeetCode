class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n > 0:
            num = n % 27
            ans += chr(int(num) + 64)
            n = n // 26
        return ans[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(53))
