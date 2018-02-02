class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degree = dict()
        maxDegree = 0
        for i in range(len(nums)):
            degree.setdefault(nums[i], (-1, -1, 0))
            first = degree[nums[i]][0]
            num = degree[nums[i]][2]
            if num == 0:
                degree[nums[i]] = (i, -1, 1)
            elif num == 1:
                degree[nums[i]] = (first, i, 2)
            else:
                degree[nums[i]] = (first, i, num + 1)
            if num + 1 >= maxDegree:
                maxDegree = num + 1
        ans = len(nums)
        if maxDegree == 1:
            return 1
        else:
            for key in degree.keys():
                if degree[key][2] == maxDegree:
                    if degree[key][1] - degree[key][0] + 1 <= ans:
                        ans = degree[key][1] - degree[key][0] + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 3, 0, 4, 1]
    print(s.findShortestSubArray(nums))
