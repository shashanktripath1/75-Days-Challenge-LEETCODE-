class Solution:
    def f(self,i,j,mat,dp):
        if i>=0 and j>=0 and mat[i][j]== 1:
            return 0
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.f(i-1,j,mat,dp)
        left=self.f(i,j-1,mat,dp)
        dp[i][j]=up+left
        return dp[i][j]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1 for i in range(n)]for j in range(m)]
        return self.f(m-1,n-1,obstacleGrid,dp)