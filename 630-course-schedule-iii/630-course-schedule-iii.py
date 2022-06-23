from heapq import heappush, heappop, heapify

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x : x[1])
        totalDuration = 0
        
        heap = []
        heapify(heap)
        
        for duration, lastDay in courses:
            totalDuration += duration
            heappush(heap, -1*duration)
            
            if totalDuration > lastDay:
                totalDuration -= -1*heappop(heap)
        
        maximumDuration = len(heap)
        return maximumDuration