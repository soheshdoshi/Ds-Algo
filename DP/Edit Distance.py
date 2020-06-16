def mySolution(A,B):
    a_lenth=len(A)
    b_lenth=len(B)
    tem_arr=[[0 for i in range(b_lenth+1)] for j in range(a_lenth+1)]
    for i in range(a_lenth+1):
        for j in range(b_lenth+1):
            if i==0:
                tem_arr[i][j]=j
            elif j==0:
                tem_arr[i][j]=i
            elif A[i-1]==B[j-1]:
                tem_arr[i][j]=tem_arr[i-1][j-1]
            else:
                tem_arr[i][j]=1+min(tem_arr[i-1][j],tem_arr[i][j-1],tem_arr[i-1][j-1])
    return tem_arr[a_lenth][b_lenth]

A = "Anshuman"
B = "Antihuman"
print(mySolution(A,B))