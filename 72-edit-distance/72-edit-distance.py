#one based indexing for tabulation to avoid minus indexes
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def f(i,j,dp):
            if i==0:
                return j
            if j==0:
                return i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i-1]==word2[j-1]:
                return 0+f(i-1,j-1,dp)
            insert=1+f(i,j-1,dp)
            delete=1+f(i-1,j,dp)
            replace=1+f(i-1,j-1,dp)
            dp[i][j]= min(insert,min(delete,replace))
            return dp[i][j]
        n=len(word1)
        m=len(word2)
        dp=[[-1 for _ in range(m+1)]for _ in range(n+1)]
        return f(n,m,dp)