class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for pay in range(len(cost)-3,-1,-1):
            cost[pay]+=min(cost[pay+1],cost[pay+2])
        return min(cost[0],cost[1])
            