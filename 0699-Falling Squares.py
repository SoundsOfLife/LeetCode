class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = [positions[0][1]]
        height = [(positions[0][0], positions[0][0] + positions[0][1], positions[0][1])]
        for sq in positions[1:]:
            pass

if __name__ == '__main__':
    s = Solution()
    pos = [[1, 2], [2, 3], [6, 1]]
    print(s.fallingSquares(pos))
