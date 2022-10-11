class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            grid[i][j]=0
            bfs(i+1,j)
            bfs(i-1,j)
            bfs(i,j-1)
            bfs(i,j+1)
        
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and grid[i][j]==1:
                    bfs(i,j)
        count=0            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
        return count
                    

