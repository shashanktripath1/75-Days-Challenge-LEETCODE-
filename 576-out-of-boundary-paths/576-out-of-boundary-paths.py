class Solution:
		def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
			dp = [[0] * n for _ in range(m)]
			dp[startRow][startColumn] = 1
			MOD = 10**9 + 7
			answer = 0
			for _ in range(maxMove):
				next_dp = [[0] * n for _ in range(m)]
				for r in range(m):
					for c in range(n):
						for nx, ny in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
							if 0 <= nx < m and 0 <= ny < n:
								next_dp[nx][ny] = (next_dp[nx][ny] + dp[r][c]) %  MOD
							else:
								answer = (answer + dp[r][c]) % MOD
				dp = next_dp                 
			return answer