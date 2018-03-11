class Solution:
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = []
        dp.append([0] * (k + 1))
        dp.append([1] + [0] * k)
        for i in range(2, n + 1):
            temp = [1]
            for j in range(1, k + 1):
                if j < i:
                    temp.append((temp[-1] + dp[-1][j]) % 1000000007)
                else:
                    temp.append((temp[-1] + dp[-1][j] - dp[-1][j - i]) % 1000000007)
            dp.append(temp)
        return dp[n][k]


if __name__ == '__main__':
    s = Solution()
    print(s.kInversePairs(40, 9))
