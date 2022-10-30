import heapq
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[-1]*n for _ in range(m)]
        lst=[(0,-1*k,0,0)]
        visited[0][0]=1
        row=[-1,1,0,0]
        col=[0,0,-1,1]
        heapq.heapify(lst)
        while lst:
            steps,k,x,y=heapq.heappop(lst)
            k=-1*k
            # print(x,y,k)
            if x==m-1 and y==n-1:
                return steps
            for i in range(4):
                n_row=x+row[i]
                n_col=y+col[i]
                if n_row>=0 and n_row<m and n_col>=0 and n_col<n and k-grid[n_row][n_col]>=0:
                    if visited[n_row][n_col]==-1 or (visited[n_row][n_col]!=-1 and (visited[n_row][n_col]<k)):
                        heapq.heappush(lst,(steps+1,-1*(k-grid[n_row][n_col]),n_row,n_col))
                        visited[n_row][n_col]=k-grid[n_row][n_col]
        return -1