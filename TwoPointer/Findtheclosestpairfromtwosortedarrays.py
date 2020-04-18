class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def maxone(self, A, B):
	    i=j=si=sj=0
	    while j<len(A):
	        if A[j]==0:
	            B-=1
	            while i<=j and B<0:
	                if A[i]==0:
	                    B+=1
	                else:
	                    return 0
	                i+=1
	        j+=1
	        if j-i>sj-si:
	            si,sj=i,j
	    return list(range(si,sj))