class Solution:
    def minPartitions(self, n: str) -> int:
        mx=0
        for i in n:
            mx=max(mx,int(i))
        return mx