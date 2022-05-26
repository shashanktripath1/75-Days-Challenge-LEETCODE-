class Solution:
    def hammingWeight(self, n: int) -> int:
        a=bin(n).count('1')
        return a
        