class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            queue=deque()
            queue.append((i,j))
            visited.add((i,j))
            while queue:
                r,c=queue.popleft()
                directions=[(0,1),(0,-1),(1,0),(-1,0)]
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if row in range(m) and col in range(n) and grid[row][col]=='1' and (row,col) not in visited:
                        queue.append((row,col))
                        visited.add((row,col))

        m,n=len(grid),len(grid[0])
        visited=set()
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    ans+=1
                    bfs(i,j)
        return ans


