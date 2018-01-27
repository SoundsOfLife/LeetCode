class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """


if __name__ == '__main__':
    s = Solution()
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    print(s.findMinHeightTrees(n, edges=edges))
