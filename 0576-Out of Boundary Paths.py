class Solution:
    def __init__(self):
        self.P = 1000000007

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or i >= m:
            return 1
        elif j < 0 or j >= n:
            return 1

        if min(i, m - 1 - i) + 1 > N and min(j, n - 1 - j) + 1 > N:
            return 0

        if N > 0:
            return (self.findPaths(m, n, N - 1, i + 1, j) % self.P  + self.findPaths(m, n, N - 1, i, j + 1) % self.P + self.findPaths(m, n, N - 1, i - 1, j) % self.P + self.findPaths(m, n, N - 1, i, j - 1) % self.P) % self.P
        else:
            return 0

if __name__ == '__main__':
    solution = Solution()
    m = 1
    n = 3
    N = 3
    i = 0
    j = 1
    print(solution.findPaths(m, n, N, i, j))
