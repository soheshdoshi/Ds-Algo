#Given n non-negative integers A[0], A[1], ..., A[n-1] , where each represents a point at coordinate (i, A[i]). N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water. Note: You may not slant the container.
import sys
def maximumContainer(arr):
    lenth=len(arr)
    if lenth<2:
        return 0
    maxC = -sys.maxsize - 1
    strat_p=0
    end_p=lenth-1
    while strat_p<end_p:
        maxC=max(maxC,min(arr[strat_p],arr[end_p])*(end_p-strat_p))
        if arr[strat_p]<arr[end_p]:
            strat_p+=1
        else:
            end_p-=1
    return maxC

    # for i in range(lenth-1):
    #     for j in range(i+1,lenth):
    #         maxC=max(min(arr[i],arr[j])*(j-i),maxC)
    # return maxC


A = [1,5,4,3]
print(maximumContainer(A))