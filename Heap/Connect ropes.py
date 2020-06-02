import heapq
def mySolution(arr):
    max_sum=0
    heapq.heapify(arr)
    while len(arr)!=1:
        ele1=heapq.heappop(arr)
        elem2=heapq.heappop(arr)
        sum_e=ele1+elem2
        max_sum+=sum_e
        heapq.heappush(arr,sum_e)
    return max_sum


A=[1,2,3,4,5]
mySolution(A)