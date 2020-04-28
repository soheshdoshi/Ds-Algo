import sys
def mySolution(A):
    lenth=len(A)
    max_area=-sys.maxsize-1
    temp_arr=[0]*lenth
    temp_arr[0]=A[0]
    for i in range(1,lenth):
        temp_arr[i]=min(temp_arr[i-1],A[i])
    #print(temp_arr)
    elemnt=temp_arr[lenth-1]
    max_area = max(max_area, elemnt * (lenth - 1))
    for i in range(lenth-1,-1,-1):
        if elemnt!=temp_arr[i]:
            elemnt=temp_arr[i]
            max_area = max(max_area, elemnt*(i+1))
    print(max_area)



A=[2, 1, 5, 6, 2, 3]
mySolution(A)

