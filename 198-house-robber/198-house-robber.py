class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*(n)
        prev1=nums[0]
        prev2=0
        for i in range(1,n):
            take=nums[i]
            if i>1:
                take+=prev2
            not_take=0+prev1
            cur=max(take,not_take)
            prev2=prev1
            prev1=cur
        return prev1