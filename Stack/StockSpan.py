def mySolution(A):
    lenth=len(A)
    temp_arr=[1]*lenth
    stack=[]
    for i in range(lenth):
        if i==0:
            stack.append(0)
        else:
            if A[i-1]>A[i]:
                stack.append(i)
            else:
                while stack and A[stack[-1]]<=A[i]:
                    stack.pop()
                if len(stack)<=0:
                    temp_arr[i]=i+1
                    stack.append(i)
                else:
                    temp_arr[i]=i-stack[-1]
                    stack.append(i)
    print(temp_arr)



A=[100,80,50,70,80,75,85,105,85]
mySolution(A)