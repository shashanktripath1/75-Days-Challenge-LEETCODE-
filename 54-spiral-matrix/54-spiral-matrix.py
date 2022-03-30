class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row=0
        end_row=len(matrix)
        start_col=0
        end_col=len(matrix[0])
        output=[]
        #right traversing
        while start_row<end_row or start_col<end_col:
            for i in range(start_col,end_col):
                if start_row<end_row:
                    output.append(matrix[start_row][i])
            start_row+=1
        #down traversing
            for i in range(start_row,end_row):
                if start_col<end_col:
                    output.append(matrix[i][end_col-1])
            end_col-=1
        #left traversing
            for i in range(end_col-1,start_col-1,-1):
                if start_row<end_row:
                    output.append(matrix[end_row-1][i])
            end_row-=1
        #up traversing
            for i in range(end_row-1,start_row-1,-1):
                if start_col<end_col:
                    output.append(matrix[i][start_col])
            start_col+=1
        return output
        