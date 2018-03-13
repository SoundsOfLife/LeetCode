class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        i, j = 0, 0
        for k in moves:
            if k == "U":
                i += 1
            elif k == "D":
                i -= 1
            elif k == "L":
                j -= 1
            elif k == "R":
                j += 1
        return i == 0 and j == 0
        # return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


if __name__ == '__main__':
    s = Solution()
    print(s.judgeCircle("UD"))
