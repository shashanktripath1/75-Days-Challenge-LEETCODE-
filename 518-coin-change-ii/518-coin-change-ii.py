class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def helper(ind,tar,dp):
            if ind==0:
                if (tar%coins[0]==0):
                    return 1
                return 0
            if dp[ind][tar]!=-1:
                return dp[ind][tar]
            not_take=helper(ind-1,tar,dp)
            take=0
            if coins[ind]<=tar:
                take=helper(ind,tar-coins[ind],dp)
            dp[ind][tar]=take+not_take
            return dp[ind][tar]
        n=len(coins)
        dp=[[-1 for i in range(amount+1)]for j in range(n+1)]
        return helper(n-1,amount,dp)