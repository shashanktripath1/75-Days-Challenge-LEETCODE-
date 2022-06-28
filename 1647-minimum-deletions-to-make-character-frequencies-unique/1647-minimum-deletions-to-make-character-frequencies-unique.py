class Solution:
    def minDeletions(self, s: str) -> int:
        hash_map=collections.Counter(s)
        deletions=0
        freq_set=set()
        for key,value in hash_map.items():
            while value>0 and value in freq_set:
                value-=1
                deletions+=1
            freq_set.add(value)
        return deletions
        