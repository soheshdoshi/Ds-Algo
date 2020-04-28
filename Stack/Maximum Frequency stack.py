from collections import defaultdict,Counter
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def __init__(self):
        self.maxfrq=0
        self.frq=Counter()
        self.gp=defaultdict(list)
    def push(self,x):
        f=self.frq[x]+1
        self.frq[x]=f
        self.maxfrq=max(self.maxfrq,f)
        self.gp[f].append(x)
        return -1
    def pop(self):
        x=self.gp[self.maxfrq].pop()
        self.frq[x]-=1
        if not self.gp[self.maxfrq]:
            self.maxfrq-=1
        return x
    def solve(self, A):
        lenth=len(A)
        l=[]
        for i in range(lenth):
            if A[i][0]==1:
                l.append(self.push(A[i][1]))
            else:
                l.append(self.pop())
        return l





