def mySolution(A):
    stat_arr=[1,2,3]
    if A<4:
        return stat_arr[:A]
    #q=[i for i in stat_arr]
    st=[i for i in stat_arr]
    index=0
    while len(st)<A:
        min_elm = st[index]
        for i in stat_arr:
            if len(st)<A:
                el=(min_elm*10)+i
                st.append(el)
            else:
                return st
        index+=1
    return st


print(mySolution(15))


