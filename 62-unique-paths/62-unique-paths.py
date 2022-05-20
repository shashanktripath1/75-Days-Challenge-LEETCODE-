class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for i in range(n)]for j in range(m)]
        for col in range(n):
            dp[0][col]=1
        for row in range(m):
            dp[row][0]=1
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col]=dp[row][col-1]+dp[row-1][col]
        return dp[m-1][n-1]
        