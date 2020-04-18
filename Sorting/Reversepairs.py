#count=0
class Solution:
    def __init__(self):
        self.c=0
    def merge(self,left,right):
        i,j=0,0
        while i<len(left) and j<len(right):
            if left[i]<=2*right[j]:
                i+=1
            else:
                self.c+=len(left)-i
                j+=1
        return sorted(left+right)
    def MegeSot(self,arr):
        if len(arr)<2:
            return arr
        else:
            midd=len(arr)//2
            left_arr=self.MegeSot(arr[:midd])
            right_arr=self.MegeSot(arr[midd:])
            return list((self.merge(left_arr,right_arr)))
    def solve(self,arr):
        self.MegeSot(arr)
        return self.c

A = [ 14046, 57239, 78362, 99387, 27609, 55100, 65536, 62099, 40820, 33056, 88380, 78549, 57512, 33137, 81212, 32365, 42276, 65368, 52459, 74924, 25355, 76044, 78056, 45190, 94365, 58869, 20611 ]
s=Solution()
print(s.solve(A))

from bisect import bisect


# class Solution:
#     # @param A : list of integers
#     # @return an integer
#
#     def mrgsort(self, lft, rgt):
#         return sorted(lft + rgt)
#
#     def mergesortrp(self, arr):
#         if len(arr) <= 1:
#             return arr, 0
#         else:
#             mid = len(arr) // 2
#             leftPart, lRevPairCount = self.mergesortrp(arr[:mid])
#             rightPart, rRevPairCount = self.mergesortrp(arr[mid:])
#             totrpCount = lRevPairCount + rRevPairCount
#             currRPcount = 0
#             for r in rightPart:
#                 currRPcount = len(leftPart) - bisect(leftPart, r * 2)
#                 if currRPcount == 0:
#                     break
#                 totrpCount += currRPcount
#             sArr = self.mrgsort(leftPart, rightPart)
#             return sArr, totrpCount
#
#     def strictIncreaseByOne(self, arr):
#         result = all((i < j and (j - 1) == 1) for i, j in zip(nums, nums[1:]))
#         return result
#
#     def solve(self, A):
#         n = len(A)
#         if self.strictIncreaseByOne and len(A) <= 1:
#             return 0
#         _, count = self.mergesortrp(A)
#
#         return count