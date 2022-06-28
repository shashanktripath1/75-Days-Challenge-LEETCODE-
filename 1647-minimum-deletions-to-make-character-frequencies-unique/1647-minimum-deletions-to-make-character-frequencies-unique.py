class Solution:
    def minDeletions(self, s: str) -> int:
        hash_map={}
        s=list(s)
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]]+=1
            else:
                hash_map[s[i]]=1
        deletions=0
        freq_set=set()
        for key,value in hash_map.items():
            while value>0 and value in freq_set:
                value-=1
                deletions+=1
            freq_set.add(value)
        return deletions
        