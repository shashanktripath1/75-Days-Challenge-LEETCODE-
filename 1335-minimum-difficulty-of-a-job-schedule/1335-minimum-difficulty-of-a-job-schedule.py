class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
    
        @cache
        def dp(l, d):
            if d == 1:
                return max(jobDifficulty[l:])            
        
            m = jobDifficulty[l]
            ans = float("inf")
            for j in range(l, len(jobDifficulty)-(d-1)):
                m = max(m, jobDifficulty[j])
                ans = min(ans, m+dp(j+1, d-1))
            
            return ans
    
        return dp(0, d)        