import sys
def mySolution(arr,a,b,c):
    lenth=len(arr)
    left=[0]*lenth
    left[0]=arr[0]*a
    for i in range(1,lenth):
        if i>=lenth-2:
            left[i]=left[i-1]
        else:
            left[i]=max(left[i-1],arr[i]*a)
    print(left)
    right=[0]*lenth
    right[lenth-1]=arr[lenth-1]*c
    for i in range(lenth-2,-1,-1):
        right[i]=max(right[i+1],right[i]*c)
    print(right)
    ans=-sys.maxsize-1
    for i in range(lenth):
        print(left[i]+(arr[i]*b)+right[i])
    print(ans)
    return ans
A = [ -29, 1, -44, -21 ]
B = -24
C = -29
D = -28
mySolution(A,B,C,D)