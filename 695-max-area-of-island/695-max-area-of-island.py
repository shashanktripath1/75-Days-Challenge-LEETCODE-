class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len=len(grid)
        col_len=len(grid[0])
        visited=set()
        def dfs(r,c):
            if r<0 or r==row_len or c<0 or c==col_len or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return 1+dfs(r,c+1)+dfs(r,c-1)+dfs(r+1,c)+dfs(r-1,c)
        area=0
        for r in range(row_len):
            for c in range(col_len):
                area=max(area,dfs(r,c))
        return area