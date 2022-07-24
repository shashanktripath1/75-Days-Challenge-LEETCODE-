class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if grid[i][j]==1:
                return True
            if i<=0 or i>=m-1 or j<=0 or j>=n-1:
                return False
            grid[i][j]=1
            up=dfs(i-1,j)
            down=dfs(i+1,j)
            left=dfs(i,j-1)
            right=dfs(i,j+1)
            return up and down and left and right
            
        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==0 and dfs(i,j):
                    ans+=1
        return ans