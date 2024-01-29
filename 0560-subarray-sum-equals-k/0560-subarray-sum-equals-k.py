class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        cum_sum=0
        count=0
        for i in range(len(nums)):
            cum_sum+=nums[i]
            
            if cum_sum-k in d:
                count+=d[cum_sum-k]
            
            if cum_sum in d:
                d[cum_sum]+=1
            else:
                d[cum_sum]=1
        return count
            