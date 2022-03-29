from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=dict(collections.Counter(nums))
        '''for i in nums:
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1'''
                
        for i,j in d.items():
            if j>1:
                return i
        