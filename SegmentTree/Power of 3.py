def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y % 2):
            res = (res * x) % p
        y = y // 2
        x = (x * x) % p
    return res


def modInverse(a, m):
    return power(a, m - 2, m)


class SegmentTree:
    bit = []
    mod = []

    def __init__(self, A, comparision):
        self.A = A
        self.size = len(A)
        self.maxSizeSeg = self.size * 4
        self.bit = [0] * self.maxSizeSeg
        self.mod = [0] * self.maxSizeSeg
        self.func = comparision
        self.build(0, 0, len(A) - 1)


# build segment tree
    def build(self, treeIndex, left, right):
        bit = self.bit
        mod = self.mod
        global n
        if (left > right):
            return

        if (left == right):
            bit[treeIndex] = ord(self.A[left]) - ord('0')
            mod[treeIndex] = bit[treeIndex] * power(2, self.size - 1 - right, 3)
            return
        else:
            mid = (left + right) // 2
            self.build(treeIndex * 2 + 1, left, mid)
            self.build(treeIndex * 2 + 2, mid + 1, right)
            mod[treeIndex] = (mod[treeIndex * 2 + 1] + mod[treeIndex * 2 + 2]) % 3


    # update to handle updates
    def updateValue(self, updateIndex, value):
        self.__update_segTree(0, 0, self.size - 1, updateIndex, value)


    def __update_segTree(self, treeIndex, left, right, updateIndex, value):
        # r = l
        bit = self.bit
        mod = self.mod

        if (left > updateIndex or updateIndex > right or left > right):
            return

        if (left >= updateIndex and right <= updateIndex):
            bit[treeIndex] = 1
            mod[treeIndex] = bit[treeIndex] * power(2, self.size - 1 - right, 3)
            return
        else:
            mid = (left + right) // 2
            self.__update_segTree(treeIndex * 2 + 1, left, mid, updateIndex, value)
            self.__update_segTree(treeIndex * 2 + 2, mid + 1, right, updateIndex, value)
            mod[treeIndex] = (mod[treeIndex * 2 + 1] + mod[treeIndex * 2 + 2]) % 3;


    def query(self, left, right):
        return self.__query_segTree(0, self.size - 1, 0, left, right)


    def __query_segTree(self, leftR, rightR, treeIndex, left, right):
        # print(treeIndex,leftR,rightR,left,right)
        bit = self.bit
        mod = self.mod
        if (leftR > rightR or leftR > right or rightR < left):
            return 0
        if (leftR >= left and rightR <= right):
            return mod[treeIndex]
        else:
            mid = (leftR + rightR) // 2
            leftSegment = self.__query_segTree(leftR, mid, 2 * treeIndex + 1, left, right)
            rightSegment = self.__query_segTree(mid + 1, rightR, 2 * treeIndex + 2, left, right)
            return (leftSegment + rightSegment) % 3


class Solution:
    def solve(self, A, B):
    # global n
        n = len(A)
        seg = SegmentTree(A, lambda a, b: a + b)
        ans = []
        for i in range(0, len(B)):
            if (B[i][0] == 0):
                l = B[i][1] - 1
                r = B[i][2] - 1
                val = seg.query(l, r)
                val = (val * modInverse(power(2, n - 1 - r, 3), 3)) % 3
                ans.append(val)
            else:
                seg.updateValue(B[i][1] - 1, 1)
                ans.append(-1)
        return ans

s=Solution.solve()