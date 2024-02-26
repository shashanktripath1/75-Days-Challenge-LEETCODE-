class Solution:
    def f(self,ind1,ind2,s1,s2,dp):
        if ind1<0 or ind2<0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if s1[ind1]==s2[ind2]:
            dp[ind1][ind2]=1+self.f(ind1-1,ind2-1,s1,s2,dp)
        else:
            dp[ind1][ind2]=0+max(self.f(ind1-1,ind2,s1,s2,dp),self.f(ind1,ind2-1,s1,s2,dp))
        return dp[ind1][ind2]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[-1 for j in range(n+1)]for i in range(m+1)]
        return self.f(m-1,n-1,text1,text2,dp)
        