from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        q=deque()
        fresh_coordinates=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh_coordinates+=1
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        minute=0
        while q:
            q_size=len(q)
            for _ in range(q_size):
                r,c=q.popleft()
                for d in directions:
                    nr,nc=r+d[0],c+d[1]
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh_coordinates-=1
                        q.append((nr,nc))
            if q:
                minute+=1
        return minute if not fresh_coordinates else -1