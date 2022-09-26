#tabulation
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        for ind in range(n-1,-1,-1):
            len1=0
            max_ans=float('-inf')
            maxi=float('-inf')
            for j in range(ind,min(n,ind+k)):
                len1+=1
                maxi=max(maxi,arr[j])
                sum1=(len1 * maxi)+dp[j+1]
                max_ans=max(max_ans,sum1)
            dp[ind]=max_ans
        return dp[ind]