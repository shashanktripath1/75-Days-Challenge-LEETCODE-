class Solution:
    def f(self,ind,k,arr,n,dp):
        if ind==n:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        len1=0
        max_ans=float('-inf')
        maxi=float('-inf')
        for j in range(ind,min(ind+k,n)):
            len1+=1
            maxi=max(maxi,arr[j])
            summation=maxi*len1 +self.f(j+1,k,arr,n,dp)
            max_ans=max(max_ans,summation)
        dp[ind]=max_ans
        return dp[ind]
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        for ind in range(n-1,-1,-1):
            len1=0
            max_ans=float('-inf')
            maxi=float('-inf')
            for j in range(ind,min(ind+k,n)):
                len1+=1
                maxi=max(maxi,arr[j])
                summation=maxi*len1 +self.f(j+1,k,arr,n,dp)
                max_ans=max(max_ans,summation)
            dp[ind]=max_ans
        return dp[0]
        