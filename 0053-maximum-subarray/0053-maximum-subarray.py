class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1,maxi=0,float('-inf')
        n=len(nums)
        for i in range(n):
            sum1+=nums[i]
            
            if sum1>maxi:
                maxi=sum1
            if sum1<0:
                sum1=0
        return maxi