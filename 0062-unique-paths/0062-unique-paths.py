class Solution:
    def f(self,i,j,dp):
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.f(i-1,j,dp)
        left=self.f(i,j-1,dp)
        dp[i][j]=up+left
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[0][0]=1
                    continue
                up,left=0,0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        return dp[m-1][n-1]
    