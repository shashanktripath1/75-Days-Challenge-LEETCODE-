class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def f(ind,buy,cap):
            if cap==0:
                return 0
            if ind==n:
                return 0
            if buy==1:
                profit=max(-prices[ind]+f(ind+1,0,cap),0+f(ind+1,1,cap))
            else:
                profit=max(prices[ind]+f(ind+1,1,cap-1),0+f(ind+1,0,cap))
            return profit
        n=len(prices)
        return f(0,1,2)