class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        min_heap = [(0, (0, 0))]
        res = 0
        
        while min_heap:
            w, (r, c) = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            res = max(res, w)
            if (r, c) == (rows - 1, cols - 1):
                break
            ds = (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)
            for dr, dc in ds:
                if dr < 0 or dr >= rows or dc < 0 or dc >= cols:
                    continue
                if (dr, dc) in visited:
                    continue
                diff = abs(heights[r][c] - heights[dr][dc])
                heapq.heappush(min_heap, (diff, (dr, dc)))
                
        return res