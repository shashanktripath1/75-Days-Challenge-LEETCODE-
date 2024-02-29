class Solution:
    def f(self,ind,buy,n,prices,dp):
        if ind>=n:
            return 0
        if dp[ind][buy]!=-1:
            return dp[ind][buy]
        if(buy==0):
            op1=0+self.f(ind+1,0,n,prices,dp)
            op2=-prices[ind]+self.f(ind+1,1,n,prices,dp)
        if buy==1:
            op1=0+self.f(ind+1,1,n,prices,dp)
            op2=prices[ind]+self.f(ind+2,0,n,prices,dp)
        dp[ind][buy]=max(op1,op2)
        return dp[ind][buy]
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        cur = [0, 0]
        front = [0, 0]
        front2 = [0, 0]        
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if(buy==0):
                    op1=0+front[0]
                    op2=-prices[ind]+front[1]
                else:
                    op1=0+front[1]
                    op2=prices[ind]+front2[0]
                cur[buy]=max(op1,op2)
            front2 = front.copy()
            front = cur.copy()
        return cur[0]