def checkZeroSum(arr):
    lenth=len(arr)
    temp=[0]*(lenth+1)
    for i in range(1,lenth+1):
        temp[i]=temp[i-1]+arr[i-1]
    #print(temp)
    s=set()
    for i in temp:
        if i in s:
            return 0
        else:
            s.add(i)
    return -1


arr=[1,2,3,4,5]
print(checkZeroSum(arr))