class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos_index=0
        neg_index=1
        ans=[0]*n
        for i in range(n):
            if nums[i]>0:
                ans[pos_index]=nums[i]
                pos_index+=2
            else:
                ans[neg_index]=nums[i]
                neg_index+=2
        return ans
            