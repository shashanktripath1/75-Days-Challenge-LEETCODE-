class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini_price=float('inf')
        max_profit=0
        for i in range(n):
            mini_price=min(mini_price,prices[i])
            max_profit=max(prices[i]-mini_price,max_profit)
        return max_profit