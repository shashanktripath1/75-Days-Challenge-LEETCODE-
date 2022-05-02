class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ptr=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[ptr],nums[i]=nums[i],nums[ptr]
                ptr+=1
        return nums
        