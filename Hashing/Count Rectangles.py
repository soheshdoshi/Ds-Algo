from collections import defaultdict
def mySolution(A,B):
    lenth=len(A)
    ans=0
    point_set=set(A+B)
    for i in range(lenth-1):
        for j in range(i+1,lenth):
            if A[i]!=B[i] and A[j]!=B[j]:
                p3=abs(B[i]-A[i]//B[j]-A[j])
                p4=abs(B[j]-A[j]//B[i]-A[i])
                if p3 in point_set or p4 in point_set:
                    ans+=1
    #print(ans)
    if ans==1:
        return ans
    return ans//2+1


A = [ 9, 5, 1, 1, 3, 7, 7, 9, 6, 9, 2, 8 ]
B = [ 8, 1, 5, 3, 8, 5, 4, 5, 2, 2, 7, 9 ]
print(mySolution(A,B))