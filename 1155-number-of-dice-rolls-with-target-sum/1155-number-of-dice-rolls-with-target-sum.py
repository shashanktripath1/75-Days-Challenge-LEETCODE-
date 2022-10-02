class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        cache = {}
        
        def dp(left, target):
            if target < 0:
                return 0
            if left == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            if (left, target) in cache:
                return cache[(left, target)]
            
            ways = 0
            for i in range(1, k + 1):
                ways += dp(left - 1, target - i)
                ways %= MOD
            cache[(left, target)] = ways
            return ways
        
        return dp(n, target)