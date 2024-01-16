class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        if k != 0:
            m = n - k
            nums[:k], nums[k:] = nums[m:], nums[:m]
        return nums
