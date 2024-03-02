class Solution:
    def f(self,i,j,cuts,dp):
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini=float('inf')
        for ind in range(i,j+1):
            cost=cuts[j+1]-cuts[i-1]+self.f(i,ind-1,cuts,dp)+self.f(ind+1,j,cuts,dp)
            mini=min(mini,cost)
        dp[i][j]=mini
        return dp[i][j]
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(n)
        cuts.insert(0,0)
        cuts.sort()
        c=len(cuts)
        dp=[[-1 for _ in range(c+1)]for _ in range(c+1)]
        return self.f(1,c-2,cuts,dp)
    