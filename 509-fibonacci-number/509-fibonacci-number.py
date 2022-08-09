class Solution:
    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        if n<=1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.fib(n-1)+self.fib(n-2)
        return dp[n]