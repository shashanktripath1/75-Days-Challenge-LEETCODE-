class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left,result,product=0,0,1
        for right in range(len(nums)):
            product*=nums[right]
            if product>=k:
                while product>=k and left<=right:
                    product/=nums[left]
                    left+=1
            result+=right-left+1
        return result
        