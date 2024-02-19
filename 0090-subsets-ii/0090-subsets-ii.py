class Solution:
    def helper(self,ind,ds,nums,ans):
        if ind==len(nums):
            ans.add(tuple(ds))
            return ans
        ds.append(nums[ind])
        self.helper(ind+1,ds,nums,ans)
        ds.pop()
        return self.helper(ind+1,ds,nums,ans)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        self.helper(0,[],nums,ans)
        return ans