class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c=len(cuts)
        cuts.append(n)
        cuts.insert(0,0)
        cuts.sort()
        dp=[[0 for _ in range(c+2)]for _ in range(c+2)]
        for i in range(c,0,-1):
            for j in range(1,c+1):
                if i>j:
                    continue
                mini=float('inf')
                for ind in range(i,j+1):
                    cost=cuts[j+1]-cuts[i-1]+dp[i][ind-1]+dp[ind+1][j]
                    mini=min(mini,cost)
                dp[i][j]=mini
        return dp[1][c]
                
    