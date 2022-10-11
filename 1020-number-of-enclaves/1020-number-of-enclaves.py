class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #this bfs function will make all the boundary 1's and the 1's connected to them as 0
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and grid[i][j]==1:
                    dfs(i,j)
        count=0
        #now counting the remaining 1's and that will be our answer
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
        return count
                    

