'''
寻找第k大的数
'''


def FindMinK(nums, k, left, right):
    def partition(nums, left, right):
        temp = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] > temp:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] < temp:
                i += 1
            nums[j] = nums[i]
        nums[i] = temp
        return i

    t = partition(nums, left, right)
    if t == k - 1:
        return nums[k - 1]
    elif t > k - 1:
        return FindMinK(nums, k, left, t - 1)
    elif t < k - 1:
        return FindMinK(nums, k, t + 1, right)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 7, 8, 9, 5, 6, 0]
    print(FindMinK(nums, 7, 0, len(nums) - 1))
