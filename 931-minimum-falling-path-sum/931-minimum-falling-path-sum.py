class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def f(i,j,dp):
            if j<0 or j>=n:
                return 1e9
            if i==0:
                return matrix[0][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            up=matrix[i][j]+f(i-1,j,dp)
            left_diagonal=matrix[i][j]+f(i-1,j-1,dp)
            right_diagonal=matrix[i][j]+f(i-1,j+1,dp)
            dp[i][j]= min(up,min(left_diagonal,right_diagonal))
            return dp[i][j]
        m,n=len(matrix),len(matrix[0])
        dp=[[-1]*(n) for i in range(m)]
        mini=float('inf')
        for j in range(n):
            mini=min(mini,f(m-1,j,dp))
        return mini