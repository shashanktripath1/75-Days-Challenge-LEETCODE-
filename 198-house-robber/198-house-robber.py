class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(ind,dp):
            
            if ind==0:
                return nums[ind]
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            take=nums[ind]+f(ind-2,dp)
            not_take=0+f(ind-1,dp)
            dp[ind]= max(take,not_take)
            return dp[ind]
        n=len(nums)
        dp=[-1]*n
        return f(n-1,dp)