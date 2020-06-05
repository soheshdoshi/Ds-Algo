
def minJumps(arr,lenth):
    if lenth<=1:
        return 0
    if arr[0]==0:
        return -1
    maxReach=arr[0]
    jups=1
    step=arr[0]
    for i in range(1,lenth):
        if i==lenth-1:
            return jups
        maxReach=max(maxReach,arr[i]+i)
        step-=1
        if step==0:
            jups+=1
            if i>=maxReach:
                return -1
            step=maxReach-i
    return jups
