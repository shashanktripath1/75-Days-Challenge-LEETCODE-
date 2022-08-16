class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=collections.Counter(s)
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1