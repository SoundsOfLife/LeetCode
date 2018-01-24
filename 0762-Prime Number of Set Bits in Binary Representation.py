from math import sqrt


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        anw = 0
        for i in range(L, R + 1):
            s = str(bin(i))
            count = s.count('1')
            if self.primer(count):
                anw += 1
        return anw

    @staticmethod
    def primer(self, n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True


if __name__ == "__main__":
    sol = Solution()
    anw = sol.countPrimeSetBits(244, 269)
    print(anw)
