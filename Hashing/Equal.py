from collections import defaultdict
def mySolution(A):
    lenth=len(A)
    d={}
    l=[]
    for i in range(lenth-1):
        for j in range(i+1,lenth):
            ans=A[i]+A[j]
            if ans not in d:
                d[ans]=(i,j)
            else:
                if d[ans][0]==i or d[ans][0]==j or d[ans][1]==i or d[ans][1]==j:
                    continue
                else:
                    l.append(list(d[ans])+[i,j])

    return sorted(l)[0] if l else l




A= [3, 4, 7, 1, 2, 9, 8]
mySolution(A)