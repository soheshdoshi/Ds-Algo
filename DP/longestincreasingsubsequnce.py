def mySolution(arr):
    lenth=len(arr)
    temp_arr=[1]*lenth
    for i in range(1,lenth):
        for j in range(i-1,-1,-1):
            if arr[j]<arr[i]:
                temp_arr[i]=1+temp_arr[j]
                break
    return max(temp_arr)



A=[1,2,3,0,4,1,5,2,6,3,5]
print(mySolution(A))
