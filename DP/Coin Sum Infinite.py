def mySolution(A,B):
    coin_lenth=len(A)
    temp_arr=[[0 for _ in range(coin_lenth)] for _ in range(B+1)]
    mod=(10**6)+7
    for i in range(coin_lenth):
        temp_arr[0][i]=1
    for i in range(1,B+1):
        for j in range(coin_lenth):
            include=None
            exclude=None
            if i-A[j]>=0:
                include=temp_arr[i-A[j]][j]
            else:
                include=0
            if j>=1:
                exclude=temp_arr[i][j-1]
            else:
                exclude=0
            temp_arr[i][j]=(include%mod+exclude%mod)%mod
    return temp_arr[B][coin_lenth-1]

print(mySolution([1,2,3],4))