from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue=deque()
        count=0
        m=len(grid)
        n=len(grid[0])
        visited=[[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j ==0 or i==m-1 or j==n-1 :
                    if grid[i][j]==1:
                        queue.append((i,j))
                        visited[i][j]=1
        deltarow=[1,-1,0,0]
        deltacol=[0,0,1,-1]
        while queue:
            row,col=queue.popleft()
            for i in range(4):
                nr=row+deltarow[i]
                nc=col+deltacol[i]
                if 0<=nr<m and 0<=nc<n and visited[nr][nc]==0 and grid[nr][nc]==1:
                    queue.append((nr,nc))
                    visited[nr][nc]=1
        for i in range(m):
            for j in range(n):
                if visited[i][j]==0 and grid[i][j]==1:
                    count+=1
        return count
                    