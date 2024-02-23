class Solution:
    def f(self,i,j,grid,dp):
        if j<0 or j>=len(grid[0]) or i<0:
            return float('inf')
        if i==0:
            return grid[0][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        up=grid[i][j]+self.f(i-1,j,grid,dp)
        left_diagonal=grid[i][j]+self.f(i-1,j-1,grid,dp)
        right_diagonal=grid[i][j]+self.f(i-1,j+1,grid,dp)
        dp[i][j]=min(up,min(left_diagonal,right_diagonal))
        return dp[i][j]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        prev=[0]*n
        cur=[0]*n
        for j in range(n):
            prev[j]=matrix[0][j]
        for i in range(1,m):
            for j in range(n):
                up=matrix[i][j]+prev[j]
                left_diagonal=0
                if j-1>=0:
                    left_diagonal=matrix[i][j]+prev[j-1]
                else:
                    left_diagonal+=float('inf')
                right_diagonal=0
                if j+1<n:
                    right_diagonal=matrix[i][j]+prev[j+1]
                else:
                    right_diagonal+=float('inf')
                cur[j]=min(up,min(left_diagonal,right_diagonal))
            prev=cur[:]
        mini=float('inf')
        for j in range(n):
            mini=min(mini,prev[j])
        return mini
        