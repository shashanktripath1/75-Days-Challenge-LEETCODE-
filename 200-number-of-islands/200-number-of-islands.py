class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid[i][j]=='0':
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        m,n=len(grid),len(grid[0])
        visited=set()
        ans=0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        return ans


        