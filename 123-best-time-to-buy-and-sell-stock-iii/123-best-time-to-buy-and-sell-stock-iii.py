class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def f(ind,buy,cap,dp):
            if cap==0 or ind==n:
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            if buy==1:
                dp[ind][buy][cap]=max(-prices[ind]+f(ind+1,0,cap,dp),0+f(ind+1,1,cap,dp))
                
            else:
                dp[ind][buy][cap]=max(prices[ind]+f(ind+1,1,cap-1,dp),0+f(ind+1,0,cap,dp))
            return dp[ind][buy][cap]
        n=len(prices)
        dp=[[[-1]*(3) for _ in range(2)]for _ in range(n)]
        return f(0,1,2,dp)