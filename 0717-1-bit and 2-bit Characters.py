class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 2:
            i += 2 if bits[i] == 1 else 1
        return False if bits[i] == 1 else True


if __name__ == '__main__':
    s = Solution()
    bits = [1, 0, 0]
    print(s.isOneBitCharacter(bits))
