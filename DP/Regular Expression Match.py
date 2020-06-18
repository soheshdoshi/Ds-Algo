def mysolution(s,p):
    s,p=' '+s,' '+p
    lenth_s,lenth_p=len(s),len(p)
    dp=[[0 for _ in range(lenth_p)] for _ in range(lenth_s)]
    dp[0][0]=1
    for i in range(1,lenth_p):
        if p[i]=='*':
            dp[0][i]=dp[0][i-2]
    for i in range(1,lenth_s):
        for j in range(1,lenth_p):
            if p[j] == s[i] or p[j]=='?':
                dp[i][j]=dp[i-1][j-1]
            elif p[j]=='*':
                dp[i][j] = dp[i][j - 2] or int(dp[i - 1][j] and p[j - 1] in {s[i], '?'})
    return bool(dp[-1][-1])


