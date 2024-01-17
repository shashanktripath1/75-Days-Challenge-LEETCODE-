class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt,maxi=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
                maxi=max(maxi,cnt)
            else:
                cnt=0
        return maxi