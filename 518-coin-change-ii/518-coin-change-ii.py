class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n=len(coins)
        dp=[[0 for i in range(amount+1)]for j in range(n+1)]

        for t in range(amount+1):
            if(t%coins[0]==0):
                dp[0][t]+=1
            dp[0][t]+=0
        for ind in range(1,n):
            for tar in range(amount+1):
                not_take=dp[ind-1][tar]
                take=0
                if coins[ind]<=tar:
                    take=dp[ind][tar-coins[ind]]
                dp[ind][tar]=take + not_take
        return dp[n-1][amount]
                
        
           