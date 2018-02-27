class Solution(object):
    def letterCasePermutation(self, S):
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bits in range(1 << B):
            b = 0
            word = []
            for letter in S:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            ans.append("".join(word))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation("a1b2"))
