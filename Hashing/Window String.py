import sys
from collections import  Counter
def mySolution(A,B):
    target_counter=Counter(B)
    i,found=0,0
    min_win=""
    for j in range(len(A)):
        if target_counter[A[j]]>0:
            found+=1
        target_counter[A[j]]-=1
        while found==len(B):
            if not min_win or j-i+1<len(min_win):
                min_win=A[i:j+1]
            target_counter[A[i]]+=1
            if target_counter[A[i]]>0:
                found-=1
            i+=1
    return min_win


A="ADOBECODEBANC"
B="ABC"
print(mySolution(A,B))
