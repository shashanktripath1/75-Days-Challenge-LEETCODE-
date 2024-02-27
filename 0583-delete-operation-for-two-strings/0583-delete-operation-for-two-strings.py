class Solution:
    def lcs(self,s, t) :
        n=len(s)
        m=len(t)
        dp=[[0 for i in range(m+1)]for j in range(n+1)]
        for j in range(m+1):
            dp[0][j]=0
        for i in range(n+1):
            dp[i][0]=0
        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if s[ind1-1]==t[ind2-1]:
                    dp[ind1][ind2]= 1+dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        return dp[n][m]
    def minDistance(self, word1: str, word2: str) -> int:
        return len(word1)+len(word2)-2*self.lcs(word1,word2)