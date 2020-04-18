def subArrray(arr,fsum):
    lenth=len(arr)
    cur_sum=0
    strat_p=0
    for i in range(lenth):
        cur_sum+=arr[i]
        while cur_sum>fsum and strat_p<i:
            cur_sum-=arr[strat_p]
            strat_p+=1
        if cur_sum==fsum:
            return arr[strat_p:i+1]
    return [-1]
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return a list of integers
#     def solve(self, A, B):
#         return subArrray(A,B)



A =[ 42, 9, 38, 36, 48, 33, 36, 50, 38, 8, 13, 37, 33, 38, 17, 25, 50, 50, 41, 29, 34, 18, 16, 6, 49, 16, 21, 29, 41, 7, 37, 14, 5, 30, 35, 26, 38, 35, 9, 36, 34, 39, 9, 4, 41, 40, 3, 50, 27, 17, 14, 5, 31, 42, 5, 39, 38, 38, 47, 24, 41, 5, 50, 9, 29, 14, 19, 27, 6, 23, 17, 1, 22, 38, 35, 6, 35, 41, 34, 21, 30, 45, 48, 45, 37 ]
B = 100
print(subArrray(A,B))

