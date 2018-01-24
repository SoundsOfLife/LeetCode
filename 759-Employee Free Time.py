class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        anw = schedule[0]
        for l in schedule[1:]:
            anw += l
        anw = sorted(anw, key=lambda item: item.start)

        j = 0
        while j < anw.__len__() - 1:
            if anw[j + 1].start <= anw[j].end:
                anw[j].end = max(anw[j + 1].end, anw[j].end)
                anw.remove(anw[j + 1])
            else:
                j += 1
        return [[anw[i].end, anw[i + 1].start] for i in range(anw.__len__() - 1)]


if __name__ == "__main__":
    A = [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]]
    sol = Solution()
    print(sol.employeeFreeTime(A))
