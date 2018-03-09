class DisjSet:
    def __init__(self, nums):
        # S中的每个下标i的值及S[i] 表示该节点的父节点下标,根节点的父节点是-1
        # 用S记录树深度的负值
        self.S = [-1] * nums

    def Find(self, x):

        # 可以进行路径压缩
        if self.S[x] < 0:
            return x
        else:
            self.S[x] = self.Find(self.S[x])
            return self.S[x]

    def SetUnion(self, root1, root2):
        # 简单但是效率不高的方法 容易产生深度过大的树
        # self.S[root1] = root2

        # 按照大小合并 小的合并到大的上面 深度不会超过 log N

        # 按照高度合并 矮的合并到高的上面去 深度最多 log N
        # 代码类似上面 只不过S记录的是树的深度的负数
        if self.S[root1] < self.S[root2]:
            self.S[root2] = root1
        else:
            if self.S[root1] == self.S[root2]:
                self.S[root1] -= 1
            self.S[root2] = root1


if __name__ == '__main__':
    # 并查集实现
    demo = DisjSet(100)
    print(demo.Find(10))
    demo.SetUnion(5, 6)
    demo.SetUnion(7, 10)
    demo.SetUnion(6, 7)
    print(demo.Find(10))
