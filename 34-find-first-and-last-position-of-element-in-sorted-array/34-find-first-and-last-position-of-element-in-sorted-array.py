class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=self.find_start(nums,target)
        end=self.find_end(nums,target)
        return [start,end]
    def find_start(self,nums:List[int],target:int)->List[int]:
        low,high=0,len(nums)-1
        start=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                start=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return start
                
        
    def find_end(self,nums:List[int],target:int)->List[int]:
        low,high=0,len(nums)-1
        end=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                end=mid
                low=mid+1               
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return end
                