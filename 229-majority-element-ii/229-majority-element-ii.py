class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for key,value in d.items():
            if value>len(nums)/3:
                res.append(key)
        return res