class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def f(ind,k,dp):
            if ind==n:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            len1=0
            max_ans=float('-inf')
            maxi=float('-inf')
            for j in range(ind,min(n,ind+k)):
                len1+=1
                maxi=max(maxi,arr[j])
                sum1=(len1 * maxi)+f(j+1,k,dp)
                max_ans=max(max_ans,sum1)
            dp[ind]=max_ans
            return dp[ind]
            

        n=len(arr)
        dp=[-1]*(n+1)
        return f(0,k,dp)