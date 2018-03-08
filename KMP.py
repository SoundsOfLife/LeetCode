def PartialMatchTable(pattern):
    k = []
    for i in range(len(pattern)):
        t = i
        while True:
            if pattern[:t] == pattern[i - t + 1:i + 1]:
                k.append(t)
                break
            else:
                t -= 1
            if t == 0:
                k.append(0)
                break
    return k


def KMP(target, pattern):
    k = PartialMatchTable(pattern)
    i = 0
    while i < len(target):
        j = 0
        while i + j < len(target) and j < len(pattern) and target[i + j] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i
        else:
            if j == 0:
                i += 1
            else:
                i += (j - k[j])
    return -1


if __name__ == '__main__':
    print(KMP("abababbbbababac", "ababaca"))
