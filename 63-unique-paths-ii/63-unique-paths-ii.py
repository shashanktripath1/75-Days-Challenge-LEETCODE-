class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])
        
        # grid that stores the number of ways to reach this cell
        mem = [[0 for _ in range(ncols)] for _ in range(nrows)]
        
        # init first row
        val = 1
        for i in range(ncols):
            if obstacleGrid[0][i] == 1:
                val = 0
            mem[0][i] = val
            
        # init first col
        val = 1
        for i in range(nrows):
            if obstacleGrid[i][0] == 1:
                val = 0
            mem[i][0] = val
            
        # Dynamic programming. Calculate the number of ways to reach each cell
        for row in range(1, nrows):
            for col in range(1, ncols):
                if obstacleGrid[row][col] == 1:
                    mem[row][col] == 0
                else:
                    mem[row][col] = mem[row-1][col] + mem[row][col-1]
            
        #print(mem)
        
        return mem[-1][-1]