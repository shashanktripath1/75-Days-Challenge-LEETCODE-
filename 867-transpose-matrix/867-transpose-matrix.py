class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,cols=len(matrix),len(matrix[0])
        mat=[[None]*rows for r in range(cols)]
        for r in range(rows):
            for c in range(cols):
                mat[c][r]=matrix[r][c]
        return mat
        