class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # Solution by DP
        # ans = 0
        # dp = [[0] * (len(A) + 1)] * (len(B) + 1)
        # for i in range(len(A) + 1):
        #     for j in range(len(B) + 1):
        #         if i == 0 or j == 0:
        #             dp[i][j] = 0
        #         elif A[i - 1] == B[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #             ans = max(ans, dp[i][j])
        #         else:
        #             dp[i][j] = 0
        # return ans

        ##############
        ans = 0
        if len(A) < len(B):
            A, B = B, A
        for i in range(len(A) + len(B)):
            if i < len(B):
                c1 = A[:i]
                c2 = B[len(B) - i:]
                ans = max(ans, self.compare(c1, c2))
            elif len(B) <= i < len(A):
                c1 = A[i - len(B):i]
                c2 = B
                ans = max(ans, self.compare(c1, c2))
            else:
                c1 = A[i - len(B):]
                c2 = B[:len(A) + len(B) - i]
                ans = max(ans, self.compare(c1, c2))
        return ans

    def compare(self, c1, c2):
        ans = 0
        t = 0
        for i in range(len(c1)):
            if c1[i] == c2[i]:
                t += 1
                ans = max(ans, t)
            else:
                t = 0
        return ans


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(s.findLength(A, B))
