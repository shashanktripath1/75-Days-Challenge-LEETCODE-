class Solution:
    def f(self,i,j,s,t,dp):
        if j<0:
            return 1
        if i<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i]==t[j]:
            dp[i][j]=self.f(i-1,j-1,s,t,dp)+self.f(i-1,j,s,t,dp)
        
        else:
            dp[i][j]=self.f(i-1,j,s,t,dp)
        return dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        dp=[[-1 for j in range(n+1)]for i in range(m+1)]
        return self.f(m-1,n-1,s,t,dp)