import math
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        middle=nums[len(nums)//2]
        for i in nums:
            count+=abs(middle-i)
        return count