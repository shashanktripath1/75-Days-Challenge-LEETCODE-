class Solution:
    def helper(self,ind,nums,ans):
        if ind==len(nums):
            ans.append(nums[:])
            return
        for i in range(ind,len(nums)):
            nums[ind],nums[i]=nums[i],nums[ind]
            self.helper(ind+1,nums,ans)
            nums[ind],nums[i]=nums[i],nums[ind]
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.helper(0,nums,ans)
        return ans