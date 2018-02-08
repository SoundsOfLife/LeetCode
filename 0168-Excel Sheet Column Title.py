class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n > 0:
            if n % 27 != 0:
                ans += chr(n % 27 + 64)
            else:
                ans += chr(n % 26 + 64)
            n = (n // 26)
        return ans[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(26))
