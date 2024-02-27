class Solution:
    def f(self,i,j,word1,word2,dp):
        if i<0:
            return j+1
        if j<0:
            return i+1
        if dp[i][j]!=-1:
            return dp[i][j]
        if word1[i]==word2[j]:
            return 0+self.f(i-1,j-1,word1,word2,dp)
        insert=1+self.f(i,j-1,word1,word2,dp)
        delete=1+self.f(i-1,j,word1,word2,dp)
        replace=1+self.f(i-1,j-1,word1,word2,dp)
        dp[i][j]=min(insert,min(delete,replace))
        return dp[i][j]
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[-1 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=0+dp[i-1][j-1]
                else:
                    insert=1+dp[i][j-1]
                    delete=1+dp[i-1][j]
                    replace=1+dp[i-1][j-1]
                    dp[i][j]=min(insert,min(delete,replace))
        return dp[m][n]