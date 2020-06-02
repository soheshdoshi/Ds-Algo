from operator import  eq,gt
def mySolution(arr):
    if eq(len(arr),0):
        return 0
    if eq(len(arr),1):
        return [arr]
    l=[]
    for i in range(len(arr)):
        if gt(i,0) and eq(arr[i],arr[i-1]):
            continue
        temp=arr[i]
        res=arr[:i]+arr[i+1:]
        for p in mySolution(res):
            l.append([temp]+p)
    return l



arr=['aa','bb','cc']
arr.sort()
print(mySolution(arr))