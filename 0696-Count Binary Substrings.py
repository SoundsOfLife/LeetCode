class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        if len(s) == 0:
            return 1
        ans = 0
        nums = []
        num = 1
        for i in range(1, len(s) - 1):
            if s[i] == s[i - 1]:
                num += 1
            else:
                nums.append(num)
                num = 1
        if s[-1] == s[-2]:
            nums.append(num + 1)
        else:
            nums.append(num)
            nums.append(1)
        for i in range(len(nums) - 1):
            ans += min(nums[i], nums[i + 1])
        return ans
'''
Better Ways 
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(s, s[1:]))
'''

if __name__ == '__main__':
    s = Solution()
    print(s.countBinarySubstrings("00110"))
