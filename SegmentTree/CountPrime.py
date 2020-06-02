from math import ceil, floor, log

MAX = 1000000


def sieveOfEratosthenes(isPrime):
    isPrime[1] = False

    for k in range(2, MAX + 1):
        if k * k > MAX:
            break
        if isPrime[k] == True:
            for i in range(2 * k, MAX + 1, k):
                isPrime[i] = False


class SegmentTree:

    def __init__(self, A, isPrime):
        self.size = len(A)
        self.A = A
        self.maxSizeSeg = 2 * pow(2, ceil(log(self.size, 2))) - 1
        self.segTree = [0] * self.maxSizeSeg
        self.isPrime = isPrime
        self.__build_segTree(0, 0, self.size - 1)

    def __build_segTree(self, treeIndex, left, right):
        if left == right:
            if self.isPrime[self.A[left]]:
                self.segTree[treeIndex] = 1
            else:
                self.segTree[treeIndex] = 0
            return self.segTree[treeIndex]
        else:
            mid = left + (right - left) // 2
            self.segTree[treeIndex] = self.__build_segTree(treeIndex * 2 + 1, left, mid) + \
                                      self.__build_segTree(treeIndex * 2 + 2, mid + 1, right)
            return self.segTree[treeIndex]

    def updateValue(self, updateIndex, value):
        if updateIndex < 0 or updateIndex > self.size - 1:
            return
        difference, oldValue = 0, 0
        oldValue = self.A[updateIndex]
        self.A[updateIndex] = value

        # case 1: old and new values both are primes
        if self.isPrime[oldValue] and self.isPrime[value]:
            return
        # case 2: old and new values both non-primes
        if ((not self.isPrime[oldValue])) and (not self.isPrime[value]):
            return

        # case 3: old value was prime , new value is non prime
        if self.isPrime[oldValue] and not self.isPrime[value]:
            difference = -1

        if not self.isPrime[oldValue] and self.isPrime[value]:
            difference = 1

        self.__update_segTree(0, 0, self.size - 1, updateIndex, difference)

    def __update_segTree(self, treeIndex, left, right, updateIndex, difference):

        if updateIndex < left or updateIndex > right:
            return
        self.segTree[treeIndex] = self.segTree[treeIndex] + difference

        if (left != right):
            mid = left + (right - left) // 2
            self.__update_segTree(treeIndex * 2 + 1, left, mid, updateIndex, difference)
            self.__update_segTree(treeIndex * 2 + 2, mid + 1, right, updateIndex, difference)

    def query(self, leftR, rightR):
        return self.__query_segTree(leftR, rightR, 0, 0, self.size - 1)

    def __query_segTree(self, leftR, rightR, treeIndex, left, right):
        if leftR <= left and rightR >= right:
            return self.segTree[treeIndex]
        if right < leftR or left > rightR:
            return 0
        mid = left + (right - left) // 2
        return self.__query_segTree(leftR, rightR, treeIndex * 2 + 1, left, mid) + \
               self.__query_segTree(leftR, rightR, treeIndex * 2 + 2, mid + 1, right)


class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @param C : list of integers
    # @param D : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D):

        isPrime = [True] * (MAX + 1)
        sieveOfEratosthenes(isPrime)

        seg = SegmentTree(A, isPrime)

        result = []
        for i in range(len(B)):
            if B[i] == "C":
                index, value = C[i] - 1, D[i]
                seg.updateValue(index, value)
            else:
                start, end = C[i] - 1, D[i] - 1

                result.append(seg.query(start, end))
        return result
