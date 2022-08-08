class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=1
        dp=[1]*len(nums)
        for ind in range(len(nums)):
            for prev in range(ind):
                if nums[ind]>nums[prev]:
                    dp[ind]=max(dp[ind],1+dp[prev])
            ans=max(ans,dp[ind])
        return ans
            