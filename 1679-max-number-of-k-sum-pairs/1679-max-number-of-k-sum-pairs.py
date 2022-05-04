class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        low,high,res=0,len(nums)-1,0
        while low<high:
            cur=nums[low]+nums[high]
            if cur==k:
                res+=1
                low+=1
                high-=1
            elif cur<k:
                low+=1
            else:
                high-=1
        return res