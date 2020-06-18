mod=(10**9)+7
def countCommandSub(s1,s2):
    s1_lenth=len(s1)
    s2_lenth=len(s2)
    temp_arr=[[0 for _ in range(s2_lenth+1)] for _ in range(s1_lenth+1)]
    for i in range(1,s1_lenth+1):
        for j in range(1,s2_lenth+1):
            if s1[i-1]==s2[j-1]:
                temp_arr[i][j]+=(1%mod+temp_arr[i][j-1]%mod+temp_arr[i-1][j]%mod)%mod
            else:
                temp_arr[i][j]+=(temp_arr[i-1][j]%mod+temp_arr[i][j-1]%mod-temp_arr[i-1][j-1]%mod)%mod
    way=[]
    for i in range(s1_lenth):
        if i==0 or i==s1_lenth-1:
            way.append(1)
        else:
            #print(i+1,s1_lenth-i)
            way.append(temp_arr[i+1-1][s1_lenth-i-1]+1)
    return way

print(countCommandSub("aaa","aaa"))

