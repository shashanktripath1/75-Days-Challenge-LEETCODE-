class Solution:
    def f(self,i,j,dp):
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.f(i-1,j,dp)
        left=self.f(i,j-1,dp)
        dp[i][j]=up+left
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        prev=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[j]=1
                    continue
                up,left=0,0
                if i>0:
                    up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j]=up+left
            prev=temp
        return prev[n-1]