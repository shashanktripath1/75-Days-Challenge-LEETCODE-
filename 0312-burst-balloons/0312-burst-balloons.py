class Solution:
    
    def f(self,i,j,nums,dp):
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        maxi=float('-inf')
        for ind in range(i,j+1):
            cost=nums[i-1] * nums[ind] * nums[j+1] +self.f(i,ind-1,nums,dp)+self.f(ind+1,j,nums,dp)
            maxi=max(maxi,cost)
        dp[i][j]=maxi
        return dp[i][j]
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.append(1)
        nums.insert(0,1)
        dp=[[-1 for _ in range(n+1)]for _ in range(n+1)]
        return self.f(1,n,nums,dp)