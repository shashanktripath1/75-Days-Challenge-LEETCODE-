class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxa=max(nums)
        mina=min(nums)
        return max(0,maxa-k-(mina+k))
        