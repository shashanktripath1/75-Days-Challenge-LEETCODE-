class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def f(ind,buy,dp):
            if ind==n:
                return 0
            if(buy==1):
                dp[ind][buy]=max(-prices[ind]+f(ind+1,0,dp),0+f(ind+1,1,dp))
            else:
                dp[ind][buy]=max(prices[ind]+f(ind+1,1,dp),0+f(ind+1,0,dp))
            return dp[ind][buy]
            
        n=len(prices)
        dp=[[0 for i in range(2)]for _ in range(n+1)]
        dp[n][0]=dp[n][1]=0
        for ind in range(n-1,-1,-1):
            for buy in range(0,2):
                if buy==1:
                    profit=max(-prices[ind]+dp[ind+1][0],dp[ind+1][1])
                else:
                    profit=max(prices[ind]+dp[ind+1][1],dp[ind+1][0])
                dp[ind][buy]=profit
        return dp[0][1]


                