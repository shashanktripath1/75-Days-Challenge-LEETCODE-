from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        visited=[[0 for _ in range(n)]for _ in range(m)]
        dist=[[0 for _ in range(n)]for _ in range(m)]
        queue=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    queue.append(((i,j),0))
                    visited[i][j]=1
                else:
                    visited[i][j]=0
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        while queue:
            (row,col),steps=queue.popleft()
            dist[row][col]=steps
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if 0<=nrow<m and 0<=ncol<n and visited[nrow][ncol]==0:
                    visited[nrow][ncol]=1
                    queue.append(((nrow,ncol),steps+1))
        return dist
            