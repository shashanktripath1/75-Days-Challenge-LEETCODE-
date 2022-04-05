class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c=d=0
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1] :
                c+=1
            if nums[i]>=nums[i+1]:
                d+=1
        return c==len(nums)-1 or d==len(nums)-1