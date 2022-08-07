class Solution:
    def countVowelPermutation(self, n: int) -> int:
        res=0
        dp={}
        def rec(l,curr):
            nonlocal dp,res
            if dp.get((l,curr),-1)!=-1:
                res+=dp[l,curr]
                return dp[l,curr]
            if l==0:
                res+=1
                return 1
            if curr=='a':
                m=rec(l-1,'e')
            elif curr=='e':
                m=rec(l-1,'a')+rec(l-1,'i')
            elif curr=='i':
                m=rec(l-1,'a')+rec(l-1,'e')+rec(l-1,'o')+rec(l-1,'u')
            elif curr=='o':
                m=rec(l-1,'u')+rec(l-1,'i')
            else:
                m=rec(l-1,'a')
            dp[l,curr]=m
            return dp[l,curr]
        for i in ['a','e','i','o','u']:
            rec(n-1,i)
        return res%1000000007