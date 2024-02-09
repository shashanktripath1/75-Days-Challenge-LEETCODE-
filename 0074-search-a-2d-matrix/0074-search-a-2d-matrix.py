class Solution:
    def Binary_search(self,arr,target):
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            if matrix[i][0]<=target<=matrix[i][n-1]:
                return self.Binary_search(matrix[i],target)
        return False