def mySolution(s):
    lenth=len(s)
    dp = [[0] * lenth for i in range(lenth)]
    for i in range(lenth - 1, -1, -1):
        for j in range(i, len(s)):
            if i == j:
                dp[i][j] = 1
            elif i + 1 == j and s[i] == s[j]:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][lenth - 1]
A="aedsead"
print(mySolution(A))