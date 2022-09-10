class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1 or k== 0: return 0
        
        dp = [[0]*n for i in range(k+1)]
        
        for t in range(1, k+1):    
            prevMax = float("-inf") 
            for d in range(1, n):  
                prevMax = max(prevMax, dp[t-1][d-1] - prices[d-1])
                dp[t][d] = max(prevMax + prices[d], dp[t][d-1])
                
        return dp[-1][-1]