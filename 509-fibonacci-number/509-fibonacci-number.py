class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        prev1,prev2=1,0
        for i in range(2,n+1):
            cur=prev1+prev2
            prev2=prev1
            prev1=cur
        return prev1
        