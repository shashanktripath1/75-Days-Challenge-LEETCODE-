class Solution:
    def f(self,ind,prev_ind,arr,dp):
        if ind==len(arr):
            return 0
        if dp[ind][prev_ind]!=-1:
            return dp[ind][prev_ind]
        not_take=0+self.f(ind+1,prev_ind,arr,dp)
        take=float('-inf')
        if prev_ind==-1 or arr[ind]>arr[prev_ind]:
            take=1+self.f(ind+1,ind,arr,dp)
        dp[ind][prev_ind]=max(not_take,take)
        return dp[ind][prev_ind]
    #tabulation    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0 for i in range(n+1)]for j in range(n+1)]
        for ind in range(n-1,-1,-1):
            for prev_ind in range(ind-1,-2,-1):
                not_take=0+dp[ind+1][prev_ind+1]#due to coordinate shift
                take=0
                if prev_ind==-1 or nums[ind]>nums[prev_ind]:
                    take=1+dp[ind+1][ind+1]
                dp[ind][prev_ind+1]=max(not_take,take)
        return dp[0][-1+1]
    