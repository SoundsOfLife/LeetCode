class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        sum = 8
        ans = [0, 1, 2, 5]
        for i in range(4, N + 1):
            ans.append(2 * sum - ans[-1] - ans[-2] + 2)
            sum += ans[-1]
        return ans[N] % int(1e9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.numTilings(4))
