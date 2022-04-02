class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=self.find_Start(nums,target)
        end=self.find_End(nums,target)
        return [start,end]
    
    def find_Start(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        start=-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                start=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return start
    
    def find_End(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        end=-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                end=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return end
    
                
