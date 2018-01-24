class Solution:
    def __init__(self):
        self.signs = ("(", ")", "+", "-", "*", "/")

    def analyzeExpression(self, s):
        ret = []
        begin = 0
        for i in range(len(s)):
            if s[i] == " ":
                if begin != i:
                    ret.append(s[begin:i])
                begin = i + 1
            elif s[i] in self.signs:
                if begin != i:
                    ret.append(s[begin:i])
                ret.append(s[i])
                begin = i + 1
            elif i == len(s) - 1:
                ret.append(s[begin:])
        return ret

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = self.analyzeExpression(s)
        s1 = ["#"]
        s2 = []
        for i in li:
            if i == "(":
                s1.append(i)
            elif i == ")":
                while s1[-1] != "(":
                    s2.append(s1[-1])
                    s1.pop()
                s1.pop()
            elif i == "*" or i == "/":
                while s1[-1] == "*" or s1[-1] == "/":
                    s2.append(s1[-1])
                    s1.pop()
                s1.append(i)
            elif i == "+" or i == "-":
                while s1[-1] == "+" or s1[-1] == "-" or s1[-1] == "*" or s1[-1] == "/":
                    s2.append(s1[-1])
                    s1.pop()
                s1.append(i)
            else:
                s2.append(i)

        if len(s1) != 0:
            s1.reverse()
            s2 += s1
        s2.reverse()
        value = []
        while len(s2) != 0:
            if s2[-1] in self.signs:
                a = int(value[-1])
                value.pop()
                b = int(value[-1])
                value.pop()
                if s2[-1] == "+":
                    value.append(a + b)
                elif s2[-1] == "-":
                    value.append(b - a)
                elif s2[-1] == "*":
                    value.append(a * b)
                elif s2[-1] == "/":
                    value.append(b // a)
            else:
                value.append(s2[-1])
            s2.pop()
        return int(value[0])
