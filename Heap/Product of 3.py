import heapq

def multiplication(arr):
    ans=1
    for i in arr:
        ans=ans*i
    return ans
def mySolution(arr):
    lenth=len(arr)
    ans_arr=[]
    k_min_arr=[]
    for i in range(lenth):
        if i<2:
            ans_arr.append(-1)
            k_min_arr.append(arr[i])
        else:
            if i==2:
                k_min_arr.append(arr[i])
                ans_arr.append(multiplication(k_min_arr))
                heapq.heapify(k_min_arr)
            else:
                pop_ele=heapq.heappop(k_min_arr)
                heapq.heappush(k_min_arr,max(arr[i],pop_ele))
                ans_arr.append(multiplication(k_min_arr))
    return ans_arr
A =[11, 5, 6, 2, 8, 10 ]
print(mySolution(A))
