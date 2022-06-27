import math
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def ncr(n,r):
            f=math.factorial
            return f(n) // (f(r)*f(n-r))
        def method1(nums):
            if len(nums)<=2:
                return 1
            left,right=[],[]
            for i in range(1,len(nums)):
                if nums[i]>nums[0]:
                    right.append(nums[i])
                if nums[i]<nums[0]:
                    left.append(nums[i])
            return ncr(len(left)+len(right),len(left))*method1(left)*method1(right)
        return (method1(nums)-1)%(10**9+7)
            