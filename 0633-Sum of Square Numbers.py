class Solution:
    def judgeSquareSum(self, c):
        def is_square(N):
            return int(N ** .5) ** 2 == N

        return any(is_square(c - a * a)
                   for a in range(int(c ** .5) + 1))


if __name__ == '__main__':
    s = Solution()
    print(s.judgeSquareSum(1000000))
