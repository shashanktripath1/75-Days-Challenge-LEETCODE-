class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)
        for _ in range(2):
            for i,e in enumerate(nums):
                while stack and e>nums[stack[-1]]:
                    res[stack.pop()]=e
                stack.append(i)
        return res
        