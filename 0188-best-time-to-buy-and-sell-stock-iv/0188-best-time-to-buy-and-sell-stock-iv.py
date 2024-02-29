class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0 for _ in range(k+1)]for _ in range(2)]for _ in range(n+1)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):#point to remember wnen do revision
                    if buy==0:
                        op1=0+dp[ind+1][0][cap]
                        op2=-prices[ind]+dp[ind+1][1][cap]
                    else:
                        op1=0+dp[ind+1][1][cap]
                        op2=prices[ind]+dp[ind+1][0][cap-1]
                    dp[ind][buy][cap]=max(op1,op2)
        return dp[0][0][k]