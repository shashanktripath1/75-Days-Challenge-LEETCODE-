class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def f(i,j):
            if i<0 and j<0:
                return True
            if j<0 and i>=0:
                return False
            if i<0 and j>=0:
                for ii in range(j+1):
                    if p[ii]!='*':
                        return False
                return True
            if s[i]==p[j] or p[j]=="?":
                return f(i-1,j-1)
            if p[j]=="*":
                return f(i-1,j) or f(i,j-1)
            return False

        n=len(s)
        m=len(p)
        return f(n-1,m-1)