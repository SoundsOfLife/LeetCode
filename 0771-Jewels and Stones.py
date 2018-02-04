class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(1 for i in list(S) if i in list(J))


if __name__ == '__main__':
    s = Solution()
    J = "z"
    S = "ZZ"
    print(s.numJewelsInStones(J, S))
