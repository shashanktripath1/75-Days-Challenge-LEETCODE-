class Solution:
    def f(self,i,j,grid,dp):
        if i==0 and j==0:
            return grid[0][0]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        up=grid[i][j]+self.f(i-1,j,grid,dp)
        left=grid[i][j]+self.f(i,j-1,grid,dp)
        dp[i][j]=min(up,left)
        return dp[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    up,left=0,0
                    if i>0:
                        up=grid[i][j]+dp[i-1][j]
                    else:
                        up+=int(1e9)
                    if j>0:
                        left=grid[i][j]+dp[i][j-1]
                    else:
                        left+=int(1e9)
                    dp[i][j]=min(up,left)
        return dp[m-1][n-1]
                