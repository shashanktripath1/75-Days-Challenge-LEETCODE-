class Solution:
    def cal_total_hours(self,piles,hourly):
        total_hour=0
        n=len(piles)
        for i in range(n):
            total_hour+=math.ceil(piles[i]/hourly)
        return total_hour
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            total_hours=self.cal_total_hours(piles,mid)
            if total_hours<=h:
                high=mid-1
            else:
                low=mid+1
        return low