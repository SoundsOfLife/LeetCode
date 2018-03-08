def insertSort(nums=[]):
    # TODO
    ret = [nums[0]]
    for i in range(1, len(nums)):
        for j in range(len(ret)):
            if nums[i] < ret[j]:
                ret.insert(j, nums[i])
                break
            if j == len(ret) - 1:
                ret.append(nums[i])
                break
    return ret


def QuickSort(nums=[]):
    # qSort
    def qSort(nums, left, right):
        i = left
        j = right
        if i >= j:
            return nums
        key = nums[i]
        while i < j:
            while i < j and nums[j] >= key:
                j = j - 1
            nums[i] = nums[j]
            while i < j and nums[i] <= key:
                i = i + 1
            nums[j] = nums[i]
            nums[i] = key
        qSort(nums, left, i - 1)
        qSort(nums, j + 1, right)
        return nums

    qSort(nums, 0, len(nums) - 1)
    return nums


def MSort(nums=[]):
    def merge(a, b):
        ret = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                ret.append(a[i])
                i += 1
            else:
                ret.append(b[j])
                j += 1
        ret += b[j:]
        ret += a[i:]
        return ret

    def mSort(nums, left, right):
        if right - left > 1:
            mid = (left + right) // 2
            a = mSort(nums, left, mid)
            b = mSort(nums, mid + 1, right)
            return merge(a, b)
        else:
            return nums[left:right + 1]

    return mSort(nums, 0, len(nums) - 1)


def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int(len(lists) / 2)
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)


def Merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    nums = [1, 10, 2, 5, 8, 7, 6, 4, 3, 0, 9]
    # print(MergeSort(nums))
    # print(MSort(nums))
    print(insertSort(nums))
