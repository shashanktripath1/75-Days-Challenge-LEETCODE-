class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        if not matrix:
            return False
        def helper(row):
            low,high=0,n-1
            while low<=high:
                mid=(low+high)//2
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return False
        for row in range(m):
            if helper(row):
                return True
        return False