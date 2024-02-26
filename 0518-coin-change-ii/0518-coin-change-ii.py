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
        dp=[[0 for j in range(amount+1)]for i in range(n+1)]
        for j in range(amount+1):
            if j%coins[0]==0:
                dp[0][j]=1
        for ind in range(1,n):
            for target in range(amount+1):
                not_take=0+dp[ind-1][target]
                take=0
                if coins[ind]<=target:
                    take=dp[ind][target-coins[ind]]
                dp[ind][target]=not_take+take
        return dp[n-1][amount]