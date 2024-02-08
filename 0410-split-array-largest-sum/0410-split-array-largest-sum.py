class Solution:
    def find(self,arr,pages):
        n=len(arr)
        students=1
        pages_student=0
        for i in range(n):
            if pages_student+arr[i]<=pages:
                pages_student+=arr[i]
            else:
                students+=1
                pages_student=arr[i]
        return students
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k>n:
            return -1
        low,high=max(nums),sum(nums)
        while low<=high:
            mid=(low+high)//2
            check=self.find(nums,mid)
            if check>k:
                low=mid+1
            else:
                high=mid-1
        return low