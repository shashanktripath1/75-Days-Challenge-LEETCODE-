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
        dp=[0]*(n+1)
        dp[n]=0
        for i in range(n-1,-1,-1):
            temp=""
            min_cost=float('inf')
            for j in range(i,n):
                temp+=s[j]
                if (ispalindrome(temp)):
                    cost=1+dp[j+1]
                    min_cost=min(min_cost,cost)
            dp[i]= min_cost
        return dp[0]-1