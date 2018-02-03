class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for j in range(rowIndex):
            # ans = [1] + [ans[i] + ans[i + 1] for i in range(len(ans) - 1)] + [1]
            ans = list(map(lambda x, y: x + y, [0] + ans, ans + [0]))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
