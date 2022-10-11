class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        left,mid=float('inf'),float('inf')
        for i in nums:
            if i>mid:
                return True
            elif i>left and i<mid:
                mid=i
            elif i<left:
                left=i
        return False

