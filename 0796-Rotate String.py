class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    A = 'abc'
    B = 'cab'
    print(s.rotateString(A, B))
