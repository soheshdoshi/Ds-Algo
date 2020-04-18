#Given a sorted array of distinct integers A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.
def sumCount(arr,C):
    lenth=len(arr)
    strat_p=0
    end_p=lenth-1
    count=0
    while strat_p<end_p:
        ans=arr[strat_p]+arr[end_p]
        if ans==C:
            count+=1
            strat_p+=1
            end_p-=1
        elif ans<C:
            strat_p+=1
        else:
            end_p-=1
    return count
