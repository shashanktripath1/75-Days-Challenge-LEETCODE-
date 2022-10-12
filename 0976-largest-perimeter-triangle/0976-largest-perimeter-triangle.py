class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0
        nums.sort(reverse=True)
        for i in range(3,n+1):
            if nums[i-1]+nums[i-2]>nums[i-3]:
                return sum(nums[i-3:i])
        return 0
                