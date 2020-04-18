from collections import Counter,defaultdict
def genrateHash(str):
    p=31
    ans=0
    for i in range(1,len(str)+1):
        ans+=(pow(p,i)*ord(str[i-1]))
    return ans


def mySolution(arr):
    lenth=len(arr)
    d=defaultdict(list)
    for i in range(lenth):
        ans=genrateHash(sorted(arr[i]))
        d[ans].append(i+1)
    #print(d)
    return list(d.values())



A=["cde","bee"]
mySolution(A)
