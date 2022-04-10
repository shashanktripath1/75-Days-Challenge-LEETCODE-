class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        d=Counter(nums)
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        return list(d.keys())[:k]