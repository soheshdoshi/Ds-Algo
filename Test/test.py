# from collections import defaultdict
# import sys
# def mySolution(arr):
#     row_lenth=len(arr)
#     col_lenth=2
#     d=defaultdict(set)
#     for i in range(row_lenth):
#         d[arr[i][0]].add(arr[i][1])
#     lenth=len(d)
#     city=list(d.keys())
#     print(d)
#     print(city)
#     max_elemnt=-sys.maxsize-1
#     max_index=[0,0]
#     for i in range(lenth-1):
#         for j in range(i+1,lenth):
#             intersection=d[city[i]].intersection(d[city[j]])
#             Union=d[city[i]].union(d[city[j]])
#             uniq_count=Union-intersection
#             inter_count=len(intersection)
#             uniq_count=len(uniq_count)
#             divion=-sys.maxsize-1
#             if uniq_count==0:
#                 divion=inter_count
#             else:
#                 divion=inter_count/uniq_count
#             if max_elemnt<divion:
#                 max_elemnt=divion
#                 max_index=[city[i],city[j]]
#     return max_index
#
#
#
#             #print(d[city[i]],d[city[j]])
#
# A =[
#   [1, 1],
#   [1, 2],
#   [1, 3],
#   [1, 4],
#   [2, 5],
#   [2, 6],
#   [2, 7],
#   [3, 8],
#   [3, 9],
#   [3, 10],
#   [4, 1],
# ]
# print(mySolution(A))



#count = 0
class Solution:
    count=0
    def myFuction(self,digit_num,n,x,count):
        if n==0 and x==0:
            self.count+=1
            return
        for i in range(1,digit_num+1):
            if x>=i:
                self.myFuction(digit_num,n-1,x-i,count)
        return self.count

s=Solution()
digit_num=6
n = 1
x = 1
print(s.myFuction(digit_num,n,x,0))
