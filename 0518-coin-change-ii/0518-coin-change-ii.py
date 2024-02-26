class Solution:
    def f(self,ind,target,arr,dp):
        if ind==0:
            if target%arr[0]==0:
                return 1
            return 0
        if dp[ind][target]!=-1:
            return dp[ind][target]
        not_take=0+self.f(ind-1,target,arr,dp)
        take=0
        if arr[ind]<=target:
            take=self.f(ind,target-arr[ind],arr,dp)
        dp[ind][target]=not_take+take
        return dp[ind][target]
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1 for j in range(amount+1)]for i in range(n)]
        return self.f(n-1,amount,coins,dp)