class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a=n+m-2
        b=m-1
        res=1
        for i in range(1,b+1):
            res=res*(a-b+i)/i
        return int(res)