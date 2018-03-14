class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        x, o = 0, 0
        for i in board:
            for j in i:
                if j == "X":
                    x += 1
                elif j == "O":
                    o += 1
        if x == o or x == o + 1:
            flag = [0, 0, 0, 0, 0, 0, 0, 0]
            if board[0][0] == board[1][1] == board[2][2]:
                if board[0][0] == "X":
                    flag[0] = 1
                elif board[0][0] == "O":
                    flag[0] = -1
            if board[0][2] == board[1][1] == board[2][0]:
                if board[0][2] == "X":
                    flag[4] = 1
                elif board[0][2] == "O":
                    flag[4] = -1
            for i in range(1, 4):
                if board[0][i - 1] == board[1][i - 1] == board[2][i - 1]:
                    if board[0][i - 1] == "X":
                        flag[i] = 1
                    elif board[0][i - 1] == "O":
                        flag[i] = -1
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2]:
                    if board[i][0] == "X":
                        flag[i + 5] = 1
                    elif board[i][0] == "O":
                        flag[i + 5] = -1
            print(flag)
            if flag.count(1) == 0 and flag.count(-1) == 0:
                return True
            else:
                if x == o:
                    if flag.count(1) != 0:
                        return False
                    else:
                        if flag.count(-1) == 1:
                            return True
                        else:
                            if flag[1] + flag[2] + flag[3] <= -2 or flag[5] + flag[6] + flag[7] <= -2:
                                return False
                            else:
                                return True
                elif x == o + 1:
                    if flag.count(-1) != 0:
                        return False
                    else:
                        if flag.count(1) == 1:
                            return True
                        else:
                            if flag[1] + flag[2] + flag[3] >= 2 or flag[5] + flag[6] + flag[7] >= 2:
                                return False
                            else:
                                return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.validTicTacToe(board=["XXX", "OOX", "OOX"]))
