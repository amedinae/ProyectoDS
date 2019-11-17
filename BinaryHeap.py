import math


class BinaryHeap(object):
    def __init__(self, max_size=0):
        self.max_size = max_size
        self.H = [0]

    def parent(self, i):
        return math.floor(i / 2)

    def leftChild(self, i):
        return 2 * i

    def rightChild(self, i):
        return 2 * i + 1

    def siftUp(self, i):
        while i > 1 and self.H[self.parent(i)][0] < self.H[i][0]:
            self.H[self.parent(i)], self.H[i] = self.H[i], self.H[self.parent(i)]
            i = self.parent(i)

    def siftDown(self, i):
        max_index = i
        l = self.leftChild(i)
        if l <= len(self.H) - 1 and self.H[l][0] > self.H[max_index][0]:
            max_index = l
        r = self.rightChild(i)
        if r <= len(self.H) - 1 and self.H[r][0] > self.H[max_index][0]:
            max_index = r
        if i != max_index:
            self.H[max_index], self.H[i] = self.H[i], self.H[max_index]
            self.siftDown(max_index)

    def insert(self, p, data):
        if len(self.H) - 1 == self.max_size:
            return "ERROR"
        self.H.append([p, data])
        self.siftUp(len(self.H) - 1)

    def extractMax(self):
        result = self.H[1]
        self.H[1] = self.H[len(self.H) - 1]
        self.siftDown(1)
        return result
