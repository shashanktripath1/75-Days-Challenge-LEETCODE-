class Solution:
    def first_occurence(self,nums,n,target):
        low,high=0,n-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return ans
                
        
    def last_occurence(self,nums,n,target):
        low,high=0,n-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        first_occ=self.first_occurence(nums,n,target)
        last_occ=self.last_occurence(nums,n,target)
        return [first_occ,last_occ]
    