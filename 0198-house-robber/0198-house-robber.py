#Tabulation Solution
class Solution:
    def f(self,ind,arr,dp):
        if ind==0:
            return arr[ind]
        if ind<0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        pick=arr[ind]+self.f(ind-2,arr,dp)
        not_pick=0+self.f(ind-1,arr,dp)
        dp[ind]=max(pick,not_pick)
        return dp[ind]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        dp[0]=nums[0]
        neg=0
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick=nums[i]+dp[i-2]
            not_pick=0+dp[i-1]
            dp[i]=max(pick,not_pick)
        return dp[n-1]