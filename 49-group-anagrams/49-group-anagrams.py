class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in strs:
            key="".join(sorted(i))
            if key not in hashmap:
                hashmap[key]=[i]
            else:
                hashmap[key].append(i)
        return hashmap.values()
    