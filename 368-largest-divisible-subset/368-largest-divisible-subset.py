class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        dp=[[x] for x in nums]
        for i in range(len(dp)):
            for j in range(i):
                if nums[j]%nums[i]==0:
                    if len(dp[j])+1>len(dp[i]):
                        dp[i]=dp[j]+[nums[i]]
        res=[]
        for x in dp:
            if len(x)>len(res):
                res=x
        return res