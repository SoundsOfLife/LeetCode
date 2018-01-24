from operator import itemgetter


class Solution:
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        data = sorted(intervals, key=itemgetter(0, 1))
        flag = 0
        while flag < data.__len__() - 1:
            if data[flag + 1][0] >= data[flag][0] and data[flag + 1][1] <= data[flag][1]:
                data.remove(data[flag])
                if flag > 0:
                    flag -= 1
            else:
                flag += 1
        print(data)
        anw = {data[0][1] - 1, data[0][1]}
        for i in data:
            num = 0
            for j in anw:
                if num >= 2:
                    break
                else:
                    if i[0] <= j <= i[1]:
                        num += 1
            if num == 0:
                anw.add(i[1] - 1)
                anw.add(i[1])
            elif num == 1:
                anw.add(i[1])
        return anw.__len__()


if __name__ == "__main__":
    demo = [[1, 3], [4, 9], [0, 10], [6, 7], [1, 2], [0, 6], [7, 9], [0, 1], [2, 5], [6, 8]]
    intervals = [[2, 10], [3, 7], [3, 15], [4, 11], [6, 12], [6, 16], [7, 8], [7, 11], [7, 15], [11, 12]]
    test = [[1, 3], [7, 10], [5, 9], [5, 8], [6, 7], [0, 3], [5, 8], [3, 4], [6, 10], [4, 6]]
    fuck = [[0, 3], [0, 4], [0, 9], [8, 9], [0, 7], [1, 4], [6, 10], [0, 4], [3, 7], [6, 8]]
    go = [[1, 24], [10, 16], [14, 25], [0, 18], [16, 17]]
    sol = Solution()
    print(sol.intersectionSizeTwo(go))
