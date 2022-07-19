class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix=[[1 for i in range(row+1)]for row in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                matrix[i][j]=matrix[i-1][j]+matrix[i-1][j-1]
        return matrix
                