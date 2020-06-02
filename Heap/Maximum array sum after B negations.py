import sys
import heapq

def mySolution(arr,B):
    heapq.heapify(arr)
    while B:
        change_min=-(heapq.heappop(arr))
        heapq.heappush(arr,change_min)
        #heapq.heapify(arr)
        B-=1
    return sum(arr)


A = [24, -68, -29, -9, 84]
B = 4

mySolution(A,B)
