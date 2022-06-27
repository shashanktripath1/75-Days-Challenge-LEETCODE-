class Solution:
    def minPartitions(self, n: str) -> int:
        n=list(n)
        mx=n[0]
        for i in range(len(n)):
            if n[i]>mx:
                mx=n[i]
        return mx