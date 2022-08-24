class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def f(i,j,dp):
            if(i==0 and j==0):
                return grid[0][0]
            if i<0 or j<0:
                return 9999999
            if dp[i][j]!=-1:
                return dp[i][j]
            up=grid[i][j]+f(i-1,j,dp)
            left=grid[i][j]+f(i,j-1,dp)
            dp[i][j]= min(up,left)
            return dp[i][j]
        m,n=len(grid),len(grid[0])
        dp=[[-1]*(n) for i in range(m)]
        return f(m-1,n-1,dp)