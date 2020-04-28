def mySolution(A):
    lenth=len(A)
    stack=[A[0]]
    temp_arr=[-1]*lenth
    for i in range(1,lenth):
        if stack[-1]<A[i]:
            temp_arr[i]=stack[-1]
            stack.append(A[i])
        else:
            while stack and stack[-1]>=A[i]:
                stack.pop()
            if len(stack)<1:
                temp_arr[i]=-1
            else:
                temp_arr[i]=stack[-1]
            stack.append(A[i])
    return temp_arr

A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
print(mySolution(A))