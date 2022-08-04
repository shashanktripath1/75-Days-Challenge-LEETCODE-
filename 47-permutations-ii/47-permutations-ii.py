class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()

        def helper(l,r):
            if (l==r):
                res.add(tuple(nums.copy()))
        
            else:
                for i in range(l,r):
                    nums[l],nums[i]=nums[i],nums[l]
                    helper(l+1,r)
                    nums[l],nums[i]=nums[i],nums[l]
                    
        helper(0,len(nums))
        return res