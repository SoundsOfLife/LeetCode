class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x})
                       for x in X
                       if x % i == 0 or i % x == 0)

        return count(N, set(range(1, N + 1)))


if __name__ == '__main__':
    s = Solution()
    print(s.countArrangement(2))
