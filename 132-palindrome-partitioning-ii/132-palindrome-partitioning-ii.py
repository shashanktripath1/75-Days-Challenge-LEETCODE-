class Solution:
    def minCut(self, s: str) -> int:
        def ispalindrome(s):
            return s==s[::-1]
        def f(i,n,s,dp):
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            temp=""
            min_cost=float('inf')
            for j in range(i,n):
                temp+=s[j]
                if (ispalindrome(temp)):
                    cost=1+f(j+1,n,s,dp)
                    min_cost=min(min_cost,cost)
            dp[i]= min_cost
            return dp[i]
                
        n=len(s)
        dp=[-1]*(n+1)
        return f(0,n,s,dp)-1