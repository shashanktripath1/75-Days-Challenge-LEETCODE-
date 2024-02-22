class Solution:
    def f(self,i,j,triangle,dp):
        n=len(triangle)
        if i==n-1:
            dp[i][j]=triangle[n-1][j]
            return dp[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        down=triangle[i][j]+self.f(i+1,j,triangle,dp)
        diagonal=triangle[i][j]+self.f(i+1,j+1,triangle,dp)
        dp[i][j]=min(down,diagonal)
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m,n=len(triangle),len(triangle[-1])
        dp=[[-1 for i in range(n)]for j in range(m)]
        #basecase
        for i in range(n):
            dp[n-1][i]=triangle[n-1][i]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down=triangle[i][j]+dp[i+1][j]
                diagonal=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down,diagonal)
        return dp[0][0]