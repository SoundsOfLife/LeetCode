class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        for i in range(1, N + 1):
            ans += self.check(i)
        return ans

    def check(self, num):
        temp = num
        good = 0
        i = 0
        while num > 0:
            t = 0
            if num % 10 == 0 or num % 10 == 1 or num % 10 == 8:
                t += num % 10
            elif num % 10 == 2:
                t += 5
            elif num % 10 == 5:
                t += 2
            elif num % 10 == 6:
                t += 9
            elif num % 10 == 9:
                t += 6
            else:
                return 0
            t *= pow(10, i)
            good += t
            i += 1
            num = num // 10
        return temp != good


if __name__ == '__main__':
    s = Solution()
    print(s.rotatedDigits(10000))
