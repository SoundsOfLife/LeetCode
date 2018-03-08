class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K == 0:
            return 5

        min = 1
        max = K * 5
        while min < max:
            mid = (min + max) // 2
            if self.cal(mid) < K:
                min = mid + 1
            else:
                max = mid

        if self.cal(min) != K:
            return 0
        else:
            return 5

    def cal(self, num):
        ans = 0
        five = 5
        while five <= num:
            ans += (num // five)
            five *= 5
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.preimageSizeFZF(10))
