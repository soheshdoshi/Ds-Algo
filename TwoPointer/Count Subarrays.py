def mySOlutino(arr):
    lenth=len(arr)
    count=1
    for i in range(lenth-1):
        ans=arr[i:]
        #print(ans)
        if len(ans)==2:
            if ans[0]!=ans[1]:
                count+=2
            else:
                count+=1
        else:
            for j in range(len(ans)-1):
                count+=1
                if ans[j]==ans[j+1]:
                    break
            #print(count)
    return count


arr=[1,2,2,3]
mySOlutino(arr)
