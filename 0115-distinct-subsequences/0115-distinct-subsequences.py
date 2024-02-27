class Solution:
    @cache
    def f(self,i,j,s,t):
        if j<0:
            return 1
        if i<0:
            return 0
        if s[i]==t[j]:
            return self.f(i-1,j-1,s,t)+self.f(i-1,j,s,t)
        
        return self.f(i-1,j,s,t)
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        return self.f(m-1,n-1,s,t)