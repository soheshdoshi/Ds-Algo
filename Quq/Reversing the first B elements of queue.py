def mySolution(A,B):
    lenth=len(A)
    st=[]
    q=[]
    for i in range(B):
        st.append(A[i])
    while st:
        q.append(st.pop())
    for i in range(B,lenth):
        q.append(A[i])
    return q



A=[1,2,3,4,5]
B=3
print(mySolution(A,B))


