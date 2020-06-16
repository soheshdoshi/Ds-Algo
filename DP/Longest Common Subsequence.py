def mySolution(A,B):
    a_lenth=len(A)
    b_lenth=len(B)
    temp_arr=[[0 for _ in range(a_lenth+1)] for j in range(b_lenth+1)]
    for i in range(b_lenth+1):
        for j in range(a_lenth+1):
            if i==0 or j==0:
                temp_arr[i][j]=0
            elif A[j-1]==B[i-1]:
                temp_arr[i][j]=1+temp_arr[i-1][j-1]
            else:
                temp_arr[i][j]=max(temp_arr[i-1][j],temp_arr[i][j-1])
    return temp_arr[b_lenth][a_lenth]



A="abbcdgf"
B="bbadcgf"
print(mySolution(A,B))
