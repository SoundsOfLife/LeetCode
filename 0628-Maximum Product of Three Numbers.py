class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 6:
            ans = nums[0] * nums[1] * nums[2]
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    for k in range(j + 1, len(nums)):
                        ans = max(ans, nums[i] * nums[j] * nums[k])
            return ans
        else:
            max1, max2, max3 = -1000, -1000, -1000
            min1, min2, min3 = 1000, 1000, 1000
            for i in nums:
                if i >= max1:
                    max3 = max2
                    max2 = max1
                    max1 = i
                elif i >= max2:
                    max3 = max2
                    max2 = i
                elif i >= max3:
                    max3 = i
                if i <= min1:
                    min3 = min2
                    min2 = min1
                    min1 = i
                elif i <= min2:
                    min3 = min2
                    min2 = i
                elif i <= min3:
                    min3 = i
            return self.maximumProduct([min1, min2, min3, max3, max2, max1])


if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([-600, -2, 3, 4, 5]))
