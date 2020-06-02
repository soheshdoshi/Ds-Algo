import heapq

def mySolution(A,B):
    lenth=len(A)
    new_arr=[]
    for i in range(lenth):
        heapq.heappush(new_arr,(A[i],A[i]))
    print(new_arr)
    for _ in range(B):
        elemnt,orignal=heapq.heappop(new_arr)
        heapq.heappush(new_arr,(elemnt+orignal,orignal))
    print(new_arr)
    return new_arr[-1]


A = [1,2,3,4]
B = 3
mySolution(A,B)