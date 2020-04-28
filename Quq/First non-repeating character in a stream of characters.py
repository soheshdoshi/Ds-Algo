def mySolution(A):
    st=[]
    q=[]
    pop_array=[]
    for i in A:
        if i in pop_array:
            if len(q) < 1:
                st.append('#')
            else:
                st.append(q[0])
            continue
        if i not in q:
            q.append(i)
        else:
            pop_array.append(q.pop(q.index(i)))
        if len(q)<1:
            st.append('#')
        else:
            st.append(q[0])
    return ("".join(st))



A="jpxvxivxkkthvpqhhhjuzhkegnzqriokhsgea"
print(mySolution(A))