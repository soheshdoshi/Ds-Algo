import sys
from math import ceil,log
class SegmenTree:
    def __init__(self,A):
        self.lenth=A
        self.maxSizeSeg = 2 * pow(2, ceil(log(self.lenth, 2))) - 1
        self.segTree = [0] * self.maxSizeSeg
        self.arr=[1 for _ in range(A)]
        self.buildTree(0,self.lenth-1,0)

    def buildTree(self,strat,end,pos):
        if strat==end:
            self.segTree[pos]=self.arr[strat]
            return self.segTree[pos]
        mid=strat+(end-strat)//2
        self.segTree[pos]=self.buildTree(strat,mid,2*pos+1)+self.buildTree(mid+1,end,2*pos+2)
        return self.segTree[pos]
    def printTre(self):
        print(self.segTree)
        print(self.arr)




A=4
s=SegmenTree(A)
s.printTre()