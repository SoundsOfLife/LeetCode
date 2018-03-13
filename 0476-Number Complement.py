class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = bin(num)
        ans = ""
        for i in range(2, len(n)):
            ans = ans + ("1" if n[i] == "0" else "0")
        return int(ans, 2)


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))
