class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        nums = list(map(str, A))
        nums = sorted(nums, key=lambda x:str(x)*10, reverse=True)
        return ''.join(nums) if nums[0] != '0' else '0'


s=Solution()
s.largestNumber([3,30,54,8,7])