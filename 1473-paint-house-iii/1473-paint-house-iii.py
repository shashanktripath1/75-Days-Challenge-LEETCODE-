class Solution:
    def minCost(self, houses, cost, m, n, target):
        
        @cache
        def dp(i, remain, last_elem):

            if i == len(houses):
                if remain == 0:
                    return 0 # valid coloring
                else:
                    return inf # reached last without hitting target
            
            if i == len(houses) or remain == -1:
                return inf
            
            m = inf
            
            if houses[i] == -1:
                # we can only color this house
                for color in range(n):
                    if color == last_elem:
                        m = min(cost[i][color] + dp(i+1, remain, color), m)
                    else:
                        m = min(cost[i][color] + dp(i+1, remain - 1, color), m)
            else:
                # we cant color this house
                if last_elem == houses[i]:
                    # same neighbour hood
                    m = dp(i+1, remain, last_elem)
                else:
                    m = dp(i+1, remain - 1, houses[i])
            
            return m

        houses = [i-1 for i in houses]
        ans = dp(0, target, -1)
        return ans if ans != inf else -1