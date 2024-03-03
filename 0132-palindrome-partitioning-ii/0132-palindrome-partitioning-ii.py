class Solution:
    def  is_palindrome(self,s):
        return s==s[::-1]
    def f(self,i,n,s,dp):
        if i==n:
            return 0
        if dp[i]!=-1:
            return dp[i]
        min_cost=float('inf')
        for j in range(i,n):
            if self.is_palindrome(i,j,s):
                cost=1+self.f(j+1,n,s,dp)
                min_cost=min(cost,min_cost)
        dp[i]=min_cost
        return dp[i]
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            temp=""
            min_cost=float('inf')
            for j in range(i,n):
                temp+=s[j]
                if (self.is_palindrome(temp)):
                    cost=1+dp[j+1]
                    min_cost=min(min_cost,cost)
            dp[i]= min_cost
        return dp[0]-1