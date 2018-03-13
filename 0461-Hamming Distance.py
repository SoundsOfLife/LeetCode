class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = x ^ y
        ans = str(bin(ret))
        num = 0
        for i in range(2, len(ans)):
            if ans[i] == "1":
                num += 1
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
