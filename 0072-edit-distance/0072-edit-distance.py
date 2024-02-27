class Solution:
    @cache
    def f(self,i,j,word1,word2):
        if i<0:
            return j+1
        if j<0:
            return i+1
        if word1[i]==word2[j]:
            return 0+self.f(i-1,j-1,word1,word2)
        insert=1+self.f(i,j-1,word1,word2)
        delete=1+self.f(i-1,j,word1,word2)
        replace=1+self.f(i-1,j-1,word1,word2)
        return min(insert,min(delete,replace))
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        return self.f(m-1,n-1,word1,word2)