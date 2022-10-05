class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited,queue=set(),deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    visited.add((row,col))
                elif grid[row][col]==2:
                    queue.append((row,col))
        ans=0
        while visited and queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for neighbours in ((r,c-1),(r,c+1),(r-1,c),(r+1,c)):
                    if neighbours in visited:
                        visited.remove(neighbours)
                        queue.append(neighbours)
            ans+=1
        return -1 if visited else ans
