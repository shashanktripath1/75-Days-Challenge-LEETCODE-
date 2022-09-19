class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def f(i,j,dp):
            if i<0 and j<0:
                return True
            if j<0 and i>=0:
                return False
            if i<0 and j>=0:
                for ii in range(j+1):
                    if p[ii]!='*':
                        return False
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==p[j] or p[j]=="?":
                dp[i][j]= f(i-1,j-1,dp)
                return dp[i][j]
            if p[j]=="*":
                dp[i][j]=f(i-1,j,dp) or f(i,j-1,dp)
                return dp[i][j]
            dp[i][j]=False
            return dp[i][j]

        n=len(s)
        m=len(p)
        dp=[[-1 for i in range(m+1)]for j in range(n+1)]
        return f(n-1,m-1,dp)