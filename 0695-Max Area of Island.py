class Solution:
    def __init__(self):
        self.areas = set()
        self.rows = 0
        self.cols = 0

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.rows = len(grid)
        self.cols = len(grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    self.areas.add((i, j))
        ans = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1 and (i, j) in self.areas:
                    self.areas.remove((i, j))
                    temp = 1 + self.check(grid, i + 1, j) + self.check(grid, i - 1, j) + self.check(grid, i,
                                                                                                j - 1) + self.check(
                        grid, i, j + 1)
                    if temp >= ans:
                        ans = temp
        return ans

    def check(self, grid, x, y):
        if x == -1 or x == self.rows or y == -1 or y == self.cols:
            return 0
        elif grid[x][y] == 1 and (x, y) in self.areas:
            self.areas.remove((x, y))
            return 1 + self.check(grid, x + 1, y) + self.check(grid, x - 1, y) + self.check(grid, x,
                                                                                            y + 1) + self.check(grid, x,
                                                                                                                y - 1)
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    # data = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    data = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(s.maxAreaOfIsland(data))
