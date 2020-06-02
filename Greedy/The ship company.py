from heapq import heappop,heappush
def mySolution(A,B,C):
    max_heap=[]
    min_heap=[]
    max_cost=0
    min_cost=0
    for i in range(B):
        heappush(max_heap,-C[i])
        heappush(min_heap, C[i])
    for i in range(A):
        max_pop=-heappop(max_heap)
        max_cost+=max_pop
        if max_pop-1>0:
            heappush(max_heap,-(max_pop-1))
        min_pop=heappop(min_heap)
        min_cost+=min_pop
        if min_pop-1>0:
            heappush(min_heap,(min_pop-1))
    return [max_cost,min_cost]


A = 4
B = 3
C = [2, 1, 1]
mySolution(A,B,C)

