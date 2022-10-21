class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def f(ind1,ind2,dp):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if text1[ind1]==text2[ind2]:
                dp[ind1][ind2]=1+f(ind1-1,ind2-1,dp)
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2]= max(f(ind1-1,ind2,dp),f(ind1,ind2-1,dp))
                return dp[ind1][ind2]
                
            
            
        m,n=len(text1),len(text2)
        dp=[[-1 for _ in range(n+1)]for _ in range(m+1)]
        return f(m-1,n-1,dp)