class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        t = N * [1]
        n = []
        for i in range(N):
            n.append(t.copy())
        for i in mines:
            n[i[0]][i[1]] = 0
        print(n)

if __name__ == "__main__":
    N = 5
    mines = [[4, 2]]
    sol = Solution()
    anw = sol.orderOfLargestPlusSign(N, mines)
    print(anw)
