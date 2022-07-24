class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col):
            if grid[row][col]==1:
                return True
            if row<=0 or row>=row_len-1 or col<=0 or col>=col_len-1:
                return False
            grid[row][col]=1
            up=dfs(row-1,col)
            down=dfs(row+1,col)
            left=dfs(row,col-1)
            right=dfs(row,col+1)
            return left and right and up and down
        row_len=len(grid)
        col_len=len(grid[0])
        ans=0
        for row in range(1,row_len-1):
            for col in range(1,col_len-1):
                if grid[row][col]==0 and dfs(row,col):
                    ans+=1
        return ans