class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetSumToK(n, k, arr):
            dp = [[False for i in range(k+1)] for j in range(n+1)]
            for i in range(n):
                dp[i][0]=True
            for ind in range(1,n):
                for target in range(1,k+1):
                    not_take=dp[ind-1][target]
                    take=False
                    if arr[ind]<=target:
                        take=dp[ind-1][target-arr[ind]]
                    dp[ind][target]=take or not_take
            return dp[n-1][k]
        n=len(nums)
        total_sum=sum(nums)
        target=total_sum//2
        if total_sum%2!=0:
            return False
        return subsetSumToK(n, target, nums)