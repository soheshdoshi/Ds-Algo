def mySolution(arr):
    lenth=len(arr)
    ans=0
    for i in range(lenth):
        l=[]
        for j in range(i,lenth):
            if arr[j] in l:
                break
            else:
                l.append(arr[j])
        ans+=len(l)
    return ans


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        totFreq = {}
        count = 0
        n = len(A)
        i, j = -1, 0
        mod = 1000000007

        # you can also do below method by lambda 0 with default dict
        for k in range(0, n):
            totFreq[A[k]] = 0
        unqCount = 0
        for j in range(0, n):
            totFreq[A[j]] += 1
            if totFreq[A[j]] >= 2:
                i += 1
                while A[i] != A[j]:
                    totFreq[A[i]] -= 1
                    i += 1
                totFreq[A[j]] -= 1
                unqCount = unqCount + (j - i)
            else:
                unqCount = unqCount + (j - i)
#print(mySolution([1,1,2]))