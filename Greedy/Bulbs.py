def mySolution(arr):
    count=0
    lenth=len(arr)
    min_togg=0
    for i in range(lenth):
        if arr[i]==1 and count%2==0:
            continue
        if arr[i]==0 and count%2!=0:
            continue
        elif arr[i]==0 and count%2==0:
            count+=1
            min_togg+=1
        elif arr[i]==1 and count%2!=0:
            count+=1
            min_togg+=1
    return min_togg