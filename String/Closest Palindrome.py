def mySolution(str):
    lenth=len(str)
    count=0
    ev=str[::-1]
    for i in range(lenth):
        if str[i]!=ev[i]:
            count+=1
    if count<2 and lenth%2!=0:
        return "YES"
    return "NO"