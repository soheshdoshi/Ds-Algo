import sys
def longestConsti(arr):
    #lenth=len(arr)
    s=set(arr)
    ans=-sys.maxsize-1
    for num in arr:
        if num-1 in s:
            continue
        else:
            count=1
            while num+1 in s:
                count+=1
                num+=1
            ans=max(ans,count)
    return ans



arr=[100,4,200,1,3,2]
print(longestConsti(arr))

