class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if(i==0 and j==0):
                    dp[i][j]=grid[i][j]

                else:
                    up=grid[i][j]
                    if i>0:
                        up+=dp[i-1][j]
                    else:
                        up+=1e9
                    left=grid[i][j]
                    if j>0:
                        left+=dp[i][j-1]
                    else:
                        left+=1e9
                    dp[i][j]=min(up,left)
        return dp[m-1][n-1]
                
                