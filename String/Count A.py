def mySolution(arr):
    total_c=0
    curr_c=0
    lenth=len(arr)
    for i in range(lenth):
        if arr[i]=='a':
            curr_c+=1
        if arr[i]=='a':
            total_c+=curr_c
    return total_c

print(mySolution("aab"))