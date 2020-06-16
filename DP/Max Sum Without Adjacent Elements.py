def mySolution(A,lenth):
    max_el=max(A[0][0],A[1][0])
    exc=0
    for i in range(1,lenth):
        exc_new=max(max_el,exc)
        max_el=exc+max(A[0][i],A[1][i])
        exc=exc_new
    return max(exc,max_el)