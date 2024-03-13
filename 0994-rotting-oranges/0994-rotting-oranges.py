from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        queue=deque()
        count_fresh_oranges=0
        for i in range(R):
            for j in range(C):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    count_fresh_oranges+=1
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        minutes=0
        while queue:
            queue_len=len(queue)
            for _ in range(queue_len):
                r,c=queue.popleft()
                for d in directions:
                    nr,nc=r+d[0],c+d[1]
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        count_fresh_oranges-=1
                        queue.append((nr,nc))
            if queue:
                minutes+=1
        return minutes if not count_fresh_oranges else -1