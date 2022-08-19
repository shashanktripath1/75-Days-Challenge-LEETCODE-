class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n-1)%(K-1)!=0:
            return -1
        dp = [[0]*n for _ in range(n)]
        sums = [0]*(n+1)
        for i in range(1,n+1):
            sums[i] = sums[i-1]+stones[i-1]
        for length in range(K,n+1):
            for i in range(n-length+1):
                j = i+length-1
                dp[i][j] = float('inf')
                for t in range(i,j,K-1):
                    dp[i][j] = min(dp[i][j], dp[i][t]+dp[t+1][j])
                if (j-i)%(K-1)==0:
                    dp[i][j] += sums[j+1]-sums[i]
        return dp[0][n-1]