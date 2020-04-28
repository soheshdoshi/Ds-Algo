def mySolution(arr,window_size):
    lenth=len(arr)
    q=[]
    st=[]
    for i in range(window_size):
        if arr[i]<0:
            q.append(arr[i])
    if q:
        st.append(q[0])
    else:
        st.append(0)
    i=1
    j=window_size
    while j<lenth:
        if q and arr[i-1]==q[0]:
            q.pop(0)
        if arr[j]<0:
            q.append(arr[j])
        if q:
            st.append(q[0])
        else:
            st.append(0)
        i+=1
        j+=1
    return st
A =[ -9, 4, 8, -1, 1, 2, 0, -2, 8, -7, 9 ]
B = 4
print(mySolution(A,B))
