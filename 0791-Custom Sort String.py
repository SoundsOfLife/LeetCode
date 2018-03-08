class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        def cmp(a, b):
            if order[a] > order[b]:
                return False
            else:
                return True

        order = {}
        for i in range(len(S)):
            order[S[i]] = i
        ret = [T[0]]
        for i in range(1, len(T)):
            for j in range(len(ret)):
                if order.get(T[i]) is None:
                    ret.append(T[i])
                    break
                if order.get(ret[j]) is None:
                    if j == len(ret) - 1:
                        ret.append(T[i])
                        break
                    continue
                if order[T[i]] < order[ret[j]]:
                    ret.insert(j, T[i])
                    break
                if j == len(ret) - 1:
                    ret.append(T[i])
        ans = ""
        for i in ret:
            ans += i
        return ans


if __name__ == '__main__':
    s = Solution()
    S = "exv"
    T = "xwvee"
    print(s.customSortString(S, T))
