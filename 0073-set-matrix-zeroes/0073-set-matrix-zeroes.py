class Solution:
    def mark_row(self,matrix,m,n,i):
        for j in range(n):
            if matrix[i][j]!=0:
                matrix[i][j]=-12345
    def mark_col(self,matrix,m,n,j):
        for i in range(m):
            if matrix[i][j]!=0:
                matrix[i][j]=-12345
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    self.mark_row(matrix,m,n,i)
                    self.mark_col(matrix,m,n,j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]== -12345:
                    matrix[i][j]=0
        return matrix
                    