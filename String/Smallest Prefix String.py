def mySolution(A,B):
    s=A[0]
    for i in A[1:]:
        if i>B[0]:
            break
        s+=i
    return s+B[0]


A="tom"
B="rid"
print(mySolution(A,B))


print("t">'r')