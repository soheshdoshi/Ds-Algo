import sys
from math import ceil,log
class SegmenTree:
    def __init__(self,lenth,A):
        self.lenth=lenth
        self.maxSizeSeg = 2 * pow(2, ceil(log(self.lenth, 2))) - 1
        self.segTree = [0] * self.maxSizeSeg
        self.arr=A
        self.buildTree(0,self.lenth-1,0)

    def buildTree(self,strat,end,pos):
        if strat==end:
            self.segTree[pos]=self.arr[strat]
            return self.segTree[pos]
        mid=strat+(end-strat)//2
        self.segTree[pos]=min(self.buildTree(strat,mid,2*pos+1),self.buildTree(mid+1,end,2*pos+2))
        return self.segTree[pos]
    def qury_seg(self,q_st,q_en,strat,end,pos):
        if q_st<=strat and q_en>=end:
            return self.segTree[pos]
        if end<q_st or strat>q_en:
            return sys.maxsize+1
        mid=strat+(end-strat)//2
        return min(self.qury_seg(q_st,q_en,strat,mid,2*pos+1),self.qury_seg(q_st,q_en,mid+1,end,2*pos+2))
    def qury(self,left,right):
        return self.qury_seg(left,right,0,self.lenth-1,0)

    def update(self,index,value):
        self.update_segTre(0,self.lenth-1,0,index,value)
    def update_segTre(self,start,end,pos,inedx,value):
        if start==end:
            self.segTree[pos]=value
            return self.segTree[pos]
        mid=start+(end-start)//2
        if inedx>=start and inedx<=mid:
            self.update_segTre(start, mid, 2 * pos + 1, inedx, value)
        else:
            self.update_segTre(mid + 1, end, 2 * pos + 2, inedx, value)
        self.segTree[pos]=min(self.segTree[2*pos+1],self.segTree[2*pos+2])
        return self.segTree[pos]
    # def printTree(self):
    #     print(self.segTree)


A = [5, 4, 5, 7]
B = [
    [1, 2, 4],
    [0, 1, 2],
    [1, 1, 4]
]
arr=[]
s=SegmenTree(len(A),A)
s.printTree()
for i in B:
    if i[0]==1:
        arr.append(s.qury(i[1]-1,i[2]-1))
    else:
        s.update(i[1]-1,i[2])
print(arr)


