class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        init = []
        initSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        possible = []
        for row in board:
            for i in row:
                r = []
                s = []
                if i == '.':
                    r.append(0)
                    s.append(initSet)
                else:
                    r.append(int(i))
                    s.append(set())
                init.append(r)
                possible.append(s)
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    