class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        d1,d2={},{}
        for i in word1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in word2:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        return d1.keys()==d2.keys() and sorted(d1.values())==sorted(d2.values())