class Solution:
    def helper(self,ind,ds,nums,ans):
        if ind==len(nums):
            ans.append(ds[:])
            return ans
        ds.append(nums[ind])
        self.helper(ind+1,ds,nums,ans)
        ds.pop()
        return self.helper(ind+1,ds,nums,ans)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.helper(0,[],nums,ans)
        return ans