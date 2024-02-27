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
        prev=[0]*(n+1)
        cur=[0]*(n+1)
        prev[0]=cur[0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    cur[j]=prev[j-1]+prev[j]
                else:
                    cur[j]=prev[j]
            prev=cur[:]
        return prev[n]
        