import math


class MaxHeap:
    def __init__(self):
        self.heap = [math.inf]
        self.length = 0

    def insert(self, val):
        self.length += 1
        self.heap.append(val)
        temp = self.length
        while self.heap[temp // 2] < val:
            self.heap[temp] = self.heap[temp // 2]
            temp = temp // 2
        self.heap[temp] = val

    def deleteMax(self):
        self.length -= 1
        maxValue = self.heap[1]
        lastValue = self.heap[-1]
        temp = 1
        self.heap.pop(1)
        while temp * 2 <= self.length:
            temp = temp * 2 if self.heap[temp * 2] > self.heap[temp * 2 + 1] else temp * 2 + 1
        self.heap[temp] = lastValue
        return maxValue


class MinHeap:
    def __init__(self):
        self.heap = [-1 * math.inf]
        self.length = 0

    def insert(self, val):
        self.length += 1
        self.heap.append(val)
        temp = self.length
        while self.heap[temp // 2] > val:
            self.heap[temp] = self.heap[temp // 2]
            temp = temp // 2
        self.heap[temp] = val

    def deleteMin(self):
        self.length -= 1
        minValue = self.heap[1]
        lastValue = self.heap[-1]
        self.heap.pop(1)
        temp = 1
        while temp * 2 <= self.length:
            temp = temp * 2 if self.heap[temp * 2] < self.heap[temp * 2 + 1] else temp * 2 + 1
        self.heap[temp] = lastValue
        return minValue


if __name__ == '__main__':
    textMax = MaxHeap()
    textMax.insert(100)
    textMax.insert(200)
    textMax.insert(3000)
    textMax.insert(1200)
    textMax.insert(1300)
    textMax.insert(5000)
    textMax.insert(600)
    textMax.insert(9000)
    print(textMax.heap)
    textMax.deleteMax()
    print(textMax.heap)
