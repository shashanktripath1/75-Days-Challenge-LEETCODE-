#BRUTE FORCE
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    self.markRow(matrix,i,m,n)
                    self.markCol(matrix,j,m,n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==-123455:
                    matrix[i][j]=0
        return matrix
    def markRow(self,matrix,i,m,n):
        for j in range(n):
            if matrix[i][j]!=0:
                matrix[i][j]=-123455
    def markCol(self,matrix,j,m,n):
        for i in range(m):
            if matrix[i][j]!=0:
                matrix[i][j]=-123455
    
            
        