import sys
def mySolution(num):
    squares = [i * i for i in range(1,320)]
    ans = [0, 1]
    for i in range(2,num+1):
        j = 0
        tempAns = sys.maxsize
        while squares[j] <= i:
            tempAns = min(tempAns, 1 + ans[i - squares[j]])
            j += 1
        ans.append(tempAns)
    return ans[num]
class Solution:
	# @param A : integer
	# @return an integer
	def countMinSquares(self, A):
	    return mySolution(A)
