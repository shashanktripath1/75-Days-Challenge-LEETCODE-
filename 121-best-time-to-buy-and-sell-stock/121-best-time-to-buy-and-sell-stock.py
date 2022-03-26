class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxs=0
        mins=prices[0]
        for i in range(len(prices)):
            mins=min(mins,prices[i])
            profit=prices[i]-mins
            maxs=max(maxs,profit)
        return maxs
        