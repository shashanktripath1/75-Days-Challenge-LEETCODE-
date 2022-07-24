class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n=len(matrix[0])
        m=len(matrix)
        def binarySearch(row):
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return False
        for row in range(m):
            if binarySearch(row):
                return True
        return False
            
                
        