#one based indexing for tabulation
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def f(i,j,dp):
            if i==0 and j==0:
                return True
            if j==0 and i>0:
                return False
            if i==0 and j>0:
                for ii in range(1,j+1):
                    if p[ii-1]!='*':
                        return False
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i-1]==p[j-1] or p[j-1]=="?":
                dp[i][j]= f(i-1,j-1,dp)
                return dp[i][j]
            if p[j-1]=="*":
                dp[i][j]=f(i-1,j,dp) or f(i,j-1,dp)
                return dp[i][j]
            dp[i][j]=False
            return dp[i][j]

        n=len(s)
        m=len(p)
        dp=[[-1 for i in range(m+1)]for j in range(n+1)]
        return f(n,m,dp)