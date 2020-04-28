def mySolution(A):
    lenth=len(A)
    stack=[]
    tep_arr=[0]*lenth
    for i in range(lenth):
        if i==0:
            stack.append(i)
        else:
            if A[stack[-1]]<A[i]:
                while stack and A[stack[-1]]<A[i]:
                    tep_arr[stack[-1]]=A[i]
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)
    while stack:
        tep_arr[stack[-1]]=-1
        stack.pop()
    print(tep_arr)


A=[10,13,22,7,24]
mySolution(A)