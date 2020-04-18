def mySolution(arr):
    lenth=len(arr)
    if lenth==0:
        return ""
    if lenth==1:
        return arr[0]
    arr.sort()
    end=min(len(arr[0]),len(arr[lenth-1]))
    i=0
    while i<end and arr[0][i]==arr[lenth-1][i]:
        i+=1
    return arr[0][:i]