class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return -1
        temp = [0, nums[0]]
        for i in range(1, len(nums)):
            temp.append(temp[-1] + nums[i])
        temp.append(0)
        for i in range(0, len(nums)):
            if temp[i] == temp[-2] - temp[i + 1]:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [-1, -1, -1, 0, 1, 1]
    print(s.pivotIndex(nums))
