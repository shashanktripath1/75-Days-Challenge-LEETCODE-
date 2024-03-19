import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Define directions for moving: up, down, left, right
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # Initialize priority queue
        pq = [(0, 0, 0)]  # (effort, row, col)
        heapq.heapify(pq)
        
        # Initialize distance matrix with infinite values
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        
        while pq:
            # Get the minimum effort cell from the priority queue
            effort, row, col = heapq.heappop(pq)
            
            # If reached the bottom-right cell, return the effort
            if row == rows - 1 and col == cols - 1:
                return effort
            
            # Iterate through adjacent cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is valid
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Calculate new effort as maximum difference in heights
                    new_effort = max(effort, abs(heights[row][col] - heights[new_row][new_col]))
                    
                    # If the new effort is less than previous, update and add to priority queue
                    if new_effort < dist[new_row][new_col]:
                        dist[new_row][new_col] = new_effort
                        heapq.heappush(pq, (new_effort, new_row, new_col))
        
        # If no path found to bottom-right cell, return -1
        return -1

# Example usage:
# heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
# obj = Solution()
# ans = obj.minimumEffortPath(heights)
# print(ans)
