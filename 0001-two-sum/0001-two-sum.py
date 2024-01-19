class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        n=len(nums)
        for i in range(n):
            element=nums[i]
            left=target-element
            if left in dic:
                return [i,dic[left]]
            dic[element]=i
        return [-1.-1]
