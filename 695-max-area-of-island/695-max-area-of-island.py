class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        
        def dfs(r,c):
            if(r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1)
                   )
        
        area = 0
        for r in range(rows):
            for c in range(cols):
                    area = max(area, dfs(r,c))
        return area