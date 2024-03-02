class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        dp=[1]*(n)
        hash_arr=list(range(n))
        for i in range(n):
            for prev_ind in range(i):
                if nums[i]%nums[prev_ind]==0 and 1+dp[prev_ind]>dp[i]:
                    dp[i]=1+dp[prev_ind]
                    hash_arr[i]=prev_ind
        ans,last_index=-1,-1
        for i in range(n):
            if dp[i]>ans:
                ans=dp[i]
                last_index=i
        result=[]
        result.append(nums[last_index])
        while hash_arr[last_index]!=last_index:
            last_index=hash_arr[last_index]
            result.append(nums[last_index])
        return result
                    