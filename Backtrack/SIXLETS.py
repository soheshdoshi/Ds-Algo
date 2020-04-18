class Solution:
    def __init__(self):
        self.c=0
    def genrateCombination(self,arr,k,lenth,index,data,i):
        if index==k:
            if sum(data)<=1000:
                self.c+=1
            return
        if i>=lenth:
            return
        data[index]=arr[i]
        self.genrateCombination(arr,k,lenth,index+1,data,i+1)
        self.genrateCombination(arr,k,lenth,index,data,i+1)

    def mySolution(self,arr,k):
        self.genrateCombination(arr,k,len(arr),0,[0]*k,0)
        return self.c


s=Solution()
print(s.mySolution([1,2,8000],4))
