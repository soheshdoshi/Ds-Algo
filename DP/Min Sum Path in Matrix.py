def optimzieSolution(matrix,row_lenth,col_lenth):
    for i in range(1,row_lenth):
        matrix[i][0]+=matrix[i-1][0]
    for j in range(1,col_lenth):
        matrix[0][j]+=matrix[0][j-1]
    for i in range(1,row_lenth):
        for j in range(1,col_lenth):
            matrix[i][j]+=min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])
    return matrix[row_lenth][col_lenth]
def mySolution(matix,row_lenth,col_lenth):
    tc=[[0 for i in range(row_lenth)] for j in range(col_lenth)]
    tc[0][0]=matix[0][0]
    for i in range(1,row_lenth+1):
        tc[i][0]=tc[i-1][0]+matix[i][0]
    for j in range(1,col_lenth+1):
        tc[0][j]=tc[0][j-1]+matix[0][j]
    for i in range(1,row_lenth+1):
        for j in range(1,col_lenth+1):
            tc[i][j]=min(tc[i-1][j-1],tc[i-1][j],tc[i][j-1])+matix[i][j]
    return tc[row_lenth][col_lenth]