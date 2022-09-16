class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def f(i,j,s,t,dp):
            if j<0:
                return 1
            if i<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j]= f(i-1,j-1,s,t,dp)+f(i-1,j,s,t,dp)
                return dp[i][j]
            
            dp[i][j]=f(i-1,j,s,t,dp)
            return dp[i][j]
        n=len(s)
        m=len(t)
        dp=[[-1 for i in range(m+1)]for j in range(n+1)]
        return f(n-1,m-1,s,t,dp)