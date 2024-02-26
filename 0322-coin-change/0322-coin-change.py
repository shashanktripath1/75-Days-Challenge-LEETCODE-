class Solution:
    def f(self,ind,target,arr,dp):
        if ind==0:
            if target%arr[0]==0:
                return target//arr[0]
            else:
                return int(1e9)
        if dp[ind][target]!=-1:
            return dp[ind][target]
        not_take=0+self.f(ind-1,target,arr,dp)
        take=int(1e9)
        if arr[ind]<=target:
            take=1+self.f(ind,target-arr[ind],arr,dp)
        dp[ind][target]=min(not_take,take)
        return dp[ind][target]
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1 for j in range(amount+1)] for i in range(n)]
        if amount==0:
            return 0
        ans=self.f(n-1,amount,coins,dp)
        if ans>=int(1e9):
            return -1
        return ans