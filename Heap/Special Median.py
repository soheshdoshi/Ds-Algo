from heapq import heappush,heappop,heappushpop

def addNum(num,large,small):
    if len(small) == len(large):
        heappush(large, -heappushpop(small, -num))
    else:
        heappush(small, -heappushpop(large, num))

def findMedian(small,large):
    if len(small) == len(large):
        return float(large[0] - small[0]) / 2.0
    else:
        return float(large[0])

def mySolution(arr):
    larg=[]
    smal=[]
    lenth=len(arr)
    flag=False
    for i in range(lenth-1):
        addNum(arr[i],larg,smal)
        if findMedian(smal,larg) == arr[i+1]:
            return 1
    larg=[]
    smal=[]
    for i in range(lenth-1,0,-1):
        addNum(arr[i],larg,smal)
        if findMedian(smal,larg) ==arr[i-1]:
            return 1
    return 0
print(mySolution([2, 7, 3, 1]))
# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         return mySolution(A)

