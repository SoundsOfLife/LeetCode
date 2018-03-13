class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        numA = a.split("+")
        numB = b.split("+")
        numA = [int(numA[0]), int(numA[1][:-1])]
        numB = [int(numB[0]), int(numB[1][:-1])]
        return str(numA[0] * numB[0] - numA[1] * numB[1]) + "+" + str(numB[0] * numA[1] + numB[1] * numA[0]) + "i"


if __name__ == '__main__':
    s = Solution()
    a, b = "1+-1i", "1+-1i"
    print(s.complexNumberMultiply(a, b))
