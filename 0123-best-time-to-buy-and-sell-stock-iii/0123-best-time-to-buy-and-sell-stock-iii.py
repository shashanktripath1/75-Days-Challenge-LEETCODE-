class Solution:
    def f(self,ind,buy,cap,prices,dp):
        if ind==len(prices) or cap==0:
            return 0
        if dp[ind][buy][cap]!=-1:
            return dp[ind][buy][cap]
        if buy==0:
            op1=0+self.f(ind+1,0,cap,prices,dp)
            op2=-prices[ind]+self.f(ind+1,1,cap,prices,dp)
        else:
            op1=0+self.f(ind+1,1,cap,prices,dp)
            op2=prices[ind]+self.f(ind+1,0,cap-1,prices,dp)
        dp[ind][buy][cap]=max(op1,op2)
        return dp[ind][buy][cap]
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1 for _ in range(3)]for _ in range(2)]for _ in range(n+1)]
        return self.f(0,0,2,prices,dp)