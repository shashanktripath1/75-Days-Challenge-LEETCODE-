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
        return self.f(n-1,nums,dp)