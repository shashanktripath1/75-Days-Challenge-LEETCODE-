class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def f(i,j,dp):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=float('inf')
            for ind in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+f(i,ind-1,dp)+f(ind+1,j,dp)
                mini=min(mini,cost)
            dp[i][j]=mini
            return dp[i][j]
               
        c=len(cuts)
        dp=[[-1 for _ in range(c+1)]for _ in range(c+1)]
        cuts.append(n)
        cuts.insert(0,0)
        cuts.sort()
        return f(1,c,dp)