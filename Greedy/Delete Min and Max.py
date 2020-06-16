from collections import Counter

def getCount(n):
    while n>=3:
        temp=n//3
        r=n%3
        n=temp+r
    return n
def mySolution(arr):
    lenth=len(arr)
    if lenth==1:
        return 1
    count1=0
    count2=0
    has=Counter(arr)
    for i in has:
        temp=getCount(has[i])
        if temp==1:
            count1+=1
        else:
            count2+=1
    count1+=count2
    if count2%2!=0:
        count1-=1
    return count1

arr=[ 2, 4, 1, 5, 4, 4, 3, 2, 3, 2, 6, 5, 5, 6, 5, 5, 4, 5, 1, 5, 1, 6, 5, 5, 1 ]
print(mySolution(arr))
