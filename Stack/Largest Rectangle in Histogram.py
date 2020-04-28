import sys
def left_iddex(A,lenth):
    left_i=[0]*lenth
    stack=[0]
    for i in range(1,lenth):
        if A[stack[-1]]<A[i]:
            left_i[i]=i-stack[-1]-1
            stack.append(i)
        else:
            while stack and A[stack[-1]]>=A[i]:
                stack.pop()
            if len(stack)<1:
                left_i[i]=i
            else:
                left_i[i]=i-stack[-1]-1
            stack.append(i)
    return left_i

def mySolution(A):
    lenth=len(A)
    left_inedx=left_iddex(A,lenth)
    right_index=left_iddex(A[::-1],lenth)[::-1]
    max_area=-sys.maxsize-1
    for i in range(lenth):
        max_area=max(max_area,A[i]*(left_inedx[i]+right_index[i]+1))
    return max_area



A=[2,1,5,6,2,3]
print(mySolution(A))
