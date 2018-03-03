class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.ans = True
        self.flag = [0 for i in range(len(graph))]
        self.flag[0] = 1

        g = [set() for i in range(len(graph))]
        for i in range(len(graph)):
            indexs = graph[i]
            for j in indexs:
                g[i].add(j)
                g[j].add(i)

        s = [list(i) for i in g]

        for i in range(len(graph)):
            self.DFS(i, s, self.flag[i])

        return self.ans

    def DFS(self, node, graph, f):
        if f == 0:
            f = 1
        for i in graph[node]:
            if self.flag[i] == f:
                self.ans = False
                break
            elif self.flag[i] == 0:
                self.flag[i] = -1 * f
                self.DFS(i, graph, -1 * f)


if __name__ == '__main__':
    s = Solution()
    print(s.isBipartite(
        [[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14], [], [10], [], [10], [19], [18], [],
         [16], [15], [23], [23], [], [20, 21], [], [], [27], [26], [], [], [34], [33, 34], [], [31], [30, 31], [38, 39],
         [37, 38, 39], [36], [35, 36], [35, 36], [43], [], [], [40], [], [49], [47, 48, 49], [46, 48, 49], [46, 47, 49],
         [45, 46, 47, 48]]))
    print(s.isBipartite(
        [[1], [0], [4], [4], [2, 3]]))
