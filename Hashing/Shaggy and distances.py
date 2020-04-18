from collections import defaultdict
import sys
def mySolution(arr):
    d=defaultdict(int)
    min_diff=sys.maxsize
    for i in range(len(arr)):
        if d[arr[i]]==0:
            d[arr[i]]=i+1
        else:
            min_diff=min(min_diff,abs(d[arr[i]]-i-1))
    if min_diff==sys.maxsize:
        return -1
    return min_diff

arr=[1,1]
print(mySolution(arr))


