from collections import Counter,defaultdict
def mySolution(A,B):
    lenth=len(A)
    x_frq=defaultdict(int)
    y_frq=defaultdict(int)
    ans=0
    for i in range(lenth):
        x_frq[A[i]]+=1
        y_frq[B[i]]+=1
    for i in range(lenth):
        ans+=(x_frq[A[i]]-1)*(y_frq[B[i]]-1)
    #print(x_frq,y_frq)
    return ans


A = [1, 1, 2, 3, 3]
B = [1, 2, 1, 2, 1]
mySolution(A,B)

