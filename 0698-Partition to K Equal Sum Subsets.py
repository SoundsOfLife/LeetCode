class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = sum(nums)
        nums = sorted(nums)
        print(nums)
        if sums % k != 0:
            return False
        else:
            s = sums % k


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(s.canPartitionKSubsets(nums=nums, k=k))
