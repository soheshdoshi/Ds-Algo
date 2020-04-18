from collections import Counter

def findXor(arr):
    arr=sorted(arr)
    p=1000003
    ans=0
    mod=(10**9)+7
    for i in range(1,len(arr)+1):
        ans+=(arr[i-1]*pow(p,i))%mod
    return ans

def mySolution(A,B):
    qury_lenth=len(B)
    l=[]
    qury_set={}
    for i in range(qury_lenth):
        q=(B[i][0],B[i][1])
        q1=(B[i][2],B[i][3])
        s1=-1
        s2=-1
        if q not in qury_set:
            s1=findXor(A[B[i][0]:B[i][1]+1])
            qury_set[q]=s1
        else:
            s1=qury_set[q]
        if q1 not  in qury_set:
            s2=findXor(A[B[i][2]:B[i][3]+1])
            qury_set[q1]=s2
        else:
            s2=qury_set[q1]
        if s1==s2:
            l.append(1)
        else:
            l.append(0)
    #print(qury_set)
    return l


A = [ 1, 7, 11, 8, 11, 7, 1 ]
B =[
  [0, 2, 4, 6]
]
print(mySolution(A,B))


