class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int

        The essence of this problem is that 10^n ≡ 1 (mod 9), and thus a_n10^n + … + a_110 + a_0 ≡ a_n + … + a_1 + a_0 (mod 9).
        This process can be continued until a number less than 9 is gotten, i.e. num % 9.
        For any digit n, n = n % 9 unless n = 9.
         The only confusing case is n % 9 = 0, but addDigits(num) = 0 if and only if num = 0, otherwise it should be 9 in fact.
        """
        # return num % 9 if num % 9 != 0 or num == 0 else 9
        return 0 if num == 0 else (num % 9 or 9)

if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))