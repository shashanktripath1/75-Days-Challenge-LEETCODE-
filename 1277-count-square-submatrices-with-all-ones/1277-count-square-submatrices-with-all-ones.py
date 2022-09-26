class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])
        dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
        for j in range(m):
            dp[0][j]=matrix[0][j]
        for i in range(n):
            dp[i][0]=matrix[i][0]
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1]))
        sum1=0
        for i in range(n):
            for j in range(m):
                sum1+=dp[i][j]
        return sum1