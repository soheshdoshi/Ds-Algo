import sys
def diff(arr):
    t=0
    for i in range(0,len(arr),2):
        t+=abs(arr[i]-arr[i+1])
    return t
def mySolution(arr):
    lenth=len(arr)
    if lenth<1:
        return 0
    N=lenth//2
    ans=sys.maxsize
    arr.sort()
    for i in range(lenth):
        for j in range(i+1,lenth):
            res=[]
            for k in range(lenth):
                if k==i or k==j:
                    continue
                res.append(arr[k])
            ans=min(ans,diff(res))
    return ans

A = [ 81, 19, 42, 70, 79, 56, 38, 106, 59, 47, 16, 65, 93, 34, 112, 37, 57, 29, 114, 107 ]
print(mySolution(A))
