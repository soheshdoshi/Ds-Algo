def mySolution(arr,mod):
    lenth=len(arr)
    arr.sort()
    min_sum=0
    max_sum=0
    for i in range(lenth):
        max_sum=2*max_sum+arr[lenth-1-i]
        max_sum%=mod
        min_sum=2*min_sum+arr[i]
        min_sum%=mod
    return (max_sum-min_sum)%mod

