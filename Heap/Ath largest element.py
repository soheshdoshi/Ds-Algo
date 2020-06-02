import  heapq

def mySolution(arr,kth):
    lenth=len(arr)
    new_arr=[]
    ans=[]
    for i in range(lenth):
        if i<kth-1:
            heapq.heappush(new_arr,arr[i])
            ans.append(-1)
        elif i==kth-1:
            heapq.heappush(new_arr,arr[i])
            ans.append(new_arr[0])
        else:
            pop_ele=heapq.heappop(new_arr)
            if pop_ele<arr[i]:
                heapq.heappush(new_arr,arr[i])
            else:
                heapq.heappush(new_arr,pop_ele)
            ans.append(new_arr[0])
        #print(new_arr)
    return ans


A = 4
B = [1,2,3,4,5,6]
print(mySolution(B,A))

