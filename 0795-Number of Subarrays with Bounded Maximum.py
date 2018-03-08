class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        big = []
        for i in range(len(A)):
            if A[i] > R:
                big.append(i)
        if len(big) == 0:
            LR = []
            for i in range(len(A)):
                if L <= A[i] <= R:
                    LR.append(i)
            return self.cal(LR, 0, len(A) - 1)
        else:
            LR = []
            for i in range(big[0]):
                if L <= A[i] <= R:
                    LR.append(i)
            ans += self.cal(LR, 0, big[0] - 1)
            for i in range(len(big) - 1):
                temp = []
                for j in range(big[i] + 1, big[i + 1]):
                    if L <= A[j] <= R:
                        temp.append(j)
                ans += self.cal(temp, big[i] + 1, big[i + 1] - 1)
            LR = []
            for i in range(big[-1] + 1, len(A)):
                if L <= A[i] <= R:
                    LR.append(i)
            ans += self.cal(LR, big[-1] + 1, len(A) - 1)
            return ans

    def cal(self, nums, left, right):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return (right - nums[0] + 1) * (nums[0] - left + 1)
        else:
            flag = -1
            loc = -1
            for i in range(len(nums)):
                if nums[i] > flag:
                    flag = nums[i]
                    loc = i
            return self.cal(nums[:loc], left, flag - 1) + self.cal(nums[loc:], flag + 1, right) + (right - flag + 1) * (
                flag - left + 1)


if __name__ == '__main__':
    s = Solution()
    A = [7, 3, 6, 7, 1]
    L = 1
    R = 4
    print(s.numSubarrayBoundedMax(A, L, R))
