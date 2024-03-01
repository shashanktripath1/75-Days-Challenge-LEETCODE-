class Solution:
    #space optimized using next and cur array
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*(n)
        ans=1
        for ind in range(n):
            for prev_ind in range(ind):
                if nums[ind]>nums[prev_ind]:
                    dp[ind]=max(dp[ind],1+dp[prev_ind])
            ans=max(ans,dp[ind])
        return ans