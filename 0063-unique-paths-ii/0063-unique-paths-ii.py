class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1]:
            return 0
        prev=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    prev[j]=0
                    continue
                if i==0 and j==0:
                    temp[j]=1
                    continue
                up,left=0,0
                if i>0:
                    up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j]=up+left
            prev=temp
        return prev[n-1]
                
                