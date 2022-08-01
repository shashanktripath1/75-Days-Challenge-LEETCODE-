class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i,j):
            if i==m-1 or j==n-1:
                return 1
            if dp[i][j]!=0:
                return dp[i][j]
            dp[i][j]=helper(i+1,j)+helper(i,j+1)
            return dp[i][j]
        dp=[[0 for i in range(n)]for j in range(m)]
        return helper(0,0)