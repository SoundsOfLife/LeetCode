class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        s = [(c, i) for i, c in enumerate(start) if c == 'L' or c == 'R']
        e = [(c, i) for i, c in enumerate(end) if c == 'L' or c == 'R']
        return len(s) == len(e) and all(
            c1 == c2 and (i1 >= i2 and c1 == 'L' or i1 <= i2 and c1 == 'R') for (c1, i1), (c2, i2) in zip(s, e))


if __name__ == '__main__':
    s = Solution()
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    print(s.canTransform(start, end))
