class Solution:
    def helper(self,nums,freq,ans,ds):
        if len(ds)==len(nums):
            ans.append(ds[:])
            return
        for i in range(len(nums)):
            if  not freq[i]:
                ds.append(nums[i])
                freq[i]=1
                self.helper(nums,freq,ans,ds)
                freq[i]=0
                ds.pop()
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        freq=[0]*len(nums)
        self.helper(nums,freq,ans,ds)
        return ans