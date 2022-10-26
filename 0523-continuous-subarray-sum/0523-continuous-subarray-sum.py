class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:0}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if s%k not in d:
                d[s%k]=i+1
            elif d[s%k]<i:
                return True
        return False