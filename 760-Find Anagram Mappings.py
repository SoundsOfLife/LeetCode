class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        return [B.index(a) for a in A]


if __name__ == "__main__":
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    sol = Solution()
    print(sol.anagramMappings(A, B))
