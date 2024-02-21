#Space Optimized
class Solution:
    def f(self,ind,arr,dp):
        if ind==0:
            return arr[ind]
        if ind<0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        pick=arr[ind]+self.f(ind-2,arr,dp)
        not_pick=0+self.f(ind-1,arr,dp)
        dp[ind]=max(pick,not_pick)
        return dp[ind]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=prev2
            not_pick=0+prev
            cur=max(pick,not_pick)
            prev2=prev
            prev=cur
        return prev