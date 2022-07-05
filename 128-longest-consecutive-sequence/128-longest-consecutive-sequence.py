class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        nums=sorted(nums)
        curMax=ans=0
        for i in range(len(nums)):
            if (i+1<len(nums) and nums[i+1]-nums[i]==1):
                curMax+=1
            elif (i+1<len(nums) and nums[i+1]-nums[i]==0):
                continue
            else:
                if (curMax>ans):
                    ans=curMax
                curMax=0
        return ans+1
            