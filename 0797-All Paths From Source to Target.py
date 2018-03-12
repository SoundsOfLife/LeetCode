class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.DFS(graph, 0, [])
        return self.ans

    def DFS(self, graph, node, nodes):
        if node == len(graph) - 1:
            nodes.append(node)
            self.ans.append(nodes)
        else:
            nodes.append(node)
            for i in graph[node]:
                if i not in nodes:
                    import copy
                    self.DFS(graph, i, copy.copy(nodes))


if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))
