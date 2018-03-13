class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum([nums[i] if i % 2 == 0 else 0 for i in range(len(nums))])


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum([1, 4, 3, 2]))
