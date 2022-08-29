from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]
        for i in range(k):
            heappush(min_heap,nums[i])
        for i in range(k,len(nums)):
            if nums[i]>min_heap[0]:
                heappop(min_heap)
                heappush(min_heap,nums[i])
        return min_heap[0]
        