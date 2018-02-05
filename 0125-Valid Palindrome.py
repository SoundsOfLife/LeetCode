class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = ""
        for i in s:
            if i.isdigit() or i.isupper() or i.islower():
                ss += i
        ss = ss.lower()
        return ss == ss[::-1]


if __name__ == '__main__':
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(s))
