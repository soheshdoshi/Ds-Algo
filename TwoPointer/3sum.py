
#Given an array A of N integers, find three integers in A such that the sum is closest to a given number B. Return the sum of those three integers. Assume that there will only be one solution.

import  sys
def closetSum(arr,B):
    if len(arr)<4:
        return sum(arr)
    arr.sort()
    closetsum=sys.maxsize
    for i in range(len(arr)-2):
        strat_p=i+1
        end_p=len(arr)-1
        while strat_p<end_p:
            ans=arr[i]+arr[strat_p]+arr[end_p]
            diff=abs(B-ans)
            if diff==0:
                return ans
            if diff<closetsum:
                closetsum=diff
                result=ans
            if ans<=B:
                strat_p+=1
            else:
                end_p-=1
    return result

A =[ 10, 1, 6, 10, -4, 1, -3, -10, -7, 10, -2, -5, 1, 7, -1, 7, -9, -7, 5, -2, 7, -1, -1, 10, 6, 0, -2, 9, 5, -9, 4, 8, 3, -6, -7, 0, 9, 3, 0, -10, 3, 7, -9, 10, -4, 7, 2, 1, -9, 3, 10, 4, 0, -2, -5, -4, 9, 10, 8, 7, 2, 1, 0, 3, 4, 7, 4, -3, 0, 8, -1 ]
B=-1
print(closetSum(A,B))
