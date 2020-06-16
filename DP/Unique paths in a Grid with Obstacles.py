def mySolution(matrix):
    row_lenth=len(matrix)
    col_lenth=len(matrix[0])
    ans_arr=[[0 for _ in range(col_lenth)]for _ in range(row_lenth)]
    if matrix[0][0]==0:
        ans_arr[0][0]=1
    for i in range(1,row_lenth):
        if matrix[i][0]==0:
            ans_arr[i][0]=ans_arr[i-1][0]
    for i in range(1,col_lenth):
        if matrix[0][i]==0:
            ans_arr[0][i]=ans_arr[0][i-1]
    for i in range(1, row_lenth):
        for j in range(1,col_lenth):
            if matrix[i][j]==0:
                ans_arr[i][j]=ans_arr[i-1][j]+ans_arr[i][j-1]
    return ans_arr[-1][-1]
A = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0] ]
print(mySolution(A))
