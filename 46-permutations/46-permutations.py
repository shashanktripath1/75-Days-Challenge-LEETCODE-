class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recurpermutate(ds, freq):
            if len(ds)==len(nums):
                ans.append(list(ds))
                return
            for i in range(len(freq)):
                if freq[i]==0:
                    ds.append(nums[i])
                    freq[i]=1
                    recurpermutate(ds, freq)
                    freq[i]=0
                    ds.pop()
        ans=[]
        freq=[0]*len(nums)
        ds=[]
        recurpermutate(ds, freq)
        return ans
