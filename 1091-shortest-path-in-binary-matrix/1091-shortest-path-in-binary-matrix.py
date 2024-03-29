from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while queue:
            row, col, path_length = queue.popleft()
            if (row, col) == (n - 1, n - 1):
                return path_length
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0 and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, path_length + 1))
        
        return -1

