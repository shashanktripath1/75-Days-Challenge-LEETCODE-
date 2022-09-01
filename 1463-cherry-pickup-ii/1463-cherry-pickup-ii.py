class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dp=[[[-1]*m for j in range(m)]for k in range(n)]
        for j1 in range(m):
            for j2 in range(m):
                if j1==j2:
                    dp[n-1][j1][j2]=grid[n-1][j1]
                else:
                    dp[n-1][j1][j2]=grid[n-1][j1]+grid[n-1][j2]
        for i in range(n-2,-1,-1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi=0
                    for di in range(-1,2):
                        for dj in range(-1,2):
                            ans=0
                            if j1 + di < 0 or j1 + di >= m or j2 + dj < 0 or j2 + dj >= m:
                                continue
                            if j1==j2:
                                ans=grid[i][j1]
                            else:
                                ans=grid[i][j1]+grid[i][j2]
                            ans += dp[i + 1][j1 + di][j2 + dj]
                            maxi=max(maxi,ans)
           
                    dp[i][j1][j2]=maxi
        return dp[0][0][m-1]
                