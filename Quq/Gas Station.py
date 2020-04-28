class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, A, B):
	    if sum(A) < sum(B): return -1
	    n, s, left_gas = len(A), 0, 0
	    for i in range(n):
		    if A[i] + left_gas < B[i]:
			    s, left_gas = i+1, 0
		    else:
			    left_gas += A[i]-B[i]
	    return s
