class Solution:
    def dfs(self, row, col, vis, mat, delrow, delcol):
        # Mark the current cell as visited
        vis[row][col] = 1
        n = len(mat)
        m = len(mat[0])
        
        # Check all four directions for unvisited 'O's
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            
            # If the neighboring cell is within bounds, unvisited, and 'O', perform DFS
            if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and mat[nrow][ncol] == 'O':
                self.dfs(nrow, ncol, vis, mat, delrow, delcol)
    def solve(self, board: List[List[str]]) -> None:
        n,m=len(board),len(board[0])
        delrow = [-1, 0, 1, 0]  # Directional changes for rows
        delcol = [0, 1, 0, -1]  # Directional changes for columns
        vis=[[0]*m for _ in range(n)]
        #traverse the boundary rows
        for j in range(m):
            # If the cell is unvisited and 'O', perform DFS
            if not vis[0][j] and board[0][j] == 'O':
                self.dfs(0, j, vis, board, delrow, delcol)

            # If the cell is unvisited and 'O', perform DFS
            if not vis[n - 1][j] and board[n - 1][j] == 'O':
                self.dfs(n - 1, j, vis, board, delrow, delcol)
        # Traverse the boundary columns
        for i in range(n):
            # If the cell is unvisited and 'O', perform DFS
            if not vis[i][0] and board[i][0] == 'O':
                self.dfs(i, 0, vis, board, delrow, delcol)

            # If the cell is unvisited and 'O', perform DFS
            if not vis[i][m - 1] and board[i][m - 1] == 'O':
                self.dfs(i, m - 1, vis, board, delrow, delcol)
         # Update the 'O's that are not visited to 'X's
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'
        

        return board