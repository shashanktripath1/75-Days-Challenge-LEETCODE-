class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def f(i,j1,j2,dp):
            if j1<0 or j1>=m or j2<0 or j2>=m:
                return -1e9
            if i==n-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
            maxi=float('-inf')
            for dj1 in range(-1,2):
                for dj2 in range(-1,2):
                    ans=0
                    if j1==j2:
                        ans=grid[i][j1]
                    else:
                        ans=grid[i][j1]+grid[i][j2]
                    ans+=f(i+1,j1+dj1,j2+dj2,dp)
                    maxi=max(maxi,ans)
            dp[i][j1][j2]=maxi
            return dp[i][j1][j2]
        

        n,m=len(grid),len(grid[0])
        dp = [[[-1 for i in range(m+1)] for j1 in range(n+1)] for j2 in range(n+1)]

        return f(0,0,m-1,dp)