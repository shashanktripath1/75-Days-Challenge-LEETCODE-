class Solution:
   #Flattening 2D array into 1D array hypothetically not technically
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        low=0
        high=m*n-1
        while low<=high:
            mid=(low+high)//2
            row=mid//n
            col=mid%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high=mid-1
            else:
                low=mid+1
        return False