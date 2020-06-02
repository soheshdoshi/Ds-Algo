import heapq
import math
mod=(10**9)+7
def mySolution(A,B):
    max_ans=0
    for i in range(len(A)):
        A[i]=-A[i]
    heapq.heapify(A)
    for i in range(B):
        el=abs(heapq.heappop(A))
        max_ans+=el
        heapq.heappush(A,-(el//2))
    return max_ans%mod


A=[6,5]
B=3
print(mySolution(A,B))