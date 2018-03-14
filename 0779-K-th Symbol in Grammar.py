class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1 or K == 1:
            return 0
        else:
            t = self.kthGrammar(N - 1, K // 2 + (0 if K % 2 == 0 else 1))
            return t if K % 2 == 1 else 1 - t


if __name__ == '__main__':
    s = Solution()
    print(s.kthGrammar(4, 1))
    print(s.kthGrammar(4, 2))
    print(s.kthGrammar(4, 3))
    print(s.kthGrammar(4, 4))
    print(s.kthGrammar(4, 5))
    print(s.kthGrammar(4, 6))
