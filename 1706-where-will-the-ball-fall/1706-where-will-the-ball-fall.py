class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])
        N, ans = range(n), []

        for pos in N:
            for row in grid:
                direction = row[pos]
                pos += row[pos]

                if pos not in N or row[pos] != direction:
                    ans.append(-1)
                    break                
            else:
                ans.append(pos)
                       
        return ans