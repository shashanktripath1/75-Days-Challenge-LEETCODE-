class Solution:
    def findMax(self, col, matrix, rows):
        maxi = float('-inf')
        rownum = -1
        for i in range(rows):
            if maxi < matrix[i][col]:
                maxi = matrix[i][col]
                rownum = i
        return rownum

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high)//2
            row = self.findMax(mid, mat, n)
            left = right = -1
            if mid-1 >= 0:
                left = mat[row][mid-1]
            if mid+1 < m:
                right = mat[row][mid+1]
            if (mat[row][mid] > left) and (mat[row][mid] > right):
                return [row, mid]
            elif mat[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1        