# def mySolution(s,t):
#     l1, l2 = len(s)+1, len(t)+1
#     dp = [[1] * l2 for _ in range(l1)]
#     for j in range(1, l2):
#         dp[0][j] = 0
#     for i in range(1, l1):
#         for j in range(1, l2):
#             dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
#     return dp[-1][-1]
#
#
# A = "rabbbit"
# B = "rabbit"
# print(mySolution(A,B))
#
#

