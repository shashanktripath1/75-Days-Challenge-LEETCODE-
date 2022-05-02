class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mina=nums[0]
        maxa=nums[-1]
        result=maxa-mina
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                maxa=max(nums[-1]-k,nums[i]+k)
                mina=min(nums[0]+k,nums[i+1]-k)
                result=min(result,maxa-mina)
        return result