class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        maxReach=0+nums[0]
        for i in range(1,len(nums)):
            if (i<=maxReach):
                maxReach=max(i+nums[i],maxReach)
            else:
                break
        return True if maxReach>=len(nums)-1 else False