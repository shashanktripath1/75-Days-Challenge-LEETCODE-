class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        def helper(idx,list1):
            if idx==len(nums):
                ans.add(tuple(list1.copy()))
                return
            for i in range(idx,len(nums)):
                if (i!=idx and nums[i]==nums[i-1]):
                    continue
                helper(i+1,list1+[nums[i]])
                return helper(i+1,list1)
        helper(0,[])
        ans = list(ans)
        return ans
                