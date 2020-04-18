import sys
def mySolution(A,B,C):
  a_lenth=len(A)
  b_lenth=len(B)
  min_diff=sys.maxsize
  Firts_index=second_index=-1
  i=0
  j=b_lenth-1
  while i<a_lenth and j>=0:
      ans=abs(A[i]+B[j]-C)
      if ans==0:
          return [A[i],B[j]]
      if ans<min_diff:
          min_diff=ans
          Firts_index=i
          second_index=j
      if A[i]+B[j]<C:
          i+=1
      else:
          j-=1
  #checking j
  temp=second_index
  temp-=1
  while temp>=0:
      ans=abs(A[Firts_index]+B[temp]-C)
      if ans<=min_diff:
          second_index=temp
      temp -= 1
  return [A[Firts_index],B[second_index]]



A=[1]
B=[2,4]
C=4
print(mySolution(A,B,C))

