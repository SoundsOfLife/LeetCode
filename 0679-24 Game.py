import itertools

import math


class Soution:
    def judgePoint24(self, nums):
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        return any(self.judgePoint24([x] + rest)
                   for a, b, *rest in itertools.permutations(nums)
                   for x in {a + b, a - b, a * b, b and a / b})


if __name__ == '__main__':
    s = Soution()
    print(s.judgePoint24([8, 8, 8, 8]))
