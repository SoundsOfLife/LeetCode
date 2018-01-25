class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        nums = dict()
        if (len(s) < 10):
            return []
        else:
            for i in range(len(s) - 9):
                nums.setdefault(s[i:i + 10], 0)
                nums[s[i:i + 10]] += 1
        return [i for i in nums.keys() if nums[i] >= 2]

if __name__ == '__main__':
    s = "AAAAAAAAAAA"
    solution = Solution()
    print(solution.findRepeatedDnaSequences(s))
