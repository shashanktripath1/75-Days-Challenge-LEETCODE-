class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        scores = [s for a,s in sorted(zip(ages, scores))]
        dp = scores[:]
        max_score = scores[0]
        for curr in range(1, N):
            for prev in range(curr):
                if scores[prev] <= scores[curr]:
                    dp[curr] = max(dp[curr], dp[prev] + scores[curr])
            max_score = max(max_score, dp[curr])
        return max_score