import sys
def minimCount(A,B,C):
    min_szie=sys.maxsize
    i=0
    j=0
    k=0
    while i<len(A) and j<len(B) and k<len(C):
        minmume=min(A[i],B[j],C[k])
        maxmume=max(A[i],B[j],C[k])
        if maxmume-minmume<min_szie:
            min_szie=maxmume-minmume
        if min_szie==0:
            return 0
        if A[i]==minmume:
            i+=1
        elif B[j]==minmume:
            j+=1
        else:
            k+=1
    return min_szie


A = [1]
B = [2]
C = [10]
print(minimCount(A,B,C))