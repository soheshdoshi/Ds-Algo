from collections import Counter
def mySolution(A,B):
    d=Counter(B)
    for i in d.keys():
        if d[i]%A!=0:
            return -1
    return 1


A=2
B="aabbbb"
print(mySolution(A,B))