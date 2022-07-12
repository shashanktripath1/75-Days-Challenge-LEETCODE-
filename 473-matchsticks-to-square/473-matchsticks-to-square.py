class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4
        # basecase 1
        if sum(matchsticks) % k != 0:
            return False
        subsetsums = [0]*k
        target = sum(matchsticks) / k
        matchsticks.sort(reverse=True)
        # basecase 2
        if matchsticks[0] > target:
            return False
        n = len(matchsticks)
        
        def dfs(i):
            if i == n:
                return True
            for j in range(k):
                subsetsums[j] += matchsticks[i]
                if subsetsums[j] <= target and dfs(i + 1):
                    return True
                subsetsums[j] -= matchsticks[i]
                if subsetsums[j] == 0:
                    break
            return False
            
        return dfs(0)