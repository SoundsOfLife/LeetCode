class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "A"
        else:
            ans = ""
            while n > 1:
                ans += chr(n % 27 + 64)
                n = (n // 26)
            return ans[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(27))
