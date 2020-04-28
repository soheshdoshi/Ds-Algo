from collections import deque

"""
for two queues -- for S and L and then proceed -- capture only indexes
throw the first element if not in index 
capture minimum increasing subsequece and maximum decresing subsequece
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        smallQ = deque()
        largeQ = deque()
        MOD = 1000000007
        for i in range(B):
            # if u have a visuvalization minimum increasing subsequece is captured
            while smallQ and A[smallQ[-1]] >= A[i]:
                smallQ.pop()

            # if u have a visuvalization maximum decresing subsequece is captured
            while largeQ and A[largeQ[-1]] <= A[i]:
                largeQ.pop()

            smallQ.append(i)
            largeQ.append(i)
        # print(smallQ)
        # print(largeQ)
        tot = 0
        for i in range(B, n):
            tot += A[smallQ[0]] + A[largeQ[0]]

            # check whther they are within window size
            while smallQ and smallQ[0] <= i - B:
                smallQ.popleft()
            while largeQ and largeQ[0] <= i - B:
                largeQ.popleft()

            while smallQ and A[smallQ[-1]] >= A[i]:
                smallQ.pop()

            while largeQ and A[largeQ[-1]] <= A[i]:
                largeQ.pop()
            smallQ.append(i)
            largeQ.append(i)
            # print(smallQ)
            # print(largeQ)

        tot += A[smallQ[0]] + A[largeQ[0]]
        return tot % 1000000007