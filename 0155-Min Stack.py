class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.nums.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.nums.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.nums)



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
