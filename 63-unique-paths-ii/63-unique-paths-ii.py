class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def f(i,j,dp):
            if i>=0 and j>=0 and obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            up=f(i-1,j,dp)
            left=f(i,j-1,dp)
            dp[i][j]=left+up
            return dp[i][j]
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[-1]*(n) for i in range(m)]
        return f(m-1,n-1,dp)