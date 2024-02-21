#MEMOIZATION
class Solution:
    def f(self,n,dp):
        prev2=1
        prev=1
        for i in range(2,n+1):
            cur=prev+prev2
            prev2=prev
            prev=cur
        return prev
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.f(n,dp)