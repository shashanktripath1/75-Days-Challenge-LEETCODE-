class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        peak,valley=0,0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                peak=valley+1
            if nums[i-1]>nums[i]:
                valley=peak+1
        return 1+max(peak,valley)