class Solution:
    def helper(self,ind,ds,nums,ans):
        ans.append(ds[:])
        for i in range(ind,len(nums)):
            if i!=ind and nums[i]==nums[i-1]:
                continue
            ds.append(nums[i])
            self.helper(i+1,ds,nums,ans)
            ds.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        ds=[]
        self.helper(0,ds,nums,ans)
        return ans