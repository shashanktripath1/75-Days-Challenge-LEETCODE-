class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        prev=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[j]=grid[i][j]
                else:
                    up=grid[i][j]
                    if i>0:
                        up+=prev[j]
                    else:
                        up=int(1e9)
                    left=grid[i][j]
                    if j>0:
                        left+=temp[j-1]
                    else:
                        left=int(1e9)
                    temp[j]=min(up,left)
            prev=temp
        return prev[n-1]