from collections import defaultdict
def mySolution(A):
    dp=defaultdict(lambda :2)
    s=set(A)
    lenth=len(A)
    for j in range(lenth):
        for i in range(j):
            if A[j]-A[i]<A[i] and A[j]-A[i] in s:
                dp[A[i],A[j]]=dp[(A[j]-A[i],A[i])]+1
    return max(dp.values() or [0])




arr=[1,2,3,4,5,6,7,8]
print(mySolution(arr))

