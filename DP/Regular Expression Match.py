def mySolution(A,B):
    a_lenth=len(A)
    b_lenth=len(B)
    ans_arr=[[False for i in range(a_lenth+1)]for j in range(b_lenth+1)]
    ans_arr[0][0]=True
    for i in range(b_lenth+1):
        ans_arr[i][0]=i>1 and ans_arr[i-2][0] and B[i-1]=='*'
    