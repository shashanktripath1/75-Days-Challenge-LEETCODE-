class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0 for _ in range(n)]for _ in range(m)]
        for j in range(n):
            dp[0][j]=matrix[0][j]
        for i in range(m):
            dp[i][0]=matrix[i][0]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]))
        ans=0
        for i in range(m):
            for j in range(n):
                ans+=dp[i][j]
        return ans
        