class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        step1 = 0
        step2 = 0
        one = []
        zero = []
        for i in range(len(board[0])):
            if board[0][i] == 1:
                one.append(i)
            else:
                zero.append(i)
        print(one)
        print(zero)
        if len(one) != len(zero):
            return -1
        else:
            order1 = []
            order2 = []
            for i in range(len(one)):
                order1.append(one[i])
                order1.append(zero[i])
                order2.append(zero[i])
                order2.append(one[i])
            for i in range(len(order1)):
                if i != order1[i]:
                    step1 += 1
                if i != order2[i]:
                    step2 += 1

            

if __name__ == '__main__':
    s = Solution()
    print(s.movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]))
