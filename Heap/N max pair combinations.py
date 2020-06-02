import heapq
from builtins import reversed


def mySolution(A,B):
    lenth=len(A)
    A=sorted(A,reverse=True)
    B = sorted(B, reverse=True)
    result=[]
    heap=[]
    visited=((0,0))
    heapq.heappush(heap,(-(A[0]+B[0]),(0,0)))
    for _ in range(lenth):
        sum,(index_A,index_B)=heapq.heappop(heap)
        result.append(-sum)
        tuple1=(index_A+1,index_B)

        tuple2=(index_A,index_B+1)




class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        visited = set()
        A = sorted(A, reverse=True)
        B = sorted(B, reverse=True)
        result = []
        heap = []
        visited.add((0, 0))
        heapq.heappush(heap, (-(A[0] + B[0]), (0, 0)))
        for _ in range(N):
            sum, (iA, iB) = heapq.heappop(heap)
            result.append(-sum)

            tuple1 = (iA + 1, iB)
            if iA < N - 1 and tuple1 not in visited:
                heapq.heappush(heap, (-(A[iA + 1] + B[iB]), tuple1))
                visited.add(tuple1)

            tuple2 = (iA, iB + 1)
            if iB < N - 1 and tuple2 not in visited:
                heapq.heappush(heap, (-(A[iA] + B[iB + 1]), tuple2))
                visited.add(tuple2)

        return result