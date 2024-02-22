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
        n=len(triangle)
        front=[0]*n
        #basecase
        for i in range(n):
            front[i]=triangle[n-1][i]
        for i in range(n-2,-1,-1):
            cur=[0]*n
            for j in range(i,-1,-1):
                down=triangle[i][j]+front[j]
                diagonal=triangle[i][j]+front[j+1]
                cur[j]=min(down,diagonal)
            front=cur
        return front[0]
            