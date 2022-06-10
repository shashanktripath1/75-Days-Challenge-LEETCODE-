class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        maxlen=start=0
        seen=set()
        for i in s:
            while i in seen:
                seen.remove(s[start])
                start+=1
            seen.add(i)
            maxlen=max(len(seen),maxlen)
        return maxlen
        