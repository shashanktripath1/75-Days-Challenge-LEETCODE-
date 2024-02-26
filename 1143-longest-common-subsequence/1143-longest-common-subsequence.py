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
        prev=[0]*(n+1)
        cur=[0]*(n+1)
        for ind1 in range(1,m+1):
            for ind2 in range(1,n+1):
                if text1[ind1-1]==text2[ind2-1]:
                    cur[ind2]=1+prev[ind2-1]
                else:
                    cur[ind2]=0+max(prev[ind2],cur[ind2-1])
            prev=cur[:]
        return prev[n]
                
        