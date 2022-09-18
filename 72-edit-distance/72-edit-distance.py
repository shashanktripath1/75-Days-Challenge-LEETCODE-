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
        dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j]=j
        for i in range(n+1):
            dp[i][0]=i
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    insert=1+dp[i][j-1]
                    delete=1+dp[i-1][j]
                    replace=1+dp[i-1][j-1]
                    dp[i][j]= min(insert,min(delete,replace))
        return dp[n][m]
