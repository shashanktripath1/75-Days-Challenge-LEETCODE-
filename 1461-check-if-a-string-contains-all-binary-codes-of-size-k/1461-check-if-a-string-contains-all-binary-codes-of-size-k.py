class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset=set()
        for i in range(len(s)-k+1):
            hashset.add(s[i:i+k])
        return len(hashset)==2**k