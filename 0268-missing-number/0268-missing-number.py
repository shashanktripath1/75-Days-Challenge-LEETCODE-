class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sonn=(n*(n+1))//2
        sum1=0
        for i in nums:
            sum1+=i
        return (sonn-sum1)