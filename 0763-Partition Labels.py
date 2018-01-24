class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        temp = S[::-1]
        anw = []
        i = 0
        while i != length:
            j = i
            m = length - temp.find(S[i]) - 1
            while i != m:
                t = length - temp.find(S[i]) - 1
                if t >= m:
                    m = t
                i += 1
            anw.append(m - j + 1)
            i += 1

        return anw


if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    sol = Solution()
    anw = sol.partitionLabels(s)
    print(anw)
