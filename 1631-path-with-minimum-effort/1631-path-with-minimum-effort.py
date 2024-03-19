import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        pq=[(0,0,0)]
        heapq.heapify(pq)
        rows,cols=len(heights),len(heights[0])
        dist=[[float('inf')]*(cols)for _ in range(rows)]
        dist[0][0]=0
        while pq:
            effort,row,col=heapq.heappop(pq)
            if row==rows-1 and col==cols-1:
                return effort
            for dr,dc in directions:
                new_row,new_col=row+dr,col+dc
                if 0<=new_row<rows and 0<=new_col<cols:
                    new_effort=max(effort,abs(heights[row][col]-heights[new_row][new_col]))
                    if new_effort<dist[new_row][new_col]:
                        dist[new_row][new_col]=new_effort
                        heapq.heappush(pq,(new_effort,new_row,new_col))
        return -1
                                   